from sqlmodel import SQLModel 
from sqlmodel import Field 

from typing import Optional
from typing import List 
from datetime import datetime 
import uuid 

from src.api.db.models.cards import Card
from src.api.db.models.decks import Deck


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str 
    last_name: str 
    username: str
    email: str
    password: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    def __repr__(self):
        return f"User {self.username}"
