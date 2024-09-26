"""
The entry point to the server.
"""

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from controllers.materials_controller import router as generate_router
from lib.ratelimit import limiter

API_VERSION = "/v1"

app = FastAPI()

# Exception handlers
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "message": "Rate limit exceeded: 5 per 1 minute",
            "data": {}
        }
    )

# Rate limit middleware
app.state.limiter = limiter

# Compression middleware
app.add_middleware(GZipMiddleware)

app.include_router(generate_router, prefix = API_VERSION)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7001, reload=True)
