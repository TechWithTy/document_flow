import os
from typing import Dict, Optional

import requests
from app.core.third_party_integrations.document_flow import config


class DotloopClient:
    """
    Skeleton client for Dotloop Public API v2.
    Docs: https://dotloop.github.io/public-api/#authentication

    Configure an access token (OAuth2 or provided token) via DOTLOOP_ACCESS_TOKEN.
    Implement endpoints (profiles, loops, documents, contacts) as needed.
    """

    def __init__(self, access_token: Optional[str] = None, base_url: Optional[str] = None, timeout: Optional[int] = None):
        self.access_token = access_token or os.getenv("DOTLOOP_ACCESS_TOKEN") or getattr(config, "DOTLOOP_ACCESS_TOKEN", None)
        resolved_base = base_url or os.getenv("DOTLOOP_BASE_URL") or getattr(config, "DOTLOOP_BASE_URL", "https://api-gateway.dotloop.com/public/v2")
        self.base_url = (resolved_base or "https://api-gateway.dotloop.com/public/v2").rstrip("/")
        self.timeout = int(timeout if timeout is not None else getattr(config, "DOTLOOP_TIMEOUT", 30))

    def health(self) -> bool:
        # Token generally required for real calls
        return bool(self.access_token)

    def _headers(self) -> Dict[str, str]:
        return {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}" if self.access_token else "",
        }

    def list_profiles(self, *, page: int = 1, page_size: int = 50) -> Dict:
        """
        GET {base}/profiles
        Docs: https://dotloop.github.io/public-api/#tag/Profiles
        """
        url = f"{self.base_url}/profiles"
        params = {"page": page, "pageSize": page_size}
        resp = requests.get(url, headers=self._headers(), params=params, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def list_loops(self, *, profile_id: str, page: int = 1, page_size: int = 50) -> Dict:
        """
        GET {base}/profiles/{profileId}/loops
        Docs: https://dotloop.github.io/public-api/#tag/Loops
        """
        url = f"{self.base_url}/profiles/{profile_id}/loops"
        params = {"page": page, "pageSize": page_size}
        resp = requests.get(url, headers=self._headers(), params=params, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()