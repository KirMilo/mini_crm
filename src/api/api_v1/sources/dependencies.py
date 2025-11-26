from typing import Sequence, Annotated, Iterable

from fastapi import Depends, Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.sources.schemas import CreateSourceModel, OperatorModel, UpdateSourceModel
from core.db import get_async_session
from core.db.models import Operator, Source, OperatorsToSources
from core.exceptions.exceptions import SourceNotFound


async def get_operators(
        source_model: CreateSourceModel,
        session: AsyncSession = Depends(get_async_session),
) -> Iterable[Operator]:
    if source_model.operators is None:
        return []
    response = await session.execute(
        select(Operator)
        .where(
            Operator.id.in_(
                [operator.id for operator in source_model.operators]
            )
        )
    )
    return response.scalars().all()


def get_operators_weights(
        operators: list[OperatorModel] | None,
) -> dict[int, int] | None:
    return {
        operator.id: operator.weight for operator in operators
    } if operators else None


async def get_source(
        source_id: Annotated[int, Path(title="Source ID")],
        session: AsyncSession = Depends(get_async_session),
):
    source: Source | None = await session.get(Source, source_id)
    if source:
        return source
    raise SourceNotFound(source_id)


async def get_operators_to_source(
        source_id: Annotated[int, Path( title="Source ID")],
        session: AsyncSession = Depends(get_async_session),
) -> Sequence[OperatorsToSources]:
    stmt = (
        select(OperatorsToSources)
        .where(OperatorsToSources.source_id == source_id)
    )
    response = await session.execute(stmt)
    return response.scalars().all()
