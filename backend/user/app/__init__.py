from fastapi import FastAPI
from app.db import init_db
from app.routers.user import user_router


def lifespan(app: FastAPI):
    init_db()
    yield


version = "v1"
app = FastAPI(lifespan=lifespan, version=version)

app.include_router(user_router, prefix=f"/{version}/user", tags=["User"])
