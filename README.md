# Parostok Monorepo

Monorepo layout:

- `frontend/` React (Vite) client
- `backend/` FastAPI API for catalog, update jobs, and source status
- `data/` SQLite DB and cache artifacts
- `docs/` data integrity and compliance notes

## Run locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Catalog update workflow

1. UI calls `POST /api/catalog/update`.
2. UI polls `GET /api/catalog/update/{job_id}` for logs and status.
3. UI reloads `GET /api/catalog` and source metadata from `GET /api/catalog/sources`.
4. Backend writes fallback snapshot to `frontend/public/catalog_fallback.json`.

## Compliance notes

- Sources include an enabled/disabled flag and reason.
- This starter disables Bayer sources by default until a compliant scraper with robots/ToS checks is configured.
- Manual import endpoint (`POST /api/catalog/manual-import`) can be used when scraping is disallowed.
- No field inference is performed by backend imports; missing values should remain null/unknown.

## Data model

SQLite tables:

- `hybrids`
- `attributes` (with provenance evidence + hash)
- `runs`

## Add a new scraper source

Implement a scraper in `backend/scrapers`, register it in source registry, and ensure parser tests run from fixtures in `backend/tests/fixtures`.

## Implementation Notes

- Bayer UA/US automated parsing is intentionally disabled in this scaffold to avoid non-compliant scraping behavior by default.
- Provenance is represented as attribute-level metadata: `source_url`, `evidence`, `evidence_hash`, and `extracted_at`.
- Frontend clearly labels simulation output as **MODELING ONLY**.
