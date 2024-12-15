from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from app.db import get_session
from app.resources.deck_manager import DeckManager
from app.schemas.decks import CreateDeck

deck_router = APIRouter()
deck_manager = DeckManager()


@deck_router.post("/create")
async def create_deck(
    deck_data: CreateDeck,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(deck_manager),
):

    deck = manager.get_deck_by_name(name=deck_data.name, session=session)
    if deck:
        return {"message": "Deck with this name already exists"}

    deck = deck_manager.create_deck(deck_data, session)
    return deck

@deck_router.get("/get/{name}")
async def get_deck(name: str, session: Session = Depends(get_session), manager: DeckManager = Depends(deck_manager)):
    deck = manager.get_deck_by_name(name=name, session=session)
    if not deck:
        return {"message": "Deck not found"}
    return deck

@deck_router.get("/get/all")
async def get_all_decks(session: Session = Depends(get_session), manager: DeckManager = Depends(deck_manager)):
    decks = manager.get_all_decks(session)
    return decks

@deck_router.delete("/delete/{name}")
async def delete_deck(name: str, session: Session = Depends(get_session), manager: DeckManager = Depends(deck_manager)):
    deck = manager.get_deck_by_name(name=name, session=session)
    if not deck:
        return {"message": "Deck not found"}
    manager.delete_deck_by_name(name=name, session=session)
    return {"message": "Deck deleted"}
