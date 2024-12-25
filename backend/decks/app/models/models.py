from sqlmodel import SQLModel
from sqlmodel import Field
from sqlmodel import Relationship
import uuid
from typing import List
from typing import Optional
from datetime import datetime


class Card(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    front: str
    back: str
    created_at: datetime = Field(default=datetime.now())
    deck_id: uuid.UUID = Field(default=None, foreign_key="deck.id")
    deck: Optional["Deck"] = Relationship(back_populates="cards")


class Deck(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    name: str
    description: str
    created_at: datetime = Field(default=datetime.now())
    cards: List["Card"] = Relationship(back_populates="deck")
