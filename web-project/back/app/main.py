from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.user import router


app = FastAPI()
app.include_router(router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://0.0.0.0",
    "http://0.0.0.0:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
