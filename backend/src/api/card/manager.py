from sqlmodel import Session
from sqlmodel import select

from src.api.card.schemas import CreateCard
from src.api.db.models.cards import Card


class CardManager:

    def create_card(self, card_data: CreateCard, session: Session) -> Card:
        """
        Create a card

        :param card_data: CreateCard: The card data
        :param session: Session: The database session
        :return: Card: The created card
        """

        card_data_dict = card_data.model_dump()
        card = Card(**card_data_dict)
        session.add(card)
        session.commit()
        session.refresh(card)
        return card

    def get_card(self, card_id: str, session: Session):
        """
        Get a card

        :param card_id: str: The card id
        :param session: Session: The database session
        :return: Card: The card
        """

        statement = select(Card).where(Card.id == card_id)
        result = session.exec(statement).first()
        return result

    def delete_card(self, card_id: str, session: Session):
        """
        Delete a card

        :param card_id: str: The card id
        :param session: Session: The database session
        """
        statement = select(Card).where(Card.id == card_id)
        result = session.exec(statement).first()
        session.delete(result)
        session.commit()
        return result
