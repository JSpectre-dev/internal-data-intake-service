
# app/submissions_repository.py
# Author: Jordan Casper

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from sqlalchemy.orm import Session
from .models import Submission