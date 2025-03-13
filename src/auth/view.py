from fastapi import APIRouter, HTTPException

from src.auth.schemas import UserCreate, UserLogin, UserResponse
from src.auth.service import create_user, get_user_by_email
from src.database import DbSession

auth_router = APIRouter()


@auth_router.post("/login")
async def login(user_in: UserLogin, db_session: DbSession):
    user = await get_user_by_email(db_session=db_session, email=str(user_in.email))
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    if user and user.verify_password(user_in.password):
        return UserResponse(email=user.email)
    else:
        raise HTTPException(status_code=400, detail="Incorrect password")


@auth_router.post("/")
async def registrate_user(user_in: UserCreate, db_session: DbSession):
    user = await get_user_by_email(db_session=db_session, email=str(user_in.email))
    if user:
        raise HTTPException(status_code=400, detail="User with this email exists")

    user = await create_user(db_session=db_session, user=user_in)
    return UserResponse(email=user.email)
