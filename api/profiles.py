import logging
from typing import Dict

from fastapi import APIRouter

from app.core.third_party_integrations.document_flow.client import DotloopClient

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/dotloop", tags=["document_flow-profiles"])


# Utility

def list_profiles_util(page: int, page_size: int) -> Dict:
    client = DotloopClient()
    return client.list_profiles(page=page, page_size=page_size)


# Routes
@router.get("/health")
async def health() -> Dict:
    client = DotloopClient()
    return {
        "healthy": client.health(),
        "base_url": client.base_url,
        "has_token": bool(client.access_token),
    }

@router.get("/profiles")
async def list_profiles(page: int = 1, page_size: int = 50) -> Dict:
    return list_profiles_util(page=page, page_size=page_size)
