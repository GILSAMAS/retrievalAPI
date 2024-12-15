from fastapi import FastAPI
from app.db import init_db


def lifespan(app: FastAPI):
    print("Application startup")
    init_db()
    yield


version = "v1"
app = FastAPI(version=version, lifespan=lifespan)
