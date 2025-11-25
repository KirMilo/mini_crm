from datetime import datetime
from typing import Annotated

from fastapi import Body
from pydantic import BaseModel, ConfigDict


class LeadModel(BaseModel):
    email: Annotated[str, Body(title="Lead's email", min_length=5, max_length=100)]


class AppealResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    lead_id: int
    source_id: int
    operator_id: int | None = None
    is_opened: bool
    created_at: datetime
