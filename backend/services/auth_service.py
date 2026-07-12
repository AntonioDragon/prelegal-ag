"""Business logic for user signup and signin."""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from database import User
from models.auth import SigninRequest, SignupRequest


def create_user(db: Session, data: SignupRequest) -> User:
    """Register a new user, or 409 if the email is already taken."""
    existing = db.query(User).filter(User.email == data.email).first()
    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists",
        )

    user = User(
        email=data.email,
        hashed_password=get_password_hash(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, data: SigninRequest) -> User:
    """Verify credentials and return the user, or 401."""
    user = db.query(User).filter(User.email == data.email).first()
    if user is None or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    return user
