"""
Internal Data Intake Service API.

This module defines the FastAPI application and HTTP endpoints.
It wires request validation (Pydantic) to persistence (SQLAlchemy) via a
request-scoped database session dependency.
"""
# app/main.py
# Author: Jordan Casper

from __future__ import annotations

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from .schemas import SubmissionCreate, SubmissionOut
from .submissions_repository import create_submission, get_submission

app = FastAPI(title= "Internal Data Intake Service")

# Create tables on process startup.
# (In larger systems this is typically handled by migrations.)
Base.metadata.create_all(bind=engine)

def get_db():
    """
    FastAPI dependency that provides a request-scoped SQLAlchemy session.

    Yields:
        A SQLAlchemy Session that is closed after the request completes.
    """
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check() -> dict:
    """
    Health check endpoint used for simple liveness verification.
    """
    
    return {"status": "ok"}

@app.post("/submissions", status_code=status.HTTP_201_CREATED, tags=["submissions"])
def create_submission_endpoint(req: SubmissionCreate, db: Session = Depends(get_db)) -> dict:
    """
    Create a new submission.

    Returns:
        {"id": <new_submission_id>}
    """
    
    new_id = create_submission(db=db, payload=req.payload, source=req.source)
    return {"id": new_id}

@app.get("/submissions/{submission_id}", response_model=SubmissionOut, tags=["submissions"])
def get_submission_endpoint(submission_id: int, db: Session = Depends(get_db)) -> SubmissionOut:
    """
    Retrieve a submission by ID.

    Raises:
        HTTPException(404) if the submission does not exist.
    """
    
    result = get_submission(db=db, submission_id=submission_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Submission not found")
    return SubmissionOut(**result)