from sqlmodel import SQLModel
from sqlmodel import Field 
from datetime import datetime 
import uuid

class SessionTracker(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True)
    # user_id: uuid.UUID = Field(foreign_key="user.id")
    deck_id: uuid.UUID = Field(foreign_key="deck.id")
    card_id: uuid.UUID = Field(foreign_key="card.id")
    score:float
    timestamp: datetime = Field(default=datetime.now())    
    