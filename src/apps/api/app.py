from fastapi import FastAPI

from .test import router as v1_test_router
from .storage import router as storage_router
from src.config.settings import settings


def get_api_app(prefix_api: str = "/api") -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        openapi_url='/openapi.json',
        docs_url='/',
        redoc_url='/redoc'
    )
    app.include_router(v1_test_router, prefix=prefix_api)
    app.include_router(storage_router, prefix=prefix_api)
    return app
