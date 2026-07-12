"""Shared FastAPI dependencies for authentication."""

from typing import Optional

from fastapi import Cookie, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.security import AUTH_COOKIE_NAME, decode_access_token
from database import User, get_db


def get_current_user(
    prelegal_token: Optional[str] = Cookie(default=None, alias=AUTH_COOKIE_NAME),
    db: Session = Depends(get_db),
) -> User:
    """Resolve the authenticated user from the JWT cookie, or 401."""
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
    )

    if not prelegal_token:
        raise credentials_error

    payload = decode_access_token(prelegal_token)
    if not payload or "sub" not in payload:
        raise credentials_error

    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if user is None:
        raise credentials_error

    return user
