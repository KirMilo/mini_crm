from fastapi import APIRouter, Depends

from api.api_v1.operators.schemas import OperatorResponseModel
from api.api_v1.operators.crud import create_operator, update_operator, get_operators

router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("/create", response_model=OperatorResponseModel)
async def post_create_operator(
        operator: OperatorResponseModel = Depends(create_operator)
) -> OperatorResponseModel:
    """Создание оператора."""
    return operator


@router.patch("/update/{operator_id}", response_model=OperatorResponseModel)
async def update_operator(
        operator: OperatorResponseModel = Depends(update_operator)
) -> OperatorResponseModel:
    """Управление лимитом нагрузки и активностью оператора."""
    return operator


@router.get("/", response_model=list[OperatorResponseModel])
async def get_operators(
        operators: list[OperatorResponseModel] = Depends(get_operators)
):
    """Просмотр списка операторов."""
    return operators


