from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression

from app.crud.base import CrudBase
from app.models.product import Product


class CrudProduct(CrudBase):
    model = Product

    def get_id(self, db: Session, filter: BinaryExpression):
        return db.query(self.model).filter(filter).first().id_product


product = CrudProduct()
