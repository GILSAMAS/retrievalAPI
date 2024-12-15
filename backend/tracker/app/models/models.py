from sqlmodel import SQLModel
from sqlmodel import Field
import uuid
from datetime import datetime


class Score(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID
    deck_id: uuid.UUID
    card_id: uuid.UUID
    metric: str
    score: float
    created_at: datetime = Field(default_factory=datetime.now)
