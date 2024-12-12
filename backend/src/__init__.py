from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.api.db.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


version = "v1"
app = FastAPI(
    title="Retrieval evaluator",
    version=version,
    description="This is a simple API that retrieves data from a database",
    lifespan=lifespan,
)
