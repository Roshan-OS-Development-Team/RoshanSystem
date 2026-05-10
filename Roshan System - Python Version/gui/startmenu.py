import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")


class StartMenu(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=300, height=400)
        self.pack_propagate(False)
