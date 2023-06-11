import customtkinter as ctk

from app.windows import AddProductController, AddPurchasesController
from app.windows.grid_purchases import GridPurchasesController


class AppMain(ctk.CTk):
    open_add_product = None
    open_add_purchases = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("470x400")

        self.create_window_element()
        self.attach_window_element()

    def create_window_element(self):
        self.add_product_btn = ctk.CTkButton(
            self,
            text="Add Item",
            command=self.open_add_product
        )
        self.add_purchases_btn = ctk.CTkButton(
            self,
            text="Add Purchases",
            command=self.open_add_purchases
        )
        self.grid_purchases = GridPurchasesController(self)

    def attach_window_element(self):
        self.add_product_btn.grid(row=0, column=0,
                                  padx=20, pady=10,
                                  sticky='ew')
        self.add_purchases_btn.grid(row=1, column=0,
                                    padx=20, pady=0,
                                    sticky='ew')
        self.grid_purchases.grid(row=0, column=1,
                                 rowspan=10,
                                 padx=20, pady=10,
                                 sticky='nsew')


class AppController(AppMain):
    add_product_win = None
    add_purchases_win = None

    def open_add_product(self):
        if self.add_product_win is None \
         or not self.add_product_win.winfo_exists():
            self.add_product_win = AddProductController(self)
        else:
            self.add_product_win.focus()

    def open_add_purchases(self):
        if self.add_purchases_win is None \
         or not self.add_purchases_win.winfo_exists():
            self.add_purchases_win = AddPurchasesController(self)
        else:
            self.add_purchases_win.focus()
