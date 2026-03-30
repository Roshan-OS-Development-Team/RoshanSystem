import customtkinter as ctk

class Calculator(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calculator")
        self.entry1 = ctk.CTkEntry(self)
        self.entry1.pack(side="top", fill="x")
        self.entry2 = ctk.CTkEntry(self)
        self.entry2.pack(side="top", fill="x")
        self.answerlabel = ctk.CTkLabel(self, text="")
        self.answerlabel.pack(side="top", fill="x")
        self.addbtn = ctk.CTkButton(self, text="Add (+)", command=self.add)
        self.addbtn.pack(side="top", fill="x")
        self.subtractbtn = ctk.CTkButton(self, text="Subtract (-)", command=self.subtract)
        self.subtractbtn.pack(side="top", fill="x")
        self.multiplybtn = ctk.CTkButton(self, text="Multiply (x , *)", command=self.multiply)
        self.multiplybtn.pack(side="top", fill="x")
        self.dividebtn = ctk.CTkButton(self, text="Divide (/)", command=self.divide)
        self.dividebtn.pack(side="top")
    def add(self):
        self.answerlabel.configure(text=f"{float(self.entry1.get()) + float(self.entry2.get())}")
    def subtract(self):
        self.answerlabel.configure(text=f"{float(self.entry1.get()) - float(self.entry2.get())}")
    def multiply(self):
        self.answerlabel.configure(text=f"{float(self.entry1.get()) * float(self.entry2.get())}")
    def divide(self):
        self.answerlabel.configure(text=f"{float(self.entry1.get()) / float(self.entry2.get())}")
