from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Temporary AI endpoint.
    Gemini will be connected later.
    """

    return ChatResponse(
        reply=f"I received: {request.message}"
    )