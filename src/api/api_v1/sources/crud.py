from typing import Sequence, Iterable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.sources.dependencies import get_operators, get_operators_weights, get_source, get_operators_to_source
from api.api_v1.sources.schemas import CreateSourceModel, OperatorModel, SourceResponseModel, UpdateSourceModel
from core.db import get_async_session
from core.db.models import Operator, Source, OperatorsToSources


async def create_source(
        source_model: CreateSourceModel,
        operators: Iterable[Operator] = Depends(get_operators),
        session: AsyncSession = Depends(get_async_session),
) -> SourceResponseModel:
    weights = get_operators_weights(source_model.operators)

    source = Source(**source_model.model_dump(exclude={"operators"}))
    session.add(source)
    await session.commit()
    for operator in operators:
        session.add(
            OperatorsToSources(
                source=source,
                operator=operator,
                weight=weights[operator.id]
            )
        )
    await session.commit()

    return SourceResponseModel(
        id=source.id,
        name=source.name,
        operators=[
            OperatorModel(id=operator.id, weight=weights[operator.id])
            for operator in operators
        ]
    )


async def update_source(
        source_model: UpdateSourceModel,
        source: Source = Depends(get_source),
        operators_sources: Sequence[OperatorsToSources] = Depends(get_operators_to_source),
        session: AsyncSession = Depends(get_async_session),
):
    weights = get_operators_weights(source_model.operators)  # Получаем веса операторов

    for items in source_model.model_dump(exclude={"operators"},).items():
        setattr(source, *items)  # Обновляем поля Source

    for operator_source in operators_sources:
        if operator_source.operator_id in weights:
            operator_source.weight = weights.pop(operator_source.operator_id)  # Обновляем веса для существующих записей
        else:
            await session.delete(operator_source)  # Удаляем записи, если их нет в новом списке

    for operator_id, weight in weights.items():  # Добавляем новые записи
        session.add(OperatorsToSources(source=source, operator_id=operator_id, weight=weight))
    await session.commit()

    return SourceResponseModel(
        id=source.id,
        name=source.name,
        operators=[
            OperatorModel(id=operator.id, weight=operator.weight)
            for operator in source_model.operators
        ]
    )

