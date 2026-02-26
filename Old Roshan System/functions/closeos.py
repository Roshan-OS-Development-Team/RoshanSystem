import tkinter as tk
from tkinter import messagebox

root = None

def closeos():
    confirmation = messagebox.askyesno(
        title="Confirm Shutdown",
        message="Are you sure you want to shutdown this pc"
    )
    if confirmation:
        root.destroy()
    else:
        return