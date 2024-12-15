from sqlmodel import SQLModel
from sqlmodel import Field
from datetime import datetime
import uuid


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=25, unique=True)
    email: str = Field(max_length=25, unique=True)
    password: str = Field(max_length=100)
    created_at: datetime = Field(default_factory=datetime.now)
