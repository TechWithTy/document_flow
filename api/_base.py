import requests
from requests import Session

from app.core.third_party_integrations.document_flow import config


class DotloopAPIBase:
    """
    Lightweight base for Dotloop API requests.
    Uses DOTLOOP_BASE_URL and DOTLOOP_TIMEOUT from config.
    """

    def __init__(self):
        self.session: Session = requests.Session()
        self.base_url: str = getattr(config, "DOTLOOP_BASE_URL", "https://api-gateway.dotloop.com/public/v2").rstrip("/")
        self.timeout: int = int(getattr(config, "DOTLOOP_TIMEOUT", 30))

    def get(self, path: str, *, params: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params or {}, headers=headers or {}, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()