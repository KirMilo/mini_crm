from fastapi import APIRouter, Depends

from api.api_v1.leads.crud import get_leads_appeals, get_lead_by_id, get_lead_by_email
from api.api_v1.leads.schemas import LeadAppealsModel, LeadModel

router = APIRouter(prefix="/leads", tags=["leads"])


@router.get("/by-id/{lead_id}", response_model=LeadModel)
async def get_by_id(
        lead: LeadModel = Depends(get_lead_by_id),
) -> LeadModel:
    """Получение лида по ID"""
    return lead


@router.post("/get-by-email", response_model=LeadModel)
async def get_by_email(
        lead: LeadModel = Depends(get_lead_by_email),
) -> LeadModel:
    """Получение лида по email"""
    return lead


@router.get("/", response_model=list[LeadAppealsModel])
async def get_leads(
        leads_appeals: list[LeadAppealsModel] = Depends(get_leads_appeals)
) -> list[LeadAppealsModel]:
    print(leads_appeals)
    """Получение списка лидов и их обращений"""
    return leads_appeals
