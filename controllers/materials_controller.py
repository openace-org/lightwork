"""
Endpoints for making API calls to OpenAI
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from lib.ratelimit import limiter

router = APIRouter()

@router.get("/")
@limiter.limit("5/minute")
async def health_check(request: Request) -> JSONResponse:
    """
    Health check endpoint.
    """
    return JSONResponse(content={
            "message": "Hello, World!",
            "data": {}
        }, status_code=status.HTTP_200_OK)
