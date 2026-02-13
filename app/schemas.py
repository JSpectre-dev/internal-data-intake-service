"""
Pydantic schemas for request and response validation.

These schemas define the public API contract for the service.
"""

# app/schemas.py
# Author: Jordan Casper

from __future__ import annotations

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class SubmissionCreate(BaseModel):
    """
    Request body for creating a submission.

    payload:
        Arbitrary JSON object submitted to the intake service. Kept generic to support
        multiple internal producers without changing the API contract.
    source:
        Optional label describing the originating system/client.
    """
    
    payload: Dict[str, Any] = Field(..., description ="Arbitrary JSON object to store")
    source: Optional[str] = None
    
class SubmissionOut(BaseModel):
    """
    Response model returned by the API when a submission is retrieved.
    """
    
    id: int 
    payload: Dict[str, Any]
    source: Optional[str] = None
    created_at: str