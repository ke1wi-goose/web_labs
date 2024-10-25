from sqlalchemy.future import select
from uuid import uuid4, UUID
from app.database.models.user import User
from app.database.schemas.user import UserCreate
from app.database.engine import Database_API
from typing import Never
from app.utils.adjust.number import number_adjustment


async def get_user_by_id(user_id: UUID) -> User | None:
    """Retrieve a user by ID."""
    async with Database_API() as async_session:
        result = await async_session.execute(select(User).filter(User.id == user_id))
        return result.scalar_one_or_none()


async def get_users() -> list[User] | list[Never]:
    """Retrieve a list of users with pagination."""
    async with Database_API() as async_session:
        result = await async_session.execute(select(User))
        return result.scalars().all()


async def create_user(user_schema: UserCreate) -> User:
    """Create a new user in the database."""
    async with Database_API() as async_session:
        id_ = uuid4()
        db_user = User(
            id=id_,
            email=user_schema.email,
            password=user_schema.password,
            name=user_schema.name,
            surname=user_schema.surname,
            middlename=user_schema.middlename,
            birthdate=user_schema.birthdate,
            gender=user_schema.gender,
            number=(await number_adjustment(user_schema.number)),
            group=user_schema.group,
        )
        async_session.add(db_user)
        await async_session.commit()
        await async_session.refresh(db_user)
        return db_user
