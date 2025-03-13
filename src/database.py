from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from src.config import settings

SQLALCHEMY_DATABASE_URL = str(settings.DATABASE_URL)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=10,
)
AsyncSession = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
)

Base = declarative_base()
metadata = Base.metadata


async def get_db():
    db = AsyncSession()
    try:
        yield db
    finally:
        await db.close()


DbSession = Annotated[AsyncSession, Depends(get_db)]
