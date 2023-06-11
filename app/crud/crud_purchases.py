from .base import CrudBase
from app.models import Purchases


class CrudPurchases(CrudBase):
    model = Purchases


purchases = CrudPurchases()
