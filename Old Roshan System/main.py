import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("Roshan System")
root.attributes(fullscreen=True)
window = tk.Frame(root)
window.pack(fill="both", expand=True)

from gui import taskbar,desktop
from functions import notepad,calculator,closeos,crash,overclocker,startmenu

taskbar.root = root
taskbar.window = window
desktop.root = root
desktop.window = window
notepad.root = root
calculator.root = root
closeos.root = root
crash.root = root
overclocker.root = root
startmenu.root = root
startmenu.window = window

root.mainloop()