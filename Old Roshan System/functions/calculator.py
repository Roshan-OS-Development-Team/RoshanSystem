import tkinter as tk

root = None

def calculator():
    calculatorwin = tk.Toplevel(root)
    calculatorwin.title("Calculator")
    calculatorwin.geometry("300x162")
    value1 = tk.DoubleVar()
    value2 = tk.DoubleVar()
    equalvalue = tk.DoubleVar()
    entry1 = tk.Entry(calculatorwin, textvariable=value1, bg="black", fg="white")
    entry1.pack(side="top", fill="x")
    entry2 = tk.Entry(calculatorwin, textvariable=value2, bg="black", fg="white")
    entry2.pack(side="top", fill="x")
    label = tk.Label(calculatorwin, textvariable=equalvalue, bg="black", fg="white")
    label.pack(side="top", fill="x")
    def add():
        equalvalue.set(value1.get()+value2.get())
        label.config(textvariable=equalvalue)
    def subtract():
        equalvalue.set(value1.get()-value2.get())
        label.config(textvariable=equalvalue)
    def multiply():
        equalvalue.set(value1.get()*value2.get())
        label.config(textvariable=equalvalue)
    def divide():
        equalvalue.set(value1.get()/value2.get())
        label.config(textvariable=equalvalue)

    addbtn = tk.Button(calculatorwin, text="+", bg="black", fg="white", command=add)
    addbtn.pack(side="top", fill="x")
    subtractbtn = tk.Button(calculatorwin, text="-", bg="black", fg="white", command=subtract)
    subtractbtn.pack(side="top", fill="x")
    multiplybtn = tk.Button(calculatorwin, text="X", bg="black", fg="white", command=multiply)
    multiplybtn.pack(side="top", fill="x")
    dividebtn = tk.Button(calculatorwin, text="/", bg="black", fg="white", command=divide)
    dividebtn.pack(side="top", fill="x")