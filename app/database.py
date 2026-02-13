"""
Database configuration for the service.

This module defines:
- the SQLAlchemy Engine (connection to SQLite),
- the session factory (SessionLocal),
- the declarative Base class used by ORM models.

Design:
- SQLite is used for portability and minimal setup.
- The DB file path can be overridden via INTAKE_DB_PATH to support tests and 
  environment-specific configuration without hardcoding values.
"""
# app/database.py
# Author: Jordan Casper

from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Default DB path at repo root: ./app.db
DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "app.db"

def _db_url() -> str:
    """
    Build the SQLAlchemy database URL.

    Uses INTAKE_DB_PATH if set, otherwise falls back to DEFAULT_DB_PATH.

    Returns:
        A SQLAlchemy SQLite URL string in the form: sqlite:////absolute/path/to/db
    """

    db_path = os.getenv("INTAKE_DB_PATH")
    path = Path(db_path).expanduser().resolve() if db_path else DEFAULT_DB_PATH
    return f"sqlite:///{path}"

engine = create_engine(
    _db_url(),
    connect_args={"check_same_thread": False},  # needed for SQLite + FastAPI/TestClient
)

# Session factory used by request-scoped dependencies.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models.
Base = declarative_base()