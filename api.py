from fastapi import APIRouter
from endpoint import router as api_router

router = APIRouter()
router.include_router(api_router, prefix='/ver1')
