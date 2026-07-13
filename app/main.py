from fastapi import FastAPI

from app.config import settings
from app.routes.health import router as health_router
from app.routes.database import router as database_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Powered Multi-Agent Browser Assistant"
)

app.include_router(health_router)
app.include_router(database_router)