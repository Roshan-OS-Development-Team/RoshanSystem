import customtkinter as ctk
from gui.window import WindowPackManager
from typing import Callable
from os import PathLike
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MessageBoxYesNo(WindowPackManager):
    """A yes no messagebox for Roshan OS
    It calls the yes callback function for when yes is pressed
    It callls the no callback function for when no is pressed"""

    def __init__(
        self,
        master: ctk.CTk,
        title: str,
        message: str,
        yes_callback: Callable | None = None,
        no_callback: Callable | None = None,
        image: str | PathLike[str] = "information",
    ):
        super().__init__(master, title)
        if image == "information":
            img = Image.open("textures/information.png").resize((50, 50))
            img_ctk = ctk.CTkImage(img, img, img.size)
        if image == "warning":
            img = Image.open("textures/warning.png").resize((50, 50))
            img_ctk = ctk.CTkImage(img, img, img.size)
        if image == "error":
            img = Image.open("textures/error.png").resize((50, 50))
            img_ctk = ctk.CTkImage(img, img, img.size)
        else:
            img = Image.open(image)
            img_ctk = ctk.CTkImage(img, img, img.size)
        ctk.CTkLabel(self, text=message, compound="left", image=img_ctk, padx=35).pack(
            side="top", pady=5, padx=5
        )

        self.yes_callback = yes_callback or self.destroy
        self.no_callback = no_callback or self.destroy

        btns_frame = ctk.CTkFrame(self)
        btns_frame.pack()

        ctk.CTkButton(btns_frame, text="Yes", command=self.yes_callback).pack(
            side="left", pady=5, padx=5
        )
        ctk.CTkButton(btns_frame, text="No", command=self.no_callback).pack(
            side="left", pady=5, padx=5
        )
