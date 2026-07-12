"""AI chat routes."""

from fastapi import APIRouter, HTTPException, status

from models.chat import ChatRequest, ChatResponse
from services.ai_service import get_greeting, process_message

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.get("/greeting", response_model=ChatResponse)
def greeting():
    """Return the assistant's opening message."""
    return get_greeting()


@router.post("/message", response_model=ChatResponse)
def message(request: ChatRequest):
    """Send the conversation to the AI and return its structured reply."""
    if not request.messages:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="messages cannot be empty",
        )

    try:
        return process_message(request.messages)
    except Exception as exc:  # noqa: BLE001 - surface AI errors to the client
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"AI service error: {exc}",
        )
