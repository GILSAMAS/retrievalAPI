from fastapi import FastAPI
from app.db import init_db
from app.routers.similarity import similarity
from dotenv import load_dotenv

def lifespan(app:FastAPI):
    init_db()
    yield
    print("Application shutting down")

version = "0.0.1"
load_dotenv()
app = FastAPI(lifespan=lifespan)

app.include_router(similarity)

