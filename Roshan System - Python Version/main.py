from PIL import Image
import customtkinter as ctk
from gui.taskbar import Taskbar
from gui.notepad import Notepad
from gui.startmenu import StartMenu
from gui.fileexplorer import FileExplorer
from gui.imageviewer import ImageViewer
from gui.calculator import Calculator

ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roshan System")
        self.geometry("1200x800")
        self.attributes(fullscreen=True)
        self.backgroundimg = Image.open("textures/background7.png")
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

        # Start Menu Stuff
        startbtnimg = Image.open("textures/startmenu.png")
        startbtnimgctk = ctk.CTkImage(startbtnimg, size=(70, 70))
        self.startbtn = ctk.CTkButton(
            self.taskbar,
            image=startbtnimgctk,
            text="",
            bg_color="transparent",
            fg_color="transparent",
            width=70,
            height=70,
            hover_color="#353434",
            command=self.toggle_start_menu,
        )
        self.startbtn.pack(side="left")
        self.startmenu = StartMenu(self.background)
        self.startmenuopened = False

        # Notepad Stuff
        notepadimg = Image.open("textures/notepad.png")
        notepadimgctk = ctk.CTkImage(notepadimg, size=(40, 51))
        self.notepadbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            image=notepadimgctk,
            width=70,
            height=70,
            hover_color="#353434",
            text="",
            fg_color="transparent",
            bg_color="transparent",
            command=lambda: self.open_app(self.notepad),
        )
        self.notepadbtn.pack(side="left")
        self.notepad = Notepad(self)

        # Calculator Stuff
        calculatorimage = Image.open("textures/calculator.png")
        calculatorimagectk = ctk.CTkImage(calculatorimage, size=(36, 52))
        self.calculator = Calculator(self)
        self.calculatorbtn = ctk.CTkButton(
            self.taskbar,
            text="",
            fg_color="transparent",
            bg_color="transparent",
            hover_color="#343435",
            image=calculatorimagectk,
            width=70,
            height=70,
            command=lambda: self.open_app(self.calculator),
        )
        self.calculatorbtn.pack(side="left")

        # File Explorer Stuff
        fileexplorerimg = Image.open("textures/filexplorer.png")
        fileexplorerimgctk = ctk.CTkImage(fileexplorerimg, size=(60, 60))
        self.fileexplorerbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            image=fileexplorerimgctk,
            width=70,
            height=70,
            hover_color="#343435",
            text="",
            bg_color="transparent",
            fg_color="transparent",
            command=lambda: self.open_app(self.fileexplorer),
        )
        self.fileexplorerbtn.pack(side="left")
        self.fileexplorer = FileExplorer(self)

        # Image Viewer Stuff
        self.imageviewer = ImageViewer(self)
        self.imageviewerbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            width=70,
            height=70,
            hover_color="#343435",
            text="Image Viewer",
            bg_color="transparent",
            fg_color="transparent",
            command=lambda: self.open_app(self.imageviewer),
        )
        self.imageviewerbtn.pack(side="left")

        self.startmenuio = ctk.CTkFrame(self, width=50, height=410)
        self.startmenuio.pack_propagate(False)

    def open_app(self, app):
        app.place(x=60, y=60)

    def resize_background(self, event):
        if event.widget == self:
            self.backgroundctk.configure(size=(self.winfo_width(), self.winfo_height()))
            self.background.configure(image=self.backgroundctk)
            self.taskbar.configure(width=self.winfo_width(), height=70)
            self.taskbar.pack_propagate(False)
            self.taskbar.place(x=0, y=self.winfo_height() - 70)

    def toggle_start_menu(self):
        if not self.startmenuopened:
            self.startmenu.place(x=50, y=self.winfo_height() - 480)
            self.startmenuio.place(x=0, y=self.winfo_height() - 480)
            self.startmenuopened = True
        else:
            self.startmenu.place_forget()
            self.startmenuio.place_forget()
            self.startmenuopened = False


if __name__ == "__main__":
    root = App()
    root.mainloop()
