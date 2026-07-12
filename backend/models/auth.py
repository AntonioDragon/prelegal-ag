"""Pydantic schemas for authentication."""

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    """New account registration."""

    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class SigninRequest(BaseModel):
    """Sign-in credentials."""

    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Public representation of a user."""

    id: int
    email: EmailStr
    created_at: datetime

    model_config = {"from_attributes": True}
