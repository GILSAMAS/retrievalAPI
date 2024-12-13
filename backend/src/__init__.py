from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.deck.routes import deck_router
from src.api.db.db import init_db
from src.api.card.routes import card_router
from src.api.session.routes import session_router
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


app.include_router(deck_router, prefix=f"/api/{version}/decks")
app.include_router(card_router, prefix=f"/api/{version}/cards")
app.include_router(session_router, prefix=f"/api/{version}/session")