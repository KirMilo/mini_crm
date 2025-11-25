from typing import Annotated, Sequence

from fastapi import Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.operators.dependencies import get_operator
from api.api_v1.operators.schemas import CreateOperatorModel, UpdateOperatorModel
from core.db.models import Operator
from core.db.session import get_async_session



async def create_operator(
        operator: CreateOperatorModel,
        session: AsyncSession = Depends(get_async_session),
) -> Operator:
    new_operator = Operator(**operator.model_dump())
    session.add(new_operator)
    await session.commit()
    return new_operator


async def update_operator(
        operator_model: UpdateOperatorModel,
        operator: Operator = Depends(get_operator),
        session: AsyncSession = Depends(get_async_session),
) -> Operator:
    for items in operator_model.model_dump(exclude_none=True, exclude_unset=True).items():
        setattr(operator, *items)
    await session.commit()
    return operator


async def get_operators(
        session: AsyncSession = Depends(get_async_session),
        limit: Annotated[int, Query(gt=0)] = 100,
) -> Sequence[Operator]:
    operators = await session.execute(select(Operator).limit(limit))
    return operators.scalars().all()
