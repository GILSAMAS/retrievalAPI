from pydantic import BaseModel 
import uuid 

class CreateRecord(BaseModel):
    deck_id: uuid.UUID
    card_id: uuid.UUID
    score: float