import bcrypt
from pydantic import SecretStr
from sqlalchemy import LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UserBase(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(LargeBinary, nullable=False)

    def verify_password(self, password: str) -> bool:
        """Verify if provided password matches stored hash"""
        if not password or not self.password:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), self.password)
