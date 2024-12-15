from sqlmodel import SQLModel
from sqlmodel import Field
from sqlmodel import Relationship
from app.models.card import Card
import uuid


class Deck(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    name: str
    description: str
    cards: list["Card"] = Relationship(back_populates="card")
