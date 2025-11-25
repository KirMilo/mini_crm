from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict


class OperatorModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int, Field(ge=1)]
    weight: Annotated[int, Field(ge=1)]


class SourceResponseModel(BaseModel):
    id: int
    name: str
    operators: list[OperatorModel]


class CreateSourceModel(BaseModel):
    name: str
    operators: list[OperatorModel] | None = None


class UpdateSourceModel(BaseModel):
    name: str
    operators: list[OperatorModel]
