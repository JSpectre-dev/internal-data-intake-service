# Internal Data Intake Service

![Python](https://img.shields.io/badge/python-3.11.5-3776AB?logo=python&logoColor=white)

## Overview

This repository contains a minimal, structured implementation of an internal data intake service built with FastAPI and SQLAlchemy, using SQLite as the backing database.

It implements:

- Clean project structure
- RESTful API endpoints
- Request validation using Pydantic
- Relational persistence using SQLAlchemy
- Clear separation between API, domain models, and data access logic

The current scope is intentionally limited to a focused, reviewable vertical slice of a backend service, with clear extension points for future enhancements.

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
    test_submissions.py # Basic API tests
```

---

## Current Features

- SQLite database configuration
- SQLAlchemy ORM model definitions
- Environment-based database configuration
- FastAPI application initialization

Endpoints are being implemented incrementally.

---

## Running Locally

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```
Install dependencies and run the application:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Testing
```bash
pytest -q
```

## Design Notes

* Database configuration is environment-driven (via INTAKE_DB_PATH).

* SQLite is used for simplicity and portability.

* The structure is intentionally modular to support future extensions.