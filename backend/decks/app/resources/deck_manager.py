from sqlmodel import Session
from sqlmodel import select
from app.schemas.decks import CreateDeck
from app.models.models import Deck
import uuid


class DeckManager:

    def create_deck(self, deck_data: CreateDeck, session: Session) -> Deck:
        deck_data_dict = deck_data.model_dump()
        deck_data_dict["id"] = uuid.uuid4()
        deck = Deck(**deck_data_dict)

        session.add(deck)
        session.commit()
        session.refresh(deck)
        return deck

    def get_deck_by_name(self, name: str, session: Session):
        statement = select(Deck).where(Deck.name == name)
        result = session.exec(statement).first()
        return result

    def get_deck_by_id(self, deck_id: uuid, session: Session) -> Deck:
        statement = select(Deck).where(Deck.id == deck_id)
        result = session.exec(statement).first()
        return result

    def get_all_decks(self, session: Session):
        statement = select(Deck)
        result = session.exec(statement).all()
        return result

    def update_deck(self, deck: Deck, deck_data: CreateDeck, session: Session) -> Deck:
        deck.name = deck_data.name
        deck.description = deck_data.description
        session.add(deck)
        session.commit()
        session.refresh(deck)
        return deck

    def delete_deck(self, deck: Deck, session: Session):
        session.delete(deck)
        session.commit()
        return {"message": "Deck deleted"}
