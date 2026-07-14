from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health():
    return {
        "status": "online",
        "app": "Browser Productivity Agent",
        "version": "1.0.0"
    }