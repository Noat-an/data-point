from fastapi import APIRouter

from .v1.routes import router as test_router


router = APIRouter(prefix="/test")
router.include_router(test_router, tags=["Test"])
