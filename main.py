"""
The entry point to the server.
"""

from contextlib import asynccontextmanager
import uvicorn

from fastapi import FastAPI
from controllers.generate_controller import router as generate_router

@asynccontextmanager
async def lifespan(api: FastAPI):
    """
    Prefix all endpoints with API version
    """
    api.router.prefix = "/v1"
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(generate_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7001, reload=True)
