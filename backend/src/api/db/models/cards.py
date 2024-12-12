from sqlmodel import Field
from sqlmodel import SQLModel

from datetime import datetime
from typing import Optional
from typing import List
import uuid


class Card(SQLModel, table=True):
    id: str = Field(default_factory=uuid.uuid4, primary_key=True)
    front: str
    back: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    deck_id: Optional[uuid.UUID] = Field(default=None, foreign_key="deck.id")
    tags: Optional[List[str]] = []


class StudySession(SQLModel, table=True):
    id: str = Field(default_factory=uuid.uuid4, primary_key=True)
    deck_id: uuid.UUID
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    studied_card: uuid.UUID
    score: float
