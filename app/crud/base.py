from typing import TypeVar
from app.models.base import Base
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression


ModelType = TypeVar("ModelType", bound=Base)


class CrudBase:
    model = None

    def create(self, db: Session, obj_in: dict):
        db_obj = self.model(**obj_in)  # type: ignore
        db.add(db_obj)
        db.flush()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, filter: BinaryExpression):
        return db.query(self.model).filter(filter).first()

    def get_multi(self, db: Session, filter: BinaryExpression = True):
        return db.query(self.model).filter(filter).all()
