from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.manager import AgentManager

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str
    context: dict


@router.post("/")
def chat(request: ChatRequest):

    agent = AgentManager.route(
        request.context
    )

    return agent.process(
        request.message,
        request.context
    )