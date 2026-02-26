import tkinter as tk

root = None

def overclocker():
    overclockerwin = tk.Toplevel(root)
    overclockerwin.title("Overclocker")
    btnsframe = tk.Frame(overclockerwin, bg="white")
    btnsframe.pack(fill="x", expand=True)
    value = tk.DoubleVar(value=1.5)
    from functions.crash import crash
    def add():
        value.set(value.get()+0.1)
        if value.get() >= 2:
            crash()
    def remove():
        value.set(value.get()-0.1)
        if value.get() <= 1:
            crash()
    removebtn = tk.Button(overclockerwin, text="-", bg="black", fg="white", font=("Segoe UI", 15, "bold"), command=remove)
    removebtn.pack(fill="x", side="left", expand=True)
    vallabel = tk.Label(overclockerwin, bg="black", fg="white", font=("Segoe UI", 15, "bold"), textvariable=value)
    vallabel.pack(fill="both", side="left", expand=True)
    addbtn = tk.Button(overclockerwin, bg="black", fg="white", font=("Segoe UI", 15, "bold"), text="+", command=add)
    addbtn.pack(fill="x", side="left", expand=True)