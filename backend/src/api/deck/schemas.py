from pydantic import BaseModel
from typing import Optional
from typing import List


class CreateDeck(BaseModel):
    name: str
    description: str
    tags: Optional[List[str]] = []
