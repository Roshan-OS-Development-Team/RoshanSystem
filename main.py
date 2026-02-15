import tkinter as tk
from tkinter import filedialog
import time

root = tk.Tk()
root.title("Roshan System")
root.geometry("1200x800")
window = tk.Frame(root)
window.pack(fill="both", expand=True)

from gui import taskbar
from gui import desktop
from functions import notepad
from functions import calculator
taskbar.root = root
taskbar.window = window
desktop.root = root
desktop.window = window
notepad.root = root
calculator.root = root

root.mainloop()