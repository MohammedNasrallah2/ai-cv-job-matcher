from fastapi import FastAPI

from app.api.router import api_router
from app.config import settings
from app.core.logger import setup_logger

logger = setup_logger()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

app.include_router(api_router)


@app.on_event("startup")
def startup_event() -> None:
    logger.info("Application is starting...")