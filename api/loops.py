import logging
from typing import Dict

from fastapi import APIRouter

from app.core.third_party_integrations.document_flow.client import DotloopClient

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/dotloop", tags=["document_flow-loops"])


# Utility

def list_loops_util(profile_id: str, page: int, page_size: int) -> Dict:
    client = DotloopClient()
    return client.list_loops(profile_id=profile_id, page=page, page_size=page_size)


# Routes
@router.get("/profiles/{profile_id}/loops")
async def list_loops(profile_id: str, page: int = 1, page_size: int = 50) -> Dict:
    return list_loops_util(profile_id=profile_id, page=page, page_size=page_size)
