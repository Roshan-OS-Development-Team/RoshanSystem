from PIL import Image
import customtkinter as ctk
from gui.taskbar import Taskbar
from gui.notepad import Notepad


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roshan System")
        self.geometry("1200x800")
        self.attributes(fullscreen=True)
        self.backgroundimg = Image.open("textures/background5.png")
        self.backgroundctk = ctk.CTkImage(self.backgroundimg, size=(1200, 800))
        self.background = ctk.CTkLabel(self, text="", image=self.backgroundctk)
        self.background.pack(fill="both", side="top")
        self.bind("<Configure>", self.resize_background)
        self.taskbar = Taskbar(
            self.background,
            width=self.winfo_width(),
            corner_radius=50,
            fg_color="gray7",
        )
        self.notepadbtn = ctk.CTkButton(
            self.taskbar, text="Open Notepad", command=self.open_notepad
        )
        self.notepadbtn.pack(side="left")
        self.notepad = Notepad(self)

    def open_notepad(self):
        self.notepad.place(x=60, y=60)

    def resize_background(self, event=None):
        if event.widget == self:
            self.backgroundctk.configure(size=(self.winfo_width(), self.winfo_height()))
            self.background.configure(image=self.backgroundctk)
            self.taskbar.configure(width=self.winfo_width(), height=70)
            self.taskbar.pack_propagate(False)
            self.taskbar.place(x=0, y=self.winfo_height() - 70)


if __name__ == "__main__":
    root = App()
    root.mainloop()
