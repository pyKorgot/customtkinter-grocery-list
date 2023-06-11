from sqlalchemy import Column, Integer, ForeignKey, Date
from app.models.base import Base


class Purchases(Base):
    __tablename__ = "t_purchases"

    id_purchases = Column(Integer, primary_key=True, index=True, comment='ID')
    id_product = Column(Integer, ForeignKey('t_product.id_product'),
                        nullable=False, comment='ID product')
    date_purchases = Column(Date, nullable=False, comment='Product Name')
