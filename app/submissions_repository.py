"""
Data access layer for submissions.

This module isolates persistence logic from the API layer:
- API layer handles HTTP and dependency injection
- Repository layer handles database reads/writes

This separation keeps the code testable and maintainable as the project grows.
"""

# app/submissions_repository.py
# Author: Jordan Casper

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from sqlalchemy.orm import Session
from .models import Submission

def create_submission(db: Session, payload: Dict[str, Any], source: Optional[str]) -> int:
    """
    Persist a new submission row.

    Args:
        db: An active SQLAlchemy Session.
        payload: Arbitrary JSON object to store.
        source: Optional origin label.

    Returns:
        The newly created submission ID.
    """
    payload_json = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)

    row = Submission(payload_json=payload_json, source=source)
    db.add(row)
    db.commit()
    db.refresh(row)
    
    return int(row.id) 

def get_submission(db: Session, submission_id: int) -> Optional[dict]:
    """
    Fetch a submission by ID.

    Args:
        db: An active SQLAlchemy Session.
        submission_id: Primary key of the submission.

    Returns:
        A dict shaped for SubmissionOut, or None if not found.
    """
    
    row = db.query(Submission).filter(Submission.id == submission_id).first()
    if row is None:
        return None
    
    return {
        "id": int(row.id),
        "payload": json.loads(row.payload_json),
        "source": row.source,
        "created_at": row.created_at.isoformat(),
    }