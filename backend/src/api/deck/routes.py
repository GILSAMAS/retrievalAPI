from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from src.api.db.db import get_session
from src.api.deck.manager import DeckManager
from src.api.deck.schemas import CreateDeck
from src.api.db.models.decks import Deck

deck_router = APIRouter(tags=["Deck"])


# create a deck
@deck_router.post("/create")
async def create_deck(
    deck_data: CreateDeck,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
) -> Deck:
    new_deck = manager.create_deck(deck_data, session)
    return new_deck


# get a deck
@deck_router.get("/get/{deck_id}")
async def get_deck(
    deck_id: str,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
) -> Deck:
    deck = manager.get_deck(deck_id, session)
    return deck


# delete a deck
@deck_router.delete("/delete/{deck_id}")
async def delete_deck(
    deck_id: str,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
):
    deck = manager.get_deck(deck_id, session)
    if not deck:
        return {"message": "Deck not found"}
    manager.delete_deck(deck_id, session)
    return {"message": "Deck deleted"}
