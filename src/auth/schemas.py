from pydantic import BaseModel, EmailStr, field_validator

from src.auth.utils import hash_password


class UserBase(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email")
    def email_required(cls, v):
        if not v:
            raise ValueError("Must not be empty string and must be a email")
        return v


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def hash(cls, v):
        password = v
        return hash_password(password)


class UserLogin(UserBase):
    email: EmailStr
    password: str

    @field_validator("password")
    def password_required(cls, v):
        if not v:
            raise ValueError("Must not be empty string")
        return v


class UserResponse(BaseModel):
    email: EmailStr
