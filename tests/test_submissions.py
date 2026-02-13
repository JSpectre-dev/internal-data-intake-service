"""
Integration tests for the submissions API.

These tests exercise the service end-to-end using FastAPI's TestClient:
- Request validation (Pydantic)
- Persistence (SQLite via SQLAlchemy)
- HTTP status codes and response payload shape

A temporary SQLite database is created per test run by setting INTAKE_DB_PATH to a
temp file path. This keeps tests isolated and repeatable.
"""

# tests/test_submissions.py
# Author: Jordan Casper

import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

@pytest.fixture()
def client(tmp_path: Path):
    """
    Provide a FastAPI TestClient configured to use an isolated temporary database.

    Why this fixture exists:
    - The application reads INTAKE_DB_PATH during import/initialization to decide
      where the SQLite DB file should live.
    - Setting INTAKE_DB_PATH *before* importing the app ensures the app binds to
      the test database, not the default on-disk database.

    Args:
        tmp_path: Built-in pytest fixture providing a unique temporary directory.

    Yields:
        A FastAPI TestClient instance for making HTTP requests to the app.
    """
    
    # Point the app to a temporary DB for test isolation
    os.environ["INTAKE_DB_PATH"] = str(tmp_path / "test.db")
    
    # Import AFTER setting the env var to ensure it picks up the test DB path
    from app.main import app # noqa: E402
    
    with TestClient(app) as c:
        yield c
        
def test_create_and_get_submission(client: TestClient):
    """
    Creating a submission returns an ID, and the same submission can be fetched by ID.

    Verifies:
    - POST /submissions returns 201 and a numeric ID
    - GET /submissions/{id} returns 200 with the same payload and metadata
    """
    
    payload = {"hello": "world", "n": 123}
    r = client.post("/submissions", json={"payload": payload, "source": "test"})
    assert r.status_code == 201
    new_id = r.json()["id"]
    assert isinstance(new_id, int)
    
    r2 = client.get(f"/submissions/{new_id}")
    assert r2.status_code == 200
    body = r2.json()
    assert body["id"] == new_id
    assert body["payload"] == payload
    assert body["source"] == "test"
    assert "created_at" in body