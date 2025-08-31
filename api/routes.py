import logging
from typing import Dict

from fastapi import APIRouter
from app.core.third_party_integrations.document_flow.api.profiles import router as profiles_router
from app.core.third_party_integrations.document_flow.api.loops import router as loops_router

logger = logging.getLogger(__name__)
router = APIRouter()

# Aggregate sub-routers
router.include_router(profiles_router)
router.include_router(loops_router)
