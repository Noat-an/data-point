from fastapi import APIRouter

from .v1.routes import router as storage_router


router = APIRouter(prefix="/storage")
router.include_router(storage_router)
