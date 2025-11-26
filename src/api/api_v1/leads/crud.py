from itertools import groupby
from typing import Annotated

from fastapi import Depends, Query, Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.leads.schemas import InputLeadModel
from core.db import get_async_session
from core.db.models import Lead, Appeal
from core.exceptions.exceptions import LeadNotFound


async def get_lead_by_id(
        lead_id: Annotated[int, Path(ge=1)],
        session: AsyncSession = Depends(get_async_session)
):
    lead = await session.get(Lead, lead_id)
    if lead:
        return lead
    raise LeadNotFound(lead_id)


async def get_lead_by_email(
        lead_model: InputLeadModel,
        session: AsyncSession = Depends(get_async_session)
) -> Lead:
    response = await session.execute(
        select(Lead)
        .where(Lead.email == lead_model.email)
    )
    lead = response.scalar_one_or_none()
    if lead:
        return lead
    lead = Lead(**lead_model.model_dump())
    session.add(lead)
    await session.commit()
    return lead


async def get_leads_appeals(
        session: AsyncSession = Depends(get_async_session),
        limit: Annotated[int | None, Query(ge=1)] = 100
) -> list[dict[str, ...]]:
    stmt = (
        select(Lead, Appeal)
        .join(Appeal)
        .limit(limit)
    )
    response = await session.execute(stmt)
    leads_appeals = response.all()
    return [
        {"lead": lead, "appeals": [appeal for _, appeal in appeals]}
        for lead, appeals in groupby(
            leads_appeals, key=lambda _: _[0])
    ]
