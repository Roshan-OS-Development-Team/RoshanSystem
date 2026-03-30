import customtkinter as ctk


class overclocker(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Overclocker")
        self.mhz = 1.0
        self.subtractbtn = ctk.CTkButton(self, text="-")
        self.subtractbtn.pack(side="left")
        self.mhzlabel = ctk.CTkLabel(self, text=f"{self.mhz} Mhz")
        self.mhzlabel.pack(side="left")
        self.addbtn = ctk.CTkButton(self, text="+")
        self.addbtn.pack(side="left")
