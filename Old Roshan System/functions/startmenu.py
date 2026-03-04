import tkinter as tk

startmenuopened = False
root = None
window = None
taskbar = None

startmenu = tk.Frame(root, width=200, height=300)
startmenu.pack_propagate(False)
startmenu.pack(side="bottom", padx=0)

def togglestartmenu():
    global startmenuopened
    if startmenuopened == True:
        startmenuopened = False
        window.tkraise()
        taskbar.tkraise()
    elif startmenuopened == False:
        startmenuopened = True
        startmenu.tkraise()
        taskbar.tkraise()