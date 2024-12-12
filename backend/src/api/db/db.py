from sqlmodel import create_engine
from sqlmodel import SQLModel
from sqlmodel import Session

DABASE_URL = "sqlite:///db.sqlite"
engine = create_engine(DABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
