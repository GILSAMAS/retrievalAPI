from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlmodel import Session
from app.db import get_session
from app.models.user import User
from app.resources.user_manager import UserManager

user_router = APIRouter()


@user_router.post("/create", response_model=User)
async def create_user(
    user_data: User,
    session: Session = Depends(get_session),
    manager: UserManager = Depends(UserManager),
):
    user = manager.get_user_by_email(email=user_data.email, session=session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )

    user = manager.create_user(user_data, session)
    return user


@user_router.get("/get/{user_id}", response_model=User)
async def get_user(
    user_id: str,
    session: Session = Depends(get_session),
    manager: UserManager = Depends(UserManager),
):
    user = manager.get_user_by_id(user_id, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@user_router.get("/all", response_model=list[User])
async def get_all_users(
    session: Session = Depends(get_session), manager: UserManager = Depends(UserManager)
):
    users = manager.get_all_users(session)
    return users


@user_router.delete("/delete/{email}")
async def delete_user(
    email: str,
    session: Session = Depends(get_session),
    manager: UserManager = Depends(UserManager),
):
    user = manager.get_user_by_email(email, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    manager.delete_user_by_email(email, session)
    return {"message": "User deleted successfully"}
