from fastapi import FastAPI
from app.db import init_db

def lifespan(app:FastAPI):
    init_db()
    yield
    print("Application shutting down")

version = "0.0.1"
app = FastAPI(lifespan=lifespan)

