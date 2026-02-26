import tkinter as tk
from tkinter import messagebox

root = None

def crash():
    root.withdraw()
    crasher = messagebox.showerror(
        title="Crashed",
        message="Your PC Crashed"
    )
    if crasher:
        root.destroy()
    else:
        root.destroy()