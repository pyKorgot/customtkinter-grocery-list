import customtkinter
from app.core.db import get_db
from app.models import Product, Purchases
from app.core.config import settings
from datetime import datetime


class GridPurchases(customtkinter.CTkFrame):
    update_grid = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.update_grid()
        self.add_update_btn()

    def add_update_btn(self):
        self.update_btn = customtkinter.CTkButton(self,
                                                  text='Update Grid',
                                                  command=self.update_grid)
        self.update_btn.grid(row=0, column=0, columnspan=2, sticky='ew')

    def write_header(self):
        self.header_name = customtkinter.CTkLabel(self,
                                                  text='Name Product',
                                                  width=100)
        self.header_name.grid(row=1, column=0, pady=3, padx=10, sticky='ew')
        self.date_purchases = customtkinter.CTkLabel(self,
                                                     text='Date Purchases',
                                                     width=100)
        self.date_purchases.grid(row=1, column=1, pady=3, padx=10, sticky='ew')

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
        self.name_product = customtkinter.CTkLabel(
            self,
            text=row.product_name
        )
        self.name_product.grid(row=index_row,
                               column=0,
                               pady=1,
                               padx=10,
                               sticky='ew')
        self.date_purchases = customtkinter.CTkLabel(
            self,
            text=datetime.strftime(row.date_purchases,
                                   settings.base_datetime_format)
        )
        self.date_purchases.grid(row=index_row,
                                 column=1,
                                 pady=1,
                                 padx=3,
                                 sticky='ew')


class GridPurchasesController(GridPurchases):
    def update_grid(self):
        self.write_header()
        store = self.get_store()
        self.write_store(store)
