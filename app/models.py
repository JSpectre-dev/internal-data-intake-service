"""
ORM models for persistence.

Models in this module define the relational schema stored in SQLite via SQLAlchemy.
"""

# app/models.py
# Author: Jordan Casper

from __future__ import annotations

from sqlalchemy import Column, Integer, Text, DateTime, String, func
from .database import Base

class Submission(Base):
    """
    A stored submission.

    Stores the original request payload as a JSON string for flexibility.
    This keeps the initial scope small while preserving the full submission data.
    """
    
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    payload_json = Column(Text, nullable=False)
    source = Column(String, nullable=True)
    
    # Server-generated timestamp (SQLite: CURRENT_TIMESTAMP via SQLAlchemy func.now()).
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)