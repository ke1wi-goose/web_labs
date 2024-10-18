from sqlalchemy.orm import Session
from app.db.models import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(
    db: Session,
    id,
    email,
    password,
    name,
    surname,
    middlename,
    birthdate,
    gender,
    number,
    group,
):
    db_user = User(
        id=id,
        email=email,
        password=password,
        name=name,
        surname=surname,
        middlename=middlename,
        birthdate=birthdate,
        gender=gender,
        number=number,
        group=group,
    )
    db.add(db_user)
    db.commit()
