
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
        
