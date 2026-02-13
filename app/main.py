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

@app.get("/health")
def health_check():
    return {"status": "ok"}