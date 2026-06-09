from gui.window import WindowPackManager
from typing import Callable
from os import PathLike
from PIL import Image
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MessageBoxOkCancel(WindowPackManager):
    def __init__(
        self,
        master: ctk.CTk,
        title: str,
        message: str,
        ok_callback: Callable,
        cancel_callback: Callable,
        image: str | PathLike[str] = "information",
    ):
        super().__init__(master, title)

        if image == "information":
            img = Image.open("textures/information.png").resize((50, 50))
            img_ctk = ctk.CTkImage(img, img, img.size)
        if image == "error":
            img = Image.open("textures/error.png").resize((50, 50))
            img_ctk = ctk.CTkImage(img, img, img.size)
        if image == "warning":
            img = Image.open("textures/warning.png").resize((50, 50))
            img_ctk = ctk.CTkImage(img, img, img.size)
        else:
            img = Image.open(image)
            img_ctk = ctk.CTkImage(img, img, img.size)

        ctk.CTkLabel(self, text=message, image=img_ctk, compound="left", padx=35).pack(
            side="top", padx=5, pady=5
        )

        btns_frame = ctk.CTkFrame(self)
        btns_frame.pack(side="bottom", padx=10, pady=10, fill="x", expand=True)

        ctk.CTkButton(btns_frame, text="Cancel", command=cancel_callback).pack(
            side="left", padx=5, pady=5
        )

        ctk.CTkButton(btns_frame, text="Ok", command=ok_callback).pack(
            size="left", padx=5, pady=5
        )
