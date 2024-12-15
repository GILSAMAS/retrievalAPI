from sqlmodel import Field 
from sqlmodel import SQLModel
from sqlmodel import Relationship
from app.models.deck import Deck
import uuid 
from typing import Optional 


class Card(SQLModel, table=True):
    id: uuid.UUID = Field(default = uuid.uuid4(), primary_key=True)
    front: str 
    back: str
    deck_id: uuid.UUID = Field(default = None, foreign_key="deck.id")
    deck: Optional[Deck] = Relationship(back_populates="decks")