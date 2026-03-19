from fastapi import APIRouter

from app.api.routes.analysis import router as analysis_router
from app.api.routes.final_analysis import router as final_analysis_router
from app.api.routes.health import router as health_router
from app.api.routes.match import router as match_router
from app.api.routes.upload import router as upload_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["Health"])
api_router.include_router(upload_router, tags=["Upload"])
api_router.include_router(analysis_router, tags=["Analysis"])
api_router.include_router(match_router, tags=["Match"])
api_router.include_router(final_analysis_router, tags=["Final Analysis"])