import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark") 

class StartMenu(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=300, height=400)
        self.pack_propagate(False)
