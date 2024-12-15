from pydantic import BaseModel
import uuid


class CreateScore(BaseModel):
    user_id: uuid.UUID
    deck_id: uuid.UUID
    card_id: uuid.UUID
    metric: str
    score: float
