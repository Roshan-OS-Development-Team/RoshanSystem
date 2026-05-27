from gui.window import WindowPackManager
from gui.fileexplorer import SaveAsFilename, OpenAsFilename
import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")


class Notepad(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, title="Notepad", size=(640, 360))
        fileoperationsframe = ctk.CTkFrame(self)
        fileoperationsframe.pack(side="top", fill="x")
        savebtn = ctk.CTkButton(
            fileoperationsframe, text="Save File", command=self.save_file
        )
        savebtn.pack(side="left", fill="x", expand=True)
        loadbtn = ctk.CTkButton(
            fileoperationsframe, text="Load File", command=self.load_file
        )
        loadbtn.pack(side="left", fill="x", expand=True)
        self.textbox = ctk.CTkTextbox(self, wrap="word")
        self.textbox.pack(side="top", fill="both", expand=True)

    def save_file(self):
        SaveAsFilename(self.master, ".txt", self.preform_save)

    def preform_save(self, filename):
        with open(f"{filename}.txt", "w") as f:
            f.write(self.textbox.get("1.0", "end"))

    def load_file(self):
        OpenAsFilename(self.master, ".txt", self.preform_load)

    def preform_load(self, filename):
        with open(f"{filename}", "r") as f:
            self.textbox.delete("1.0", "end")
            self.textbox.insert("1.0", f.read())

    def set_text(self, text: str):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)
