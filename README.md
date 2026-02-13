# Internal Data Intake Service

![Python](https://img.shields.io/badge/python-3.11.5-3776AB?logo=python&logoColor=white)

## Overview

This repository contains a minimal, structured implementation of an internal data intake service built with FastAPI and SQLAlchemy, using SQLite as the backing database.

It implements:

- Clean project structure
- RESTful API design
- Request validation using Pydantic
- Relational persistence using SQLAlchemy
- Clear separation between API, domain models, and data access logic
- Basic integration testing using pytest

The current scope is intentionally limited to a focused, reviewable vertical slice of a backend service.

---

## Architecture

```text
HTTP (FastAPI)
    ↓
Schemas (Pydantic)
    ↓
Repository Layer
    ↓
SQLAlchemy ORM
    ↓
SQLite
```

The repository layer isolates database access from HTTP handling to maintain separation of concerns and testability.

---

## Project Structure

```text
app/
    main.py # FastAPI application entrypoint
    database.py # Engine and session configuration
    models.py # SQLAlchemy ORM models
    schemas.py # Pydantic request/response models
    submissions_repository.py # Data access layer

tests/
    test_submissions.py # API integration tests
```

---

## API Endpoints

The following endpoints are implemented in app/main.py.

---

### GET `/health`

Health check endpoint.

Example request:

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

---

### POST `/submissions`

Creates a new submission record.

Example request body:

```json
{
  "payload": { "hello": "world", "n": 123 },
  "source": "manual"
}
```

Example response:

```json
{
  "id": 1
}
```

---

### GET `/submissions/{id}`

Retrieves a submission by ID.

Example request:

```http
GET /submissions/1
```

Example response:

```json
{
  "id": 1,
  "payload": { "hello": "world", "n": 123 },
  "source": "manual",
  "created_at": "2024-01-01T12:00:00"
}
```

---

## Running Locally

### 1. Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Start the server

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to use the interactive Swagger UI.

---

## Example Usage

The following examples assume the service is running at:

```text
http://127.0.0.1:8000
```

> Note: Output formatting may vary depending on the HTTP client.
> Some clients (e.g., curl) display raw JSON, while others (e.g., PowerShell `Invoke-RestMethod`) automatically parse and format the response.

---

### Using curl (Linux / macOS / Git Bash)

Create submission:

```bash
curl -X POST http://127.0.0.1:8000/submissions \
  -H "Content-Type: application/json" \
  -d '{"payload":{"hello":"world","n":123},"source":"manual"}'
```

Fetch submission:

```bash
curl http://127.0.0.1:8000/submissions/1
```

---

### Using PowerShell (Windows-native)

Create submission:

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8000/submissions" `
  -ContentType "application/json" `
  -Body '{"payload":{"hello":"world","n":123},"source":"manual"}'
```

Fetch submission:

```powershell
Invoke-RestMethod `
  -Method Get `
  -Uri "http://127.0.0.1:8000/submissions/1"
```

---

## Testing

Run integration tests:

```bash
pytest -q
```

Tests use a temporary SQLite database via the INTAKE_DB_PATH environment variable to ensure isolation.

## Design Considerations

- Database configuration is environment-driven (via INTAKE_DB_PATH).

- Repository layer isolates persistence logic

- ORM models define relational schema explicitly

- API contracts are defined with Pydantic schemas
  
- Tables are initialized on startup for simplicity (migration tooling would be used in larger systems)