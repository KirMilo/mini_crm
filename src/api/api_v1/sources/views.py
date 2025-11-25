from fastapi import APIRouter, Depends

from api.api_v1.sources.crud import create_source, update_source
from api.api_v1.sources.schemas import SourceResponseModel

router = APIRouter(prefix="/source", tags=["sources"])


@router.post("/create", response_model=SourceResponseModel)
async def create_source(
        source: SourceResponseModel = Depends(create_source)
) -> SourceResponseModel:
    """Создание источника (бота)."""
    return source



@router.put("/update/{source_id}", response_model=SourceResponseModel)
async def update_source(
        source: SourceResponseModel = Depends(update_source),
) -> SourceResponseModel:
    """Настройка для источника списка операторов и их весов"""
    return source
