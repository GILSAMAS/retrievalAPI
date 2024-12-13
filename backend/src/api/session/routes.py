from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from src.api.db.db import get_session
from src.api.session.schema import CreateRecord
from src.api.session.manager import RecordManager

session_router = APIRouter(tags=["Session"])    


@session_router.post("/create_record")
async def create_record(
    record_data: CreateRecord,
    session: Session = Depends(get_session),
    manager: RecordManager = Depends(RecordManager),
):
    manager.create_record(record_data, session)
    
    return {"message": "Record created"}

@session_router.get("/get_all_records")
async def get_all_records(
    session: Session = Depends(get_session),
    manager: RecordManager = Depends(RecordManager),
):
    records = manager.get_all_records(session)
    return records
