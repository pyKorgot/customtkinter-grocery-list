from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Product(Base):
    __tablename__ = "t_product"

    id_product = Column(Integer, primary_key=True, index=True, comment='ID')
    product_name = Column(String, nullable=False, comment='Product Name')
