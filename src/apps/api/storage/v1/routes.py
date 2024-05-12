from fastapi import APIRouter

from .storage.routes import router as storage_router
from .owner.routes import router as owner_router


router = APIRouter(prefix="/v1")
router.include_router(storage_router, tags=["Storage"])
router.include_router(owner_router, tags=["Owner"])
