from fastapi import APIRouter
from fastapi import status 
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session
from app.schemas.user import UserLogin
from app.resources.user_manager import UserManager
from app.db import get_session

login_router = APIRouter()

@login_router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(login_data: UserLogin, session: Session= Depends(get_session), manager: UserManager= Depends(UserManager)):
    """
    This endpoint is used to login the user
    """
    user = manager.get_user_by_email(email=login_data.email, session=session)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"message": "Login"}

@login_router.post("/logout")
async def logout():
    return {"message": "Logout"}

@login_router.post("/signup")
async def create_user():
    return {"message": "Register"}

@login_router.post("/refresh_token")
async def get_new_access_token():
    return {"message": "Refresh Token"}


