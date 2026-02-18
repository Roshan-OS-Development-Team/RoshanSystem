import tkinter as tk
from tkinter import filedialog

root = None
window = None

taskbar = tk.Frame(window, bg="black")
taskbar.pack(side="bottom", fill="x", expand=True, pady=0)

startmenuimg = tk.PhotoImage(file="textures/startmenu.png")
startmenubtn = tk.Button(taskbar, image=startmenuimg, bg="black")
startmenubtn.pack(side="left")

from functions.notepad import notepad

notepadimg = tk.PhotoImage(file="textures/notepad.png")
notepadbtn = tk.Button(taskbar, image=notepadimg, command=notepad)
notepadbtn.pack(side="left")

from functions.calculator import calculator

calculatorimg = tk.PhotoImage(file="textures/calculator.png")
calculatorbtn = tk.Button(taskbar, image=calculatorimg, bg="black", command=calculator)
calculatorbtn.pack(side="left")

from functions.closeos import closeos

closeosimg = tk.PhotoImage(file="textures/closeicon.png")
closeosbtn = tk.Button(taskbar, image=closeosimg, bg="black", command=closeos)
closeosbtn.pack(side="left")