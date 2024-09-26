"""
Type definitions
"""

from typing import Any
from pydantic import BaseModel

class JsonResponse(BaseModel):
    """
    Standardized response payload structure
    """
    error: bool
    message: str
    data: Any
