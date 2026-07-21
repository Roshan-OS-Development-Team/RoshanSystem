from gui.window import WindowPackManager
import customtkinter as ctk
from PIL import Image


class Rosver(WindowPackManager):
    def __init__(self, master: ctk.CTk):
        super().__init__(master, "Rosver", (300, 500))
        os_logo = Image.open("textures/startmenu.png").resize((100, 100))
        os_logo_ctk = ctk.CTkImage(os_logo, size=os_logo.size)
        ctk.CTkLabel(
            self,
            text=" " * 3 + "Roshan OS",
            image=os_logo_ctk,
            compound="left",
            font=("Arial", 30, "bold"),
            text_color=("black", "white"),
        ).pack(side="top", pady=10)

        ctk.CTkLabel(
            self,
            text="\n" * 2 + "Roshan OS\nVersion 18 | Build Number 18.200726",
        ).pack(side="top")

        ctk.CTkLabel(
            self,
            text="\n" * 2 + "The Source Code and GUI of Roshan OS\n"
            " is open-source for anyone to use.\n"
            "Roshan OS is licensed under the MIT license",
        ).pack(side="top", pady=10)

        ctk.CTkLabel(
            self,
            text="\n" * 2
            + "Roshan OS Development Team\nRoshan | Lead Dev\nA cool black hole | Artist\nMacanautics | Artist",
        ).pack(side="top")

        ctk.CTkButton(self, text="Exit", command=self.place_forget).pack(
            side="top", pady=20
        )


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Rosver -- TESTING ENVIROMENT NOT FOR END USER --")
    root.geometry("300x500")
    Rosver(root).place(x=0, y=0)
    root.mainloop()
