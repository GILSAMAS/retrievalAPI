from pydantic import BaseModel


class CreateDeck(BaseModel):
    name: str
    description: str    