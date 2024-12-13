from sqlmodel import SQLModel
from sqlmodel import Field
import uuid
from datetime import datetime
from typing import List
from typing import Optional


class Deck(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
