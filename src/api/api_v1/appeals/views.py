from fastapi import APIRouter, Depends

from api.api_v1.appeals.schemas import AppealResponseModel
from api.api_v1.appeals.crud import create_appeal

router = APIRouter(prefix="/appeal", tags=["appeals"])


@router.post("/{source_id}/create", response_model=AppealResponseModel)
async def create_appeal(
        appeal: AppealResponseModel = Depends(create_appeal)
) -> AppealResponseModel:
    """Создание обращения лида"""
    return appeal
