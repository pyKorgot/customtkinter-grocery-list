from typing import Callable

import customtkinter as ctk

from app.core.db import get_db
from app.crud.crud_product import product as crud_product


class AddProductWindow(ctk.CTkToplevel):
    close_window: Callable = None
    save_item: Callable = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.create_window_element()
        self.attach_window_element()

    def create_window_element(self):
        self.name_product = ctk.CTkEntry(self,
                                         placeholder_text='Name product',
                                         width=250)
        self.button_save = ctk.CTkButton(self,
                                         text='Save Product',
                                         command=self.save_item)
        self.button_cancel = ctk.CTkButton(self,
                                           text='Cancel',
                                           command=self.close_window)

    def attach_window_element(self):
        self.name_product.grid(row=0, column=0, columnspan=2,
                               padx=5, pady=20,
                               sticky="ew")
        self.button_save.grid(row=1, column=0,
                              padx=5, pady=5,
                              sticky='ew')
        self.button_cancel.grid(row=1, column=1,
                                padx=5, pady=5,
                                sticky='ew')


class AddProductController(AddProductWindow):
    def close_window(self):
        self.destroy()

    def save_item(self):
        db = get_db()
        product_name = self.name_product.get()
        crud_product.create(db, {'product_name': product_name})

        db.commit()
        self.close_window()
