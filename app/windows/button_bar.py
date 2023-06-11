import customtkinter as ctk
from app.windows import AddProductController, AddPurchasesController


class ButtonsFrame(ctk.CTkFrame):
    add_product_win = None
    add_purchases_win = None

    def __init__(self, master):
        super().__init__(master, corner_radius=0)

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
        self.add_product_btn.grid(row=0, column=0,
                                  padx=5, pady=10,
                                  sticky='ew')
        self.add_purchases_btn.grid(row=1, column=0,
                                    padx=5, pady=0,
                                    sticky='ew')

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
