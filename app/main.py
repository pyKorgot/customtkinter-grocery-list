import customtkinter as ctk

from app.windows.grid_purchases import GridPurchasesController
from app.windows.button_bar import ButtonsFrame


class AppMain(ctk.CTk):
    open_add_product = None
    open_add_purchases = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Grocery List')
        self.geometry("460x500")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.buttons_frame = ButtonsFrame(self)
        self.buttons_frame.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky='sn'
        )

        self.grid_purchases = GridPurchasesController(self)
        self.grid_purchases.grid(
            row=0,
            column=1,
            sticky='snwe'
        )


class AppController(AppMain):
    pass
