import customtkinter as ctk
from ui.notepad import Notepad
from ui.calculator import Calculator
from ui.overclocker import overclocker
from PIL import Image


class Taskbar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=50, height=50, **kwargs)
        self.pack_propagate(False)
        self.notepadimg = Image.open("textures/notepad.png")
        self.notepadimgctk = ctk.CTkImage(self.notepadimg)
        self.notepadbtn = ctk.CTkButton(
            self, command=self.open_notepad, image=self.notepadimgctk, text=""
        )
        self.notepadbtn.pack(side="left")
        self.notepad_window = None
        self.calculatorimg = Image.open("textures/calculator.png")
        self.calculatorimgctk = ctk.CTkImage(self.calculatorimg)
        self.calculatorbtn = ctk.CTkButton(
            self, command=self.open_calculator, text="", image=self.calculatorimgctk
        )
        self.calculatorbtn.pack(side="left")
        self.calculator_window = None
        self.overclockerimg = Image.open("textures/overclocker.png")
        self.overclockerimgctk = ctk.CTkImage(self.overclockerimg)
        self.overclockerbtn = ctk.CTkButton(
            self, command=self.open_overclocker, text="", image=self.overclockerimgctk
        )
        self.overclockerbtn.pack(side="left")
        self.overclocker_window = None
        self.shutdownimg = Image.open("textures/closeicon.png")
        self.shutdownimgctk = ctk.CTkImage(self.shutdownimg)
        self.shutdownbtn = ctk.CTkButton(self, text="", image=self.shutdownimgctk)
        self.shutdownbtn.pack(side="left")

    def open_notepad(self):
        if self.notepad_window is None or not self.notepad_window.exists():
            self.notepad_window = Notepad(self)
        else:
            self.notepad_window.focus()

    def open_calculator(self):
        if self.calculator_window is None or not self.calculator_window.exists():
            self.calculator_window = Calculator(self)
        else:
            self.calculator_window.focus()

    def open_overclocker(self, master):
        if self.overclocker_window is None or not self.overclocker_window.exists():
            self.overclocker_window = overclocker(self)

            def addmhz():
                self.overclocker_window.mhz += 0.1
                self.overclocker_window.mhzlabel.configure(
                    text=f"{self.overclocker_window.mhz} Mhz"
                )
                if self.overclocker_window.mhz >= 2.0:
                    master.destroy()

            self.overclocker_window.addbtn.configure(command=addmhz)

            def removemhz():
                self.overclocker_window.mhz -= 0.1
                self.overclocker_window.mhzlabel.configure(
                    text=f"{self.overclocker_window.mhz} Mhz"
                )
                if self.overclocker_window.mhz <= 0.5:
                    master.destroy()

            self.overclocker_window.subtractbtn.configure(command=removemhz)

        else:
            self.overclocker_window.focus()
