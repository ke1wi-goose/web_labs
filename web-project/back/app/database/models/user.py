from datetime import date
from app.database.models.base import Base
from app.utils.enums.group import Group
from app.utils.enums.gender import Gender
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    password: Mapped[str]
    surname: Mapped[str]
    middlename: Mapped[str]
    birthdate: Mapped[date]
    gender: Mapped[Gender]
    number: Mapped[int] = mapped_column(BigInteger)
    group: Mapped[Group]
