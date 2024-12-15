from sqlmodel import Session
from sqlmodel import select
from app.schemas.user import CreateUser
from app.models.user import User
import uuid
from typing import Dict


class UserManager:

    def create_user(self, user_data: CreateUser, session: Session) -> User:
        user_data_dict = user_data.model_dump()
        user = User(**user_data_dict)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get_user_by_username(self, username: str, session: Session) -> User:
        statement = select(User).where(User.username == username)
        result = session.exec(statement).first()
        return result

    def get_user_by_email(self, email: str, session: Session) -> User:
        statement = select(User).where(User.email == email)
        result = session.exec(statement).first()
        return result

    def get_user_by_id(self, user_id: str, session: Session) -> User:
        statement = select(User).where(User.id == uuid.UUID(user_id))
        result = session.exec(statement).first()
        return result

    def get_all_users(self, session: Session) -> list:
        statement = select(User)
        result = session.exec(statement).all()
        return result

    def delete_user_by_email(self, email: str, session: Session) -> Dict[str, str]:
        user = self.get_user_by_email(email, session)
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully"}
