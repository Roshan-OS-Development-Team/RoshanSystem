from tkinter import PhotoImage
import customtkinter as ctk
import subprocess
import threading

try:
    from gui.window import WindowPackManager
except ImportError:
    from window import WindowPackManager

class Terminal(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "Terminal (I am going to terminate myself)", (960, 480), "textures/terminal.png")
        self.command_box = ctk.CTkTextbox(self)
        self.command_box.insert("end", "> ")
        self.command_box.pack(fill="both", expand=True)
        self.command_box.bind("<Return>", self.handle_command)
        self.line_num: int = 1
    def handle_command(self, event = None):
        command = self.command_box.get(f"{self.line_num}.2", "insert").strip()

        threading.Thread(target=self.execute_command, args=(command, ), daemon=True).start()

        return "break"

    def execute_command(self, command: str):
        process = subprocess.run(command, capture_output=True, shell=True, text=True)

        output = process.stdout if process.stdout else process.stderr

        self.command_box.after(0, self.update_ui, output)

    def update_ui(self, output: str):
        self.line_num += 1

        if output:
            cleaned_output = output.rstrip()
            self.command_box.insert("end", f"\n{cleaned_output}")
            self.line_num += cleaned_output.count("\n")

        self.command_box.insert("end", "\n> ")
        self.line_num += 1

        self.command_box.mark_set("insert", "end - 1c")
        self.command_box.see("end")


if __name__ == '__main__':
    root = ctk.CTk()
    root.title("Terminal (I am going to terminate myself)")
    root.geometry("960x480")
    winico = PhotoImage(file="textures/terminal.png")

    root.after(200, lambda: root.iconphoto(False, winico))
    Terminal(root).place(x=0, y=0)
    root.mainloop()