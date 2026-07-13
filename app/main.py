from fastapi import FastAPI

from app.config import settings
from app.database.db import create_tables

from app.routes.health import router as health_router
from app.routes.database import router as database_router
from app.routes.auth import router as auth_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Powered Multi-Agent Browser Assistant",
)


@app.on_event("startup")
def startup():
    """
    Create all database tables when the application starts.
    """
    create_tables()


# Register API Routes
app.include_router(health_router)
app.include_router(database_router)
app.include_router(auth_router)