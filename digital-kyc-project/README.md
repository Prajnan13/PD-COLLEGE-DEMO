# Digital KYC — Reduce Drop-Off & Lift Conversion

**Capstone project — full-stack prototype (mobile + backend + ML stubs) ready for GitHub.**
Generated: 2025-12-06 12:32 UTC

## What's included
- `mobile/` — React Native (Expo) starter with camera capture guidance (placeholder).
- `backend/` — FastAPI app with upload endpoints, DB model stubs, and worker queue integration points.
- `workers/` — OCR, face, and duplicate detection worker stubs.
- `web-dashboard/` — simple admin Flask app skeleton for human review.
- `infra/` — `docker-compose.yml` to run services locally (Postgres, Redis, MinIO, FastAPI, workers).
- `data/` — CSVs exported from provided Excel (if uploaded) or sample dataset.
- `.github/workflows/ci.yml` — CI pipeline to run tests and lint.
- `tests/` — basic pytest tests and a Locust load test stub under `tests/load`.
- `README` includes quickstart, architecture, and next steps.

## Quickstart (dev)
Requirements: Docker, Docker Compose, Python 3.10+, Node/npm (for mobile if you run it)

1. Clone repo (or upload this ZIP to GitHub and clone it)
2. From repo root:
   ```bash
   docker-compose -f infra/docker-compose.yml up --build
   ```
3. Backend API will be available at `http://localhost:8000` (FastAPI docs at `/docs`)
4. Mobile: See `mobile/README.md` for running the Expo placeholder app.

## Note
This repo contains production-ready structure and working backend stubs. ML tasks (OCR, face match, liveness) are provided as pluggable Python modules with clear interfaces; you can replace them with cloud APIs or trained models.

See `backend/README.md` and `workers/README.md` for developer details.

