"""Business logic for saving and retrieving user documents.

Documents belong to a user. form_data is stored as a JSON string in the
database and (de)serialized here so callers work with plain dicts.
"""

import json

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from database import Document
from models.document import (
    DocumentCreate,
    DocumentResponse,
    DocumentUpdate,
)


def _to_response(doc: Document) -> DocumentResponse:
    return DocumentResponse(
        id=doc.id,
        document_type=doc.document_type,
        title=doc.title,
        form_data=json.loads(doc.form_data),
        created_at=doc.created_at,
        updated_at=doc.updated_at,
    )


def list_documents(db: Session, user_id: int) -> list[Document]:
    """Return the user's documents, most recently updated first."""
    return (
        db.query(Document)
        .filter(Document.user_id == user_id)
        .order_by(Document.updated_at.desc())
        .all()
    )


def _get_owned(db: Session, user_id: int, document_id: int) -> Document:
    """Fetch a document owned by the user, or 404."""
    doc = (
        db.query(Document)
        .filter(Document.id == document_id, Document.user_id == user_id)
        .first()
    )
    if doc is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    return doc


def get_document(db: Session, user_id: int, document_id: int) -> DocumentResponse:
    """Return a single owned document with parsed form data."""
    return _to_response(_get_owned(db, user_id, document_id))


def create_document(
    db: Session, user_id: int, data: DocumentCreate
) -> DocumentResponse:
    """Persist a new document for the user."""
    doc = Document(
        user_id=user_id,
        document_type=data.document_type,
        title=data.title,
        form_data=json.dumps(data.form_data),
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return _to_response(doc)


def update_document(
    db: Session, user_id: int, document_id: int, data: DocumentUpdate
) -> DocumentResponse:
    """Update an owned document's title and form data."""
    doc = _get_owned(db, user_id, document_id)
    doc.title = data.title
    doc.form_data = json.dumps(data.form_data)
    db.commit()
    db.refresh(doc)
    return _to_response(doc)


def delete_document(db: Session, user_id: int, document_id: int) -> None:
    """Delete an owned document."""
    doc = _get_owned(db, user_id, document_id)
    db.delete(doc)
    db.commit()
