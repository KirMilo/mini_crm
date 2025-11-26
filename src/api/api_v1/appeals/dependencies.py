from typing import Annotated, Sequence, Any, Coroutine

from fastapi import Depends, Path
from sqlalchemy import select, func, Row
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.appeals.schemas import LeadModel
from core.db.models import Lead, Appeal, Operator, Source, OperatorsToSources
from core.db.session import get_async_session
from core.exceptions.exceptions import SourceNotFound


async def get_existing_lead(
        lead: LeadModel,
        session: AsyncSession = Depends(get_async_session)
) -> Lead | None:
    response = await session.execute(
        select(Lead).where(Lead.email == lead.email)
    )
    return response.scalar_one_or_none()


async def get_lead(
        lead: LeadModel,
        existing_lead: Lead | None = Depends(get_existing_lead),
        session: AsyncSession = Depends(get_async_session),
) -> Lead:
    if existing_lead:
        return existing_lead
    new_lead = Lead(**lead.model_dump())
    session.add(new_lead)
    await session.commit()
    return new_lead


async def get_source(
        source_id: Annotated[int, Path(title="Источник (бот)", ge=1)],
        session: AsyncSession = Depends(get_async_session),
) -> Source:
    source: Source | None = await session.get(Source, source_id)
    if source:
        return source
    raise SourceNotFound(source_id)


async def get_operators(
        source: Source = Depends(get_source),
        session: AsyncSession = Depends(get_async_session),
) -> Sequence[Row[tuple[Operator, int]]]:
    appeals_count = (
        select(func.count(Appeal.id))
        .where(Appeal.operator_id == Operator.id)
        .scalar_subquery()
    )

    stmt = (
        select(Operator, OperatorsToSources.weight)
        .join(OperatorsToSources)
        .where(
            OperatorsToSources.source_id == source.id,
            Operator.is_active == True,
            Operator.req_limit > appeals_count
        )
    )
    response = await session.execute(stmt)
    return response.all()
