__all__ = (
    "appeals_router",
    "leads_router",
    "operators_router",
    "sources_router",
)

from .appeals.views import router as appeals_router
from .leads.views import router as leads_router
from .operators.views import router as operators_router
from .sources.views import router as sources_router
