from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from app.database.schemas.user import UserCreate, UserResponse
from uuid import UUID
from app.database.api import create_user, get_user_by_id, get_users

router = APIRouter()


@router.post("/newuser")
async def new_user(user: UserCreate) -> JSONResponse:
    try:
        created_user = await create_user(user_schema=user)
        return JSONResponse(
            {"message": f"User with id {created_user.id} has been created."}
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/users", response_model=list[UserResponse])
async def all_users():
    users = await get_users()
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: UUID):
    db_user = await get_user_by_id(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
