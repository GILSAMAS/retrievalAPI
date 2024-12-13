from src.api.session.schema import CreateRecord
from src.api.db.db import get_session
from src.api.db.models.tracker import SessionTracker
from sqlmodel import Session
from sqlmodel import select 

class RecordManager():

    def create_record(self, record_data: CreateRecord, session: Session) -> SessionTracker:
        """
        Create a record

        :param record_data: CreateRecord: The record data
        :param session: Session: The database session
        :return: Record: The created record
        """
        
        record = SessionTracker(**record_data.model_dump())
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    
    def get_all_records(self, session: Session):
        statement = select(SessionTracker).order_by(SessionTracker.score)
        result = session.exec(statement).all()
        return result