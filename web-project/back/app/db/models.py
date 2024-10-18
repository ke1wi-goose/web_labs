from sqlalchemy import Column, Integer, String, Date, Enum, UUID
from app.db.database import Base
from app.utils.enums.group import Group
from app.utils.enums.gender import Gender


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    password = Column(String)
    surname = Column(String)
    middlename = Column(String)
    birthdate = Column(Date)
    gender = Column(Enum(Gender))
    number = Column(Integer)
    group = Column(Enum(Group))
