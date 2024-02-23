import fastapi

from .test import router as v1_router


def get_api_app(prefix_api: str = "/api") -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    app.include_router(v1_router, prefix=prefix_api)
    return app
