from gui.window import WindowPackManager
import customtkinter as ctk
from tkinter import StringVar

class Calculator(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "Calculator", (250, 337), "textures/calculator.png")
        self.flipped: bool = False
        self.nums_var = StringVar()
        ctk.CTkLabel(self, textvariable=self.nums_var, height=50).pack(side="top", fill="x")
        self.btnsframe = ctk.CTkFrame(self)
        self.btnsframe.pack(side="top", fill="both", expand=True)

        ctk.CTkButton(self.btnsframe, text="7", command=lambda: self.add_num_to_var("7"), width=50, height=50).grid(
            row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="8", command=lambda: self.add_num_to_var("8"), width=50, height=50).grid(
            row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="9", command=lambda: self.add_num_to_var("9"), width=50, height=50).grid(
            row=0, column=2, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="/", command=lambda: self.add_operator("/"), width=50, height=50).grid(
            row=0, column=3, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="4", command=lambda: self.add_num_to_var("4"), width=50, height=50).grid(
            row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="5", command=lambda: self.add_num_to_var("5"), width=50, height=50).grid(
            row=1, column=1, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="6", command=lambda: self.add_num_to_var("6"), width=50, height=50).grid(
            row=1, column=2, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="*", command=lambda: self.add_operator("*"), width=50, height=50).grid(
            row=1, column=3, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="1", command=lambda: self.add_num_to_var("1"), width=50, height=50).grid(
            row=2, column=0, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="2", command=lambda: self.add_num_to_var("2"), width=50, height=50).grid(
            row=2, column=1, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="3", command=lambda: self.add_num_to_var("3"), width=50, height=50).grid(
            row=2, column=2, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="-", command=lambda: self.add_operator("-"), width=50, height=50).grid(
            row=2, column=3, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text=".", command=lambda: self.add_num_to_var("."), width=50, height=50).grid(
            row=3, column=0, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="0", command=lambda: self.add_num_to_var("0"), width=50, height=50).grid(
            row=3, column=1, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="=", command=self.eval_operation, width=50, height=50).grid(
            row=3, column=2, padx=5, pady=5)
        ctk.CTkButton(self.btnsframe, text="+", command=lambda: self.add_operator("+"), width=50, height=50).grid(
            row=3, column=3, padx=5, pady=5)


    def add_num_to_var(self, num: str):
        self.nums_var.set(self.nums_var.get() + num)

    def add_operator(self, operator: str):

        self.nums_var.set(self.nums_var.get() + " " + operator + " ")

    def eval_operation(self):
        result = eval(self.nums_var.get())
        self.nums_var.set(str(result))

if __name__ == '__main__':
    root = ctk.CTk()
    root.title("Calculator Test")
    Calculator(root).place(x=0, y=0)
    root.geometry(f"250x337")
    root.mainloop()
