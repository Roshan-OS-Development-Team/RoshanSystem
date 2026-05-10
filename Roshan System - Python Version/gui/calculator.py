from gui.window import WindowGridManager
import customtkinter as ctk
from tkinter import DoubleVar


class Calculator(WindowGridManager):
    def __init__(self, master):
        super().__init__(master, "Calculator")
        self.x = DoubleVar()
        self.y = DoubleVar()
        ctk.CTkEntry(self, textvariable=self.x).grid(row=1)
        ctk.CTkEntry(self, textvariable=self.y).grid(row=2)
        self.result = DoubleVar()
        ctk.CTkLabel(self, textvariable=self.result).grid(row=3)
        ctk.CTkButton(
            self,
            text="Add (+)",
            command=lambda: self.do_operation(self.x.get() + self.y.get()),
        ).grid(row=4, column=0)
        ctk.CTkButton(
            self,
            text="Subtract (-)",
            command=lambda: self.do_operation(self.x.get() - self.y.get()),
        ).grid(row=4, column=1)
        ctk.CTkButton(
            self,
            text="Mutliply (*)",
            command=lambda: self.do_operation(self.x.get() * self.y.get()),
        ).grid(row=5, column=0)
        ctk.CTkButton(
            self,
            text="Divide (/)",
            command=lambda: self.do_operation(self.x.get() / self.y.get()),
        ).grid(row=5, column=1)

    def do_operation(self, operation):
        self.result.set(operation)
