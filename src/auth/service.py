from sqlalchemy import select

from src.auth.model import UserBase
from src.auth.schemas import UserCreate, UserLogin


async def create_user(*, db_session, user: UserCreate):
    user = UserBase(**user.model_dump())
    db_session.add(user)
    await db_session.flush()
    return user


async def get_user_by_email(*, db_session, email: str):
    query = select(UserBase).where(UserBase.email == email)
    return await db_session.execute(query).scalars().one_or_none()
