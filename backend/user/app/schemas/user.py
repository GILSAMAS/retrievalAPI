from pydantic import BaseModel


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str
