from app.models import Purchases

from .base import CrudBase


class CrudPurchases(CrudBase):
    model = Purchases


purchases = CrudPurchases()
