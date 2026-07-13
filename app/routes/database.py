from fastapi import APIRouter
from sqlalchemy import text

from app.database.session import engine

router = APIRouter(
    prefix="/database",
    tags=["Database"]
)


@router.get("/test")
def test_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "Database Connected Successfully ✅"
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }