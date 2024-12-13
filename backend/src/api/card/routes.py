from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from src.api.db.db import get_session
from src.api.card.schemas import CreateCard
from src.api.db.models.cards import Card
from src.api.card.manager import CardManager

card_router = APIRouter(tags=["Card"])


# create a card
@card_router.post("/create")
async def create_card(
    card_data: CreateCard,
    session: Session = Depends(get_session),
    manager: CardManager = Depends(CardManager),
) -> Card:
    new_card = manager.create_card(card_data, session)
    return new_card


@card_router.get("/get/{card_id}")
async def get_card(
    session: Session = Depends(get_session),
    manager: CardManager = Depends(CardManager),
) -> Card:
    
    # analize the score of the card
    # find the right card
    card_id = "1"
    card = manager.get_card(card_id, session)
    return card

@card_router.delete("/delete/{card_id}")
async def delete_card(
    card_id: str,
    session: Session = Depends(get_session),
    manager: CardManager = Depends(CardManager),
) -> Card:
    manager.delete_card(card_id, session)
    return {"message": "Card deleted"}