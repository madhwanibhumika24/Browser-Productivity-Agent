from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_service import GeminiService

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

    reply = GeminiService.chat(
        request.message
    )

    return ChatResponse(
        reply=reply
    )