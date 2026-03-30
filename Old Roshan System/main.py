import customtkinter as ctk
import os
from ui.taskbar import Taskbar
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roshan System")
        self.attributes(fullscreen=True)
        self.geometry("1200x800")
        self.bgimg = Image.open("textures/background7.png")
        self.bgimgctk = ImageTk.PhotoImage(self.bgimg)
        self.background = ctk.CTkCanvas(self, highlightthickness=0)
        self.background.pack(fill="both", expand=True)
        self.taskbar = Taskbar(self)
        self.taskbar.place(relx=0, rely=1, relwidth=1, anchor="sw")
        self.taskbar.shutdownbtn.configure(command=self.shutdown)
        self.enterfullscreenbtn = ctk.CTkButton(
            self.taskbar, text="Enter Fullscreen", command=lambda: self.fullscreen(True)
        )
        self.enterfullscreenbtn.pack(side="left")
        self.exitfullscreenbtn = ctk.CTkButton(
            self.taskbar, text="Exit Fullscreen", command=lambda: self.fullscreen(False)
        )
        self.exitfullscreenbtn.pack(side="left")
        self.bind("<Configure>", self.resizebackground)
        self.after(1, self.force_initial_resize)

    def force_initial_resize(self):
        self.resizebackground(
            type(
                "Event",
                (),
                {"width": self.winfo_width(), "height": self.winfo_height()},
            )
        )

    def resizebackground(self, event):
        width = event.width
        height = event.height
        resized = self.bgimg.resize((width, height))
        self.bgimgctk = ImageTk.PhotoImage(resized)
        self.background.delete("all")
        self.background.create_image(0, 0, anchor="nw", image=self.bgimgctk)

    def shutdown(self):
        msg = CTkMessagebox(
            title="Shutdown",
            message="Do you want to shutdown?",
            option_1="Yes",
            option_2="No",
            icon="question",
        )
        response = msg.get()
        if response == "Yes":
            self.destroy()
        else:
            return

    def fullscreen(self, fullscreenbool: bool):
        root.attributes(fullscreen=fullscreenbool)


root = App()
root.mainloop()
