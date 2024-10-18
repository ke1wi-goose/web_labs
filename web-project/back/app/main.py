from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import date
from app.utils.enums.gender import Gender
from app.utils.enums.group import Group
from uuid import uuid4, UUID
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import SessionLocal, engine, Base
import app.db.models
from app.db.crud import create_user, get_user, get_users

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://0.0.0.0",
    "http://0.0.0.0:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.post("/newuser")
def new_user(user: UserCreate, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        uuid = uuid4()
        create_user(
            db=db,
            id=uuid,
            email=user.email,
            password=user.password,
            name=user.name,
            surname=user.surname,
            middlename=user.middlename,
            birthdate=user.birthdate,
            gender=user.gender,
            number=user.number,
            group=user.group,
        )
        return JSONResponse({"message": f"User with id {uuid} has been created."})
    except Exception as e:
        print(e)
        raise HTTPException(status_code=422, detail=str(e))


@app.get("/users", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
