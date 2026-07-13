from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)


@router.get("/")
def health_check():
    """
    Health Check Endpoint
    """

    return {
        "status": "success",
        "application": "Browser Productivity Agent",
        "version": "1.0.0",
        "message": "Backend is running successfully 🚀"
    }