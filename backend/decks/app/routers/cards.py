from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session

from app.db import get_session
from app.resources.card_manager import CardManager  

from app.schemas.cards import CreateCard

card_router = APIRouter()

@card_router.post("/create")
async def create_card(
    card_data: CreateCard,
    session: Session = Depends(get_session),
    manager: CardManager = Depends(CardManager),
):
    card = manager.get_card_by_front(front=card_data.front, session=session)
    if card:
        return {"message": "Card with this front already exists"}
    
    card = manager.create_card(card_data, session)
    return card

@card_router.get("/get/{card_id}")
async def get_card(card_id: str, session: Session = Depends(get_session), manager: CardManager = Depends(CardManager)):
    card = manager.get_card_by_id(card_id=card_id, session=session)
    if not card:
        return {"message": "Card not found"}
    return card

@card_router.get("/get_all")
async def get_all_cards(session: Session = Depends(get_session), manager: CardManager = Depends(CardManager)):
    cards = manager.get_all_cards(session)
    return cards

@card_router.get("/get_deck_cards/{deck_id}")
async def get_all_deck_cards(deck_id: str, session: Session = Depends(get_session), manager: CardManager = Depends(CardManager)):
    cards = manager.get_all_deck_cards(deck_id=deck_id, session=session)
    return cards

