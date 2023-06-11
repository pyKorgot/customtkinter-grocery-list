import customtkinter as ctk
from typing import Callable
from app.core.db import get_db
from app.crud.crud_product import product as crud_product
from app.crud.crud_purchases import purchases as crud_purchases
from app.models.product import Product
from datetime import datetime


class AddPurchasesWindow(ctk.CTkToplevel):
    date_format = '%d.%m.%Y'
    close_window: Callable = None
    save_item: Callable = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.create_window_element()
        self.attach_window_element()

    def create_window_element(self):
        db = get_db()
        products: list[Product] = crud_product.get_multi(db)

        self.combobox_product = ctk.CTkComboBox(
            self,
            values=list(map(lambda row: row.product_name, products)),
            width=200
        )
        self.date_purchases = ctk.CTkEntry(
            self,
            placeholder_text=datetime.strftime(datetime.today(),
                                               self.date_format)
        )
        self.button_save = ctk.CTkButton(self,
                                         text='Save Product',
                                         command=self.save_item)
        self.button_cancel = ctk.CTkButton(self,
                                           text='Cancel',
                                           command=self.close_window)

    def attach_window_element(self):
        self.combobox_product.grid(row=0, column=0, columnspan=2,
                                   padx=5, pady=5,
                                   sticky='ew')
        self.date_purchases.grid(row=1, column=0, columnspan=2,
                                 padx=5, pady=5,
                                 sticky='ew')
        self.button_save.grid(row=2, column=0,
                              padx=5, pady=5,
                              sticky='ew')
        self.button_cancel.grid(row=2, column=1,
                                padx=5, pady=5,
                                sticky='ew')


class AddPurchasesController(AddPurchasesWindow):
    def close_window(self):
        self.destroy()

    def save_item(self):
        db = get_db()
        product = self.combobox_product.get()
        date = self.date_purchases.get()
        date = datetime.strptime(date, self.date_format).date()

        id_product = crud_product.get_id(db, Product.product_name == product)
        crud_purchases.create(db, {'id_product': id_product,
                                   'date_purchases': date})
        db.commit()

        self.close_window()
