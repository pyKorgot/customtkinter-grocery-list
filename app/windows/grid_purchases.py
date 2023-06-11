from datetime import datetime

import customtkinter as ctk

from app.core.config import settings
from app.core.db import get_db
from app.models import Product, Purchases


class GridPurchases(ctk.CTkFrame):
    update_grid = None

    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)

        self.update_grid()

    def write_header(self):
        self.header_name = ctk.CTkLabel(self,
                                        text='Name Product',
                                        width=200,
                                        fg_color='gray60')
        self.header_name.grid(row=1, column=0, pady=3, padx=0, sticky='ew')
        self.date_purchases = ctk.CTkLabel(self,
                                           text='Date Purchases',
                                           width=100,
                                           fg_color='gray60')
        self.date_purchases.grid(row=1, column=1, pady=3, padx=0, sticky='ew')

    def get_store(self) -> list:
        db = get_db()
        store = db.query(
            Product.product_name, Purchases.date_purchases) \
            .join(Product, Product.id_product == Purchases.id_product) \
            .all()
        return store

    def write_store(self, store: list) -> None:
        for index_row, row in enumerate(store, start=2):
            self.write_row(index_row, row)

    def write_row(self, index_row, row) -> None:
        self.name_product = ctk.CTkLabel(
            self,
            text=row.product_name,
            fg_color='gray80',
            width=100
        )
        self.name_product.grid(row=index_row,
                               column=0,
                               pady=0,
                               padx=0,
                               sticky='ew')
        self.date_purchases = ctk.CTkLabel(
            self,
            text=datetime.strftime(row.date_purchases,
                                   settings.base_datetime_format),
            fg_color='gray80'
        )
        self.date_purchases.grid(row=index_row,
                                 column=1,
                                 pady=0,
                                 padx=0,
                                 sticky='ew')


class GridPurchasesController(GridPurchases):
    def update_grid(self):
        self.write_header()
        store = self.get_store()
        self.write_store(store)
