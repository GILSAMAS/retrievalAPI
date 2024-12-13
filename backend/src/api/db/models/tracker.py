from sqlmodel import SQLModel
from sqlmodel import Field 
from datetime import datetime 
import uuid

class SessionTracker(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    deck_id: uuid.UUID = Field(foreign_key="deck.id")
    card_id: uuid.UUID = Field(foreign_key="card.id")
    timestamp: datetime = Field(default_factory=datetime.now)    
    