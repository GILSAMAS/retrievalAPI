from sqlmodel import Session
from sqlmodel import select

from app.schemas.scorer import CreateScore
from app.models.models import Score
import uuid
from typing import Dict


class UserScoreManager:

    def create_score(self, score_data: CreateScore, session: Session):
        score_data_dict = score_data.model_dump()

        # verify that the ids are uuid objects
        for key in ["user_id", "deck_id", "card_id"]:
            score_data_dict[key] = self._verify_uuid(score_data_dict[key])

        score = Score(**score_data_dict)

        session.add(score)
        session.commit()
        session.refresh(score)
        return score

    def get_user_score(self, user_id: str, session: Session):
        statement = select(Score).where(Score.user_id == self._verify_uuid(user_id))
        scores = session.exec(statement).all()
        return scores

    def get_card_score(self, card_id: str, user_id: str, session: Session):
        statement = (
            select(Score)
            .where(Score.card_id == self._verify_uuid(card_id))
            .where(Score.user_id == self._verify_uuid(user_id))
        )
        scores = session.exec(statement).all()
        return scores

    def get_deck_score(self, deck_id: str, user_id: str, session: Session):
        statement = (
            select(Score)
            .where(Score.deck_id == self._verify_uuid(deck_id))
            .where(Score.user_id == self._verify_uuid(user_id))
        )
        scores = session.exec(statement).all()
        return scores

    def get_score(self, score_id: str, user_id: str, session: Session):
        statement = (
            select(Score)
            .where(Score.id == self._verify_uuid(score_id))
            .where(Score.user_id == self._verify_uuid(user_id))
        )
        score = session.exec(statement).first()
        return score

    def get_score_by_metric(self, metric: str, user_id: str, session: Session):

        statement = (
            select(Score)
            .where(Score.metric == metric)
            .where(Score.user_id == self._verify_uuid(user_id))
        )
        scores = session.exec(statement).all()
        return scores

    def get_score_by_metric_and_user(self, metric: str, user_id: str, session: Session):
        statement = (
            select(Score)
            .where(Score.metric == metric)
            .where(Score.user_id == self._verify_uuid(user_id))
        )
        scores = session.exec(statement).all()
        return scores

    def _verify_uuid(self, id: str) -> uuid.UUID:
        if isinstance(id, str):
            return uuid.UUID(id)
        else:
            return id
