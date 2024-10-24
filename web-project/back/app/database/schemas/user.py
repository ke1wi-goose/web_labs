from pydantic import BaseModel, ConfigDict
from datetime import date
from app.utils.enums.gender import Gender
from app.utils.enums.group import Group
from uuid import UUID


class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: str
    password: str
    name: str
    surname: str
    middlename: str
    birthdate: date
    gender: Gender
    number: int
    group: Group


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: str
    name: str
    surname: str
    middlename: str
    birthdate: date
    gender: Gender
    number: int
    group: Group
