from pydantic import BaseModel
from typing import Optional
from typing import List
import uuid


class CreateCard(BaseModel):
    front: str
    back: str
    deck_id: Optional[uuid.UUID] = None
    tags: Optional[List[str]] = []
