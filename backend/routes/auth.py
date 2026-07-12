"""Authentication routes: signup, signin, signout, and current user."""

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from core.dependencies import get_current_user
from core.security import (
    ACCESS_TOKEN_EXPIRE_DAYS,
    AUTH_COOKIE_NAME,
    create_access_token,
)
from database import User, get_db
from models.auth import SigninRequest, SignupRequest, UserResponse
from services.auth_service import authenticate_user, create_user

router = APIRouter(prefix="/api/auth", tags=["auth"])

_COOKIE_MAX_AGE = ACCESS_TOKEN_EXPIRE_DAYS * 24 * 60 * 60


def _set_auth_cookie(response: Response, user: User) -> None:
    """Attach the JWT as an HttpOnly cookie."""
    token = create_access_token(user.id, user.email)
    response.set_cookie(
        key=AUTH_COOKIE_NAME,
        value=token,
        max_age=_COOKIE_MAX_AGE,
        httponly=True,
        samesite="lax",
        secure=False,  # served over http on localhost; set True behind TLS
        path="/",
    )


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(data: SignupRequest, response: Response, db: Session = Depends(get_db)):
    """Create an account and sign the user in."""
    user = create_user(db, data)
    _set_auth_cookie(response, user)
    return user


@router.post("/signin", response_model=UserResponse)
def signin(data: SigninRequest, response: Response, db: Session = Depends(get_db)):
    """Sign in with email and password."""
    user = authenticate_user(db, data)
    _set_auth_cookie(response, user)
    return user


@router.post("/signout")
def signout(response: Response):
    """Clear the auth cookie."""
    response.delete_cookie(key=AUTH_COOKIE_NAME, path="/")
    return {"status": "signed out"}


@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)):
    """Return the currently authenticated user."""
    return current_user
