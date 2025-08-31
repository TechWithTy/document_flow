# Document Flow (Dotloop Public API v2)

Modular SDK and FastAPI routes to proxy Dotloop endpoints via our backend.

## Environment Variables

- DOTLOOP_ACCESS_TOKEN (required for real API calls)
- DOTLOOP_BASE_URL (default: https://api-gateway.dotloop.com/public/v2)
- DOTLOOP_TIMEOUT (default: 30)

Example .env:
DOTLOOP_ACCESS_TOKEN=your_token_here
DOTLOOP_BASE_URL=https://api-gateway.dotloop.com/public/v2
DOTLOOP_TIMEOUT=30

## Endpoints

- GET /dotloop/health
  - Returns: { healthy, base_url, has_token }

- GET /dotloop/profiles
  - Query: page (default 1), page_size (default 50)
  - Proxies: GET {DOTLOOP_BASE_URL}/profiles

- GET /dotloop/profiles/{profile_id}/loops
  - Query: page (default 1), page_size (default 50)
  - Proxies: GET {DOTLOOP_BASE_URL}/profiles/{profileId}/loops

Examples:
curl "http://localhost:8000/dotloop/health"

curl "http://localhost:8000/dotloop/profiles?page=1&page_size=50"

curl "http://localhost:8000/dotloop/profiles/123456/loops?page=1&page_size=50"

## Internal Structure

- client.py: DotloopClient builds URLs using base, adds Bearer token header if present.
- api/profiles.py: Routes (`/dotloop/health`, `/dotloop/profiles`).
- api/loops.py: Route (`/dotloop/profiles/{profile_id}/loops`).
- api/_base.py: DotloopAPIBase with shared requests session, base URL, timeout.
- api/_requests.py: ListParams, ListLoopsParams.
- api/_enums.py, api/_responses.py: helpers.
- api/routes.py: Aggregates dotloop sub-routers without extra prefix.