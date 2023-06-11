from sqlalchemy import create_engine, Engine
from app.core.config import settings
from sqlalchemy.orm import Session


engine: Engine = create_engine(settings.database_uri, pool_pre_ping=True)


def get_db():
    with Session(autoflush=False, bind=engine) as db:
        return db


def update_migration():
    pass
