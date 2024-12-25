from sqlmodel import Session
from sqlmodel import select
from app.schemas.cards import CreateCard
from app.models.models import Card
import uuid
from typing import List
from typing import Dict


class CardManager:

    def create_card(self, card_data: CreateCard, session: Session) -> Card:
        card_data_dict = card_data.model_dump()
        card_data_dict["id"] = uuid.uuid4()
        card = Card(**card_data_dict)
        session.add(card)
        session.commit()
        session.refresh(card)
        return card

    def get_card_by_id(self, card_id: str, session: Session) -> Card:
        statement = select(Card).where(Card.id == card_id)
        result = session.exec(statement).first()
        return result

    def get_card_by_front(self, front: str, session: Session) -> Card:
        statement = select(Card).where(Card.front == front)
        result = session.exec(statement).first()
        return result

    def get_all_cards(self, session: Session) -> List[Card]:
        statement = select(Card)
        result = session.exec(statement).all()
        return result

    def get_all_deck_cards(self, deck_id: str, session: Session):
        statement = select(Card).where(Card.deck_id == uuid.UUID(deck_id))
        result = session.exec(statement).all()
        return result

    def delete_card(self, card_id: uuid.UUID, session: Session) -> Dict[str, str]:
        statement = select(Card).where(Card.id == card_id)
        card = session.exec(statement).first()
        session.delete(card)
        session.commit()
        return {"message": "Card deleted"}

    def delete_all_deck_cards(
        self, deck_id: uuid.UUID, session: Session
    ) -> Dict[str, str]:
        statement = select(Card).where(Card.deck_id == deck_id)
        cards = session.exec(statement).all()
        for card in cards:
            session.delete(card)
        session.commit()
        return {"message": "All cards deleted"}
