from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlmodel import Session
from app.db import get_session
from app.models.models import Deck
from app.resources.deck_manager import DeckManager
from app.schemas.decks import CreateDeck
from typing import List
from typing import Dict
import uuid

deck_router = APIRouter()


@deck_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Deck)
async def create_deck(
    deck_data: CreateDeck,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
):

    deck = manager.get_deck_by_name(name=deck_data.name, session=session)
    if deck:
        raise HTTPException(status_code=400, detail="Deck already exists")

    deck = manager.create_deck(deck_data, session)
    return deck


@deck_router.put(
    "/update/{deck_id}", status_code=status.HTTP_200_OK, response_model=Deck
)
async def update_deck(
    deck_id: uuid.UUID,
    deck_data: CreateDeck,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
):
    deck = manager.get_deck_by_id(deck_id=deck_id, session=session)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    
    if deck_data.name != deck.name:
        deck = manager.get_deck_by_name(name=deck_data.name, session=session)
        if deck:
            raise HTTPException(status_code=400, detail=f"Deck with the name: '{deck_data.name}' already exists")

    updated_deck = manager.update_deck(deck=deck, deck_data=deck_data, session=session)

    return updated_deck


@deck_router.get("/get/{name}", status_code=status.HTTP_200_OK, response_model=Deck)
async def get_deck(
    name: str,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
):
    deck = manager.get_deck_by_name(name=name, session=session)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck


@deck_router.get("/list", status_code=status.HTTP_200_OK, response_model=List[Deck])
async def get_all_decks(
    session: Session = Depends(get_session), manager: DeckManager = Depends(DeckManager)
):
    decks = manager.get_all_decks(session)
    return decks


@deck_router.delete(
    "/delete/{name}", status_code=status.HTTP_200_OK, response_model=Dict[str, str]
)
async def delete_deck(
    name: str,
    session: Session = Depends(get_session),
    manager: DeckManager = Depends(DeckManager),
):
    deck = manager.get_deck_by_name(name=name, session=session)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    manager.delete_deck_by_name(name=name, session=session)
    return {"message": "Deck deleted"}
