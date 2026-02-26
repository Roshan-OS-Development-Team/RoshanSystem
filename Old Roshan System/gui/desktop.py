import tkinter as tk
import time
from tkinter import filedialog

root = None
window = None
taskbar = None

backgroundimg = tk.PhotoImage(file="textures/background2.png")
background = tk.Label(window, image=backgroundimg)
background.pack(fill="both", expand=True)