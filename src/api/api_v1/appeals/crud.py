import random
from typing import Sequence, Annotated

from fastapi import Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.appeals.dependencies import get_operators, get_lead, get_source
from core.db.models import Lead, Appeal, Operator, Source
from core.db.session import get_async_session
from core.exceptions.exceptions import AllOperatorsAreBusy


async def create_appeal(
        source: Source = Depends(get_source),
        lead: Lead = Depends(get_lead),
        operators_weights: Sequence[tuple[Operator, int]] = Depends(get_operators),
        session: AsyncSession = Depends(get_async_session)
) -> Appeal:
    if not operators_weights:
        raise AllOperatorsAreBusy()

    operators = []
    weights = []
    for operator, weight in operators_weights:
        operators.append(operator)
        weights.append(weight)

    operator = random.choices(operators, weights=weights, k=1)
    appeal = Appeal(
        lead=lead,
        source=source,
        operator=operator[0],
    )
    session.add(appeal)
    await session.commit()
    return appeal


async def get_appeals(
        limit: Annotated[int, Query(gt=0)] = 100,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = (
        select(Appeal)

        .limit(limit)
    )
