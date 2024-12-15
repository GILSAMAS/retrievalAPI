from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from sqlmodel import Session
from app.db import get_session
from app.schemas.scorer import CreateScore
from app.resources.scorer_manager import UserScoreManager

score_router = APIRouter()


@score_router.post("/score")
async def create_score(
    score_data: CreateScore,
    session: Session = Depends(get_session),
    manager: UserScoreManager = Depends(UserScoreManager),
):
    score = manager.create_score(score_data, session)

    return {"message": "Score created successfully", "score": score}


@score_router.get("/score/{user_id}")
async def get_user_score(
    user_id: str,
    session: Session = Depends(get_session),
    manager: UserScoreManager = Depends(UserScoreManager),
):
    scores = manager.get_user_score(user_id, session)
    if not scores:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No scores found for the user",
        )
    return {"scores": scores}
