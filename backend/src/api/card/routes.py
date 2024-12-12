from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from src.api.db.db import get_session
from src.api.card.schemas import CreateCard
from src.api.db.models.cards import Card
from src.api.card.manager import CardManager

card_router = APIRouter()


# create a card
@card_router.post("/create")
async def create_card(
    card_data: CreateCard,
    session: Session = Depends(get_session),
    manager: CardManager = Depends(CardManager),
) -> Card:
    return {"message": "Card created"}
