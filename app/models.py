
# app/models.py
# Author: Jordan Casper

from __future__ import annotations

from sqlalchemy import Column, Integer, Text, DateTime, String, func
from .database import Base

class Submission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    payload_json = Column(Text, nullable=False)
    source = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)