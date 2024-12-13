from src.api.db.models.decks import Deck
from src.api.db.models.cards import Card
from src.api.deck.schemas import CreateDeck

from sqlmodel import Session
from sqlmodel import select

from typing import List 

class DeckManager:

    def create_deck(self, deck_data: CreateDeck, session: Session) -> Deck:
        """
        Create a deck

        :param deck_data: CreateDeck: The deck data
        :param session: Session: The database session
        :return: Deck: The created deck
        """

        deck = Deck(**deck_data.model_dump())
        session.add(deck)
        session.commit()
        session.refresh(deck)
        return deck

    def get_deck(self, deck_id: str, session: Session) -> Deck:
        """
        Get a deck

        :param deck_id: str: The deck id
        :param session: Session: The database session
        :return: Deck: The deck
        """
        statement = select(Deck).where(Deck.id == deck_id)
        result = session.exec(statement).first()
        return result

    def delete_deck(self, deck_id: str, session: Session):
        """
        Delete a deck

        :param deck_id: str: The deck id
        :param session: Session: The database session
        """
        statement = select(Deck).where(Deck.id == deck_id)
        result = session.exec(statement).first()
        session.delete(result)
        session.commit()
        return result
    
    def get_all_cards(self, deck_id:str, session:Session)->List[Card]:
        statement = select(Card).where(Card.deck_id == deck_id)
        result = session.exec(statement).all()
        return result
