from fastapi import FastAPI
from app.db import init_db
from app.routers.score_tracker import score_router


def lifespan(app: FastAPI):
    init_db()
    yield


version = "v1"
app = FastAPI(version=version, lifespan=lifespan)

app.include_router(score_router, prefix=f"/{version}", tags=["score"])
