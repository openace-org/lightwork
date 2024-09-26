"""
The entry point to the server.
"""

import uvicorn

from fastapi import FastAPI
from controllers.generate_controller import router as generate_router

API_VERSION = "/v1"

app = FastAPI()

app.include_router(generate_router, prefix = API_VERSION)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7001, reload=True)
