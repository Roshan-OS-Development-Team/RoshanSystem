import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark") 

class Taskbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
