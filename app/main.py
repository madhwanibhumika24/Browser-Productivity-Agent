from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database.db import Base, engine

from app.routes.auth import router as auth_router
from app.routes.health import router as health_router
from app.routes.chat import router as chat_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Browser Productivity Agent API",
        "status": "running",
        "version": settings.APP_VERSION,
    }


app.include_router(auth_router)
app.include_router(health_router)
app.include_router(chat_router)