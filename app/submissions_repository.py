
# app/submissions_repository.py
# Author: Jordan Casper

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from sqlalchemy.orm import Session
from .models import Submission

def create_submission(db: Session, payload: Dict[str, Any], source: Optional[str]) -> int:
    row = Submission(payload_json=json.dumps(payload, separators=(',', ','), ensure_ascii=False), source=source)
    db.add(row)
    db.commit()
    db.refresh(row)
    return int(row.id) 

def get_submission(db: Session, submission_id: int) -> Optional[dict]:
    row = db.query(Submission).filter(Submission.id == submission_id).first()
    if row is None:
        return None
    return {
        "id": int(row.id),
        "payload": json.loads(row.payload_json),
        "source": row.source,
        "created at": row.created_at.isoformat(),
    }