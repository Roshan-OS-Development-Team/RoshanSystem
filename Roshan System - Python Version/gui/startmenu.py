import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")


class StartMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=300, height=400)
