from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import init_db
from app.routers.decks import deck_router
from app.routers.cards import card_router

def lifespan(app: FastAPI):
    print("Application startup")
    init_db()
    yield


version = "v1"
app = FastAPI(version=version, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(deck_router, prefix=f"/{version}/deck", tags=["Deck"])
app.include_router(card_router, prefix=f"/{version}/card", tags=["Card"])
