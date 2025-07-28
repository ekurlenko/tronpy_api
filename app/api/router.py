from fastapi import APIRouter

from .tron.router import router as tron_router

router = APIRouter(prefix="/api")
router.include_router(tron_router)
