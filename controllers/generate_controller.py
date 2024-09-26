"""
Endpoints for making API calls to OpenAI
"""

from fastapi import APIRouter
from lib.types import JsonResponse

router = APIRouter()

@router.get("/")
async def health_check() -> JsonResponse:
    """
    Health check endpoint.
    """
    return JsonResponse(
        error = False,
        message = "Hello, World!",
        data = {
            "some_col": 1,
        }
    )


