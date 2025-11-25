from typing import Annotated

from fastapi import Body
from pydantic import BaseModel, ConfigDict


class OperatorResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    req_limit: int


class CreateOperatorModel(BaseModel):
    is_active: bool = True
    req_limit: Annotated[
        int,
        Body(
            min_length=1,
            title="Requests limit",
            description="Max requests for current operator",
        )
    ]


class UpdateOperatorModel(BaseModel):
    is_active: bool | None = None
    req_limit: Annotated[
                   int,
                   Body(
                       min_length=1,
                       title="Requests limit",
                       description="Max requests for current operator",
                   )
               ] | None = None
