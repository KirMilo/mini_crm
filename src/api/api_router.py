from fastapi import APIRouter
from .api_v1 import appeals_router, leads_router, operators_router, sources_router

router_v1 = APIRouter(prefix="/api/v1")
router_v1.include_router(appeals_router)
router_v1.include_router(leads_router)
router_v1.include_router(operators_router)
router_v1.include_router(sources_router)
