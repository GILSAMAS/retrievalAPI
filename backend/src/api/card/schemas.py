from pydantic import BaseModel
from typing import Optional
from typing import List
import uuid


class CreateCard(BaseModel):
    front: str
    back: str
    deck_id: Optional[uuid.UUID] = None
    tags: Optional[List[str]] = []

class SessionTracker(BaseModel):
    deck_id: uuid.UUID
    card_id: uuid.UUID
    user_id: uuid.UUID
    score: float

# example of table schema
# deck_id | card_id | user_id | score
# 1       | 1       | 1       | 0.5
# 1       | 2       | 1       | 0.5
# 1       | 3       | 1       | 0.5
# 1       | 4       | 1       | 0.5
# 1       | 5       | 1       | 0.5
# 1       | 6       | 1       | 0.5
# 1       | 7       | 1       | 0.5
