
# app/database.py
# Author: Jordan Casper
# File: database.py

from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Default DB path at repo root: ./app.db
DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "app.db"

def _db_url() -> str:
   # Allow override for tests / different environments
   db_path = os.getenv("INTAKE_DB_PATH")
   if db_path:
       p = Path(db_path).expanduser().resolve()
   else:
       p = DEFAULT_DB_PATH
   return f"sqlite:///{p}"

engine = create_engine(
    _db_url(),
    connect_args={"check_same_thread": False}  # needed for SQLite + FastAPI/TestClient
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()