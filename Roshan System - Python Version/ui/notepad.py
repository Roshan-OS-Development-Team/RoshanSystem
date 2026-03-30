import customtkinter as ctk
from PIL import Image

class Notepad(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Notepad")
        def savefile():
            filesave = ctk.filedialog.asksaveasfilename(
                title="Save txt file",
                defaultextension="*.txt",
                filetypes=[("Text Files", ".txt")]
            )
            if not filesave:
                return
            with open(filesave, "w", encoding="utf-8") as f:
                f.write(self.textbox.get("1.0", "end"))
        def loadfile():
            fileopen = ctk.filedialog.askopenfilename(
                title="Open txt file",
                defaultextension="*.txt",
                filetypes=[("Text Files", ".txt")]
            )
            with open(fileopen, "r", encoding="utf-8") as f:
                self.textbox.delete("0.0", "end")
                self.textbox.insert("0.0", f.read())
        self.btnsframe = ctk.CTkFrame(self)
        self.btnsframe.pack(side="top", fill="x")
        self.savebtn = ctk.CTkButton(self.btnsframe, command=savefile, text="Save File")
        self.savebtn.pack(side="left", fill="x")
        self.loadbtn = ctk.CTkButton(self.btnsframe, command=loadfile, text="Load File")
        self.loadbtn.pack(side="left", fill="x")
        self.textbox = ctk.CTkTextbox(self)
        self.textbox.pack(side="top", fill="both")