import tkinter as tk
from tkinter import filedialog
root = None

def notepad():
    notepad = tk.Toplevel(root)
    notepad.title("Notepad")
    notepad.geometry("640x360")
    notepadtext = tk.StringVar()
    def savefile():
        filesave = filedialog.asksaveasfilename(
            title="Save File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if not filesave:
            return
        
        with open(filesave, "w", encoding="utf-8") as f:
            f.write(notepadtext.get())

    def loadfile():
        fileload = filedialog.askopenfilename(
            title="Open File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if not fileload:
            return
        
        with open(fileload, "r", encoding="utf-8") as f:
            notepadtext.set(f.read())

    savebtn = tk.Button(notepad, bg="black", fg="white", command=savefile, text="Save File")
    savebtn.pack(side="top", padx=0, fill="x")
    loadbtn = tk.Button(notepad, bg="black", fg="white", text="Load File", command=loadfile)
    loadbtn.pack(side="top", fill="x")
    notepadentry = tk.Entry(notepad, bg="black", fg="white", textvariable=notepadtext, font=("Segoe UI", 15, "bold"))
    notepadentry.pack(fill="both", expand=True)