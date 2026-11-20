# Auto Shop — Australian used-car intelligence platform

A custom Next.js frontend plus FastAPI/PostgreSQL backend starter. The included experience is a polished, responsive prototype using clearly labelled demo listings. The API scaffold is ready for authorised marketplace feeds and valuation data.

## Stack
- Web: Next.js App Router, React, TypeScript, Tailwind CSS
- API: FastAPI, SQLAlchemy 2, Pydantic
- Database: PostgreSQL
- Local development: Docker Compose

## Run the frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:3000.

## Run the API
```bash
cd backend
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
API docs: http://localhost:8000/docs

## Run PostgreSQL
From the project root:
```bash
docker compose up -d db
```
Set `DATABASE_URL` in `backend/.env` (see `.env.example`).

## Important production work
The demo data is not live marketplace inventory and price estimates are illustrative. Before launch:
1. Obtain permitted API/feed access or commercial agreements for each listing source.
2. Implement source-specific ingestion adapters and respect provider terms, rate limits and robots/access policies.
3. Validate valuations against Australian transaction/listing data; disclose methodology and uncertainty.
4. Add authentication, verified email, password reset, rate limiting, audit logs and account deletion.
5. Add billing only after subscription plans, consumer terms, privacy policy and Australian legal review are settled.
6. Configure monitoring, backups, secrets management, CI/CD and security testing.

No marketplace scraping, access bypass, or fabricated live availability is included.
