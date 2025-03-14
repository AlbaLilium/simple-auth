from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from src.auth.model import UserBase
from src.auth.schemas import UserCreate


async def create_user(*, db_session, user: UserCreate):
    user = UserBase(**user.model_dump())
    try:
        db_session.add(user)
        await db_session.commit()
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(status_code=400, detail="This email is busy")
    return user


async def get_user_by_email(*, db_session, email: str):
    executed_query = await db_session.execute(
        select(UserBase).where(UserBase.email == email)
    )
    return executed_query.scalar()
