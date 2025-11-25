from datetime import datetime
from typing import Annotated

from fastapi import Body
from pydantic import BaseModel, ConfigDict


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class LeadModel(CustomBaseModel):
    id: int
    email: str
    created_at: datetime


class AppealModel(CustomBaseModel):
    source_id: int
    operator_id: int
    is_opened: bool
    created_at: datetime


class LeadAppealsModel(CustomBaseModel):
    lead: LeadModel
    appeals: list[AppealModel]


class InputLeadModel(BaseModel):
    email: Annotated[str, Body(min_length=5, title="Leads email")]
