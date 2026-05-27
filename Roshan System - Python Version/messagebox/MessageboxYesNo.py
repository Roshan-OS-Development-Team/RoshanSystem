import customtkinter as ctk
from tkinter import StringVar
from gui.window import WindowPackManager
from typing import Callable

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MessageBoxYesNo(WindowPackManager):
    """A yes no messagebox for Roshan OS
    It calls the yes callback function for when yes is pressed
    It callls the no callback function for when no is pressed"""

    def __init__(
        self,
        master,
        title: str,
        message: str,
        yes_callback: Callable,
        no_callback: Callable,
    ):
        super().__init__(master, title)
        ctk.CTkLabel(self, text=message).pack(side="top", pady=5, padx=5)

        self.result_var = StringVar()

        btns_frame = ctk.CTkFrame(self)
        btns_frame.pack()

        ctk.CTkButton(btns_frame, text="Yes", command=yes_callback).pack(
            side="left", pady=5, padx=5
        )
        ctk.CTkButton(btns_frame, text="No", command=no_callback).pack(
            side="left", pady=5, padx=5
        )
