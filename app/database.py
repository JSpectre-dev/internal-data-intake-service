
# app/database.py
# Author: Jordan Casper
# File: database.py

from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base


# Default DB path at repo root: ./app.db
DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "app.db"
