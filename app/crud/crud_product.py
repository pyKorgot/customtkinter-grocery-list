from app.crud.base import CrudBase
from app.models.product import Product
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression


class CrudProduct(CrudBase):
    model = Product

    def get_id(self, db: Session, filter: BinaryExpression):
        return db.query(self.model).filter(filter).first().id_product


product = CrudProduct()
