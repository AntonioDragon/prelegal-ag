"""AI chat service.

Uses LiteLLM via OpenRouter with Cerebras as the inference provider (per the
project's Cerebras skill) and Structured Outputs so the reply and any extracted
document fields come back as a validated ChatResponse.
"""

import litellm
from litellm import completion

from models.chat import ChatResponse, Message
from models.documents import get_document_catalog_text

MODEL = "openrouter/openai/gpt-oss-120b"
EXTRA_BODY = {"provider": {"order": ["cerebras"]}}

# Some OpenRouter routes reject provider-specific params (e.g. reasoning_effort)
# for certain models. Dropping unsupported params lets the call succeed instead
# of erroring; the param is still sent where the provider accepts it.
litellm.drop_params = True

_CATALOG = get_document_catalog_text()

SYSTEM_PROMPT = f"""You are a friendly legal assistant helping users draft legal agreements.

AVAILABLE DOCUMENT TYPES:
{_CATALOG}

YOUR JOB:
1. Determine which document the user needs through natural conversation.
2. Once the document type is clear, set `documentType` to the exact name from
   the list above and gather the information that document requires.
3. Ask questions conversationally, one or two at a time. ALWAYS end your reply
   with a follow-up question when more information is still needed — never leave
   the user with nothing to answer.
4. Extract concrete values the user gives you into the matching fields (party
   names, dates, terms, fees, etc.). Only fill a field when the user has
   actually provided that information; leave unknown fields null.
5. When every required field for the chosen document has been gathered,
   summarize what you have and set `isComplete` to true.

If the user asks for something outside the available document types, politely
say so and use `suggestedDocument` to recommend the closest available option.

Always put your conversational message in the `response` field."""


def _build_messages(messages: list[Message]) -> list[dict]:
    llm_messages: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in messages:
        llm_messages.append({"role": msg.role, "content": msg.content})
    return llm_messages


def get_greeting() -> ChatResponse:
    """Return the assistant's opening message (no API call needed)."""
    return ChatResponse(
        response=(
            "Hi! I'm your legal drafting assistant. I can help you create "
            "agreements like NDAs, service agreements, and more. What kind of "
            "document would you like to work on today?"
        )
    )


def process_message(messages: list[Message]) -> ChatResponse:
    """Send the conversation to the LLM and return a validated ChatResponse."""
    response = completion(
        model=MODEL,
        messages=_build_messages(messages),
        response_format=ChatResponse,
        reasoning_effort="low",
        extra_body=EXTRA_BODY,
    )

    content = response.choices[0].message.content
    if not content:
        raise ValueError("Empty response from AI service")

    return ChatResponse.model_validate_json(content)
