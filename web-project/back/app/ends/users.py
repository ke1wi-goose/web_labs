from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/users")
async def users() -> JSONResponse:
    return {"message": "USERS"}
