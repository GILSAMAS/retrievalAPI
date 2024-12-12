from sqlmodel import SQLModel
from sqlmodel import Field

from typing import Optional
from typing import List
from datetime import datetime


class Metrics(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    description: str
    tags: Optional[List[str]] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
