
# app/schemas.py
# Author: Jordan Casper

from __future__ import annotations

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class SubmissionCreate(BaseModel):
    payload: Dict[str, Any] = Field(..., description ="Arbitrary JSON object to store")
    source: Optional[str] = None