"""
Internal Data Intake Service.

This module defines the FastAPI application responsible for receiving
and validating internal data submissions.
"""
# Author: Jordan Casper
# File: main.py

import uvicorn
from fastapi import FastAPI

app = FastAPI(title= "Internal Data Intake Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}