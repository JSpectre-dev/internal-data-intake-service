"""
Internal Data Intake Service.

This module defines the FastAPI application responsible for receiving
and validating internal data submissions.
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

# Initialize database schema
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/submissions", status_code=status.HTTP_201_CREATED, tags=["submissions"])
def create_submission_endpoint(req: SubmissionCreate, db: Session = Depends(get_db)) -> dict:
    new_id = create_submission(db=db, payload=req.payload, source=req.source)
    return {"id": new_id}

@app.get("/submissions/{submission_id}", response_model=SubmissionOut, tags=["submissions"])
def get_submission_endpoint(submission_id: int, db: Session = Depends(get_db)) -> SubmissionOut:
    result = get_submission(db=db, submission_id=submission_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Submission not found")
    return SubmissionOut(**result)