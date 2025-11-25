from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from core.db.models import Operator
from core.exceptions.exceptions import OperatorNotFound


async def get_operator(
        operator_id: Annotated[int, Path(title="Operator_id", ge=1)],
        session: AsyncSession = Depends(get_async_session),
) -> Operator:
    operator: Operator | None = await session.get(Operator, operator_id)
    if operator:
        return operator
    raise OperatorNotFound(operator_id)
