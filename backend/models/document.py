"""Pydantic schemas for saved documents."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    """Payload to save a new document."""

    document_type: str = Field(min_length=1)
    title: str = Field(min_length=1, max_length=200)
    form_data: dict[str, Any]


class DocumentUpdate(BaseModel):
    """Payload to update an existing document."""

    title: str = Field(min_length=1, max_length=200)
    form_data: dict[str, Any]


class DocumentSummary(BaseModel):
    """Lightweight document representation for list views (no form_data)."""

    id: int
    document_type: str
    title: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class DocumentResponse(BaseModel):
    """Full document representation including the parsed form data."""

    id: int
    document_type: str
    title: str
    form_data: dict[str, Any]
    created_at: datetime
    updated_at: datetime
