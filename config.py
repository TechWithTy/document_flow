import os


DOTLOOP_ACCESS_TOKEN = os.getenv("DOTLOOP_ACCESS_TOKEN")
DOTLOOP_BASE_URL = (os.getenv("DOTLOOP_BASE_URL", "https://api-gateway.dotloop.com/public/v2").rstrip("/"))
DOTLOOP_TIMEOUT = float(os.getenv("DOTLOOP_TIMEOUT", "30"))