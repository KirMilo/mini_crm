import random
from typing import Sequence

from fastapi import Depends
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
