
# tests/test_submissions.py
# Author: Jordan Casper

import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

@pytest.fixture()
def client(tmp_path: Path):
    
    # Point the app to a temporary DB for test isolation
    os.environ["INTAKE_DB_PATH"] = str(tmp_path / "test.db")
    
    from app.main import app # Import AFTER setting the env var to ensure it picks up the test DB path
    
    with TestClient(app) as c:
        yield c
        
def test_create_and_get_submission(client: TestClient):
    
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