import tkinter as tk
from tkinter import filedialog

root = None
window = None

taskbar = tk.Frame(window, bg="black")
taskbar.pack(side="bottom", fill="x", expand=True, pady=0)

from functions import startmenu
from functions.startmenu import togglestartmenu

startmenu.taskbar = taskbar
startmenuimg = tk.PhotoImage(file="textures/startmenu.png")
startmenubtn = tk.Button(taskbar, image=startmenuimg, bg="black", command=togglestartmenu)
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

from functions.overclocker import overclocker

overclockerimg = tk.PhotoImage(file="textures/overclocker.png")
overclockerbtn = tk.Button(taskbar, image=overclockerimg, command=overclocker)
overclockerbtn.pack(side="left")