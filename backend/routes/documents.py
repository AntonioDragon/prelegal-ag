"""Document persistence routes. All endpoints require authentication."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.dependencies import get_current_user
from database import User, get_db
from models.document import (
    DocumentCreate,
    DocumentResponse,
    DocumentSummary,
    DocumentUpdate,
)
from services import document_service

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.get("", response_model=list[DocumentSummary])
def list_documents(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List the current user's saved documents."""
    return document_service.list_documents(db, current_user.id)


@router.post("", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def create_document(
    data: DocumentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Save a new document for the current user."""
    return document_service.create_document(db, current_user.id, data)


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Load one of the current user's documents."""
    return document_service.get_document(db, current_user.id, document_id)


@router.put("/{document_id}", response_model=DocumentResponse)
def update_document(
    document_id: int,
    data: DocumentUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update one of the current user's documents."""
    return document_service.update_document(db, current_user.id, document_id, data)


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete one of the current user's documents."""
    document_service.delete_document(db, current_user.id, document_id)
