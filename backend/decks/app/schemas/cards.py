from pydantic import BaseModel
import uuid


class CreateCard(BaseModel):
    front: str
    back: str
    deck_id: uuid.UUID
