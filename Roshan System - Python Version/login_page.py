import customtkinter as ctk
from os.path import exists
import hashlib
import json


class EntryWithLabel(ctk.CTkFrame):
    def __init__(self, master, text: str, show: str | None = None):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self, text=text).pack(side="left")
        self.entry = ctk.CTkEntry(self)

        if type(show) == str:
            self.entry.configure(show=show)

        self.entry.pack(side="left")

    def get(self):
        return self.entry.get()

    def set(self, text: str):
        self.entry.set(text)


class LoginPage(ctk.CTkFrame):
    def __init__(self, master, width: int, height: int):
        super().__init__(master, width=width, height=height)

        self.pack_propagate(False)

        self.error_message = ctk.CTkLabel(self, text="")
        self.error_message.pack(side="top", pady=20, padx=50)

        self.username_entry = EntryWithLabel(self, "Username: ")
        self.username_entry.pack(side="top", pady=20, padx=50)

        self.password_entry = EntryWithLabel(self, "Password: ", "*")
        self.password_entry.pack(side="top", pady=20, padx=50)

        self.login_btn = ctk.CTkButton(
            self, text="Login", command=self.handle_login_or_sign_up
        )
        self.login_btn.pack(side="top", padx=50, pady=20)

        self.has_acc: bool = False

        if exists("login_details.json"):
            with open("login_details.json", "r") as f:
                self.login_details: dict[str, str] = json.load(f)

            if self.login_details.get("username") and self.login_details.get(
                "password"
            ):
                self.has_acc = True

        else:
            self.login_btn.configure(text="Sign Up")

    def handle_login_or_sign_up(self):
        if self.has_acc:
            if self.username_entry == self.login_details[
                "username"
            ] and self.check_sha3_512(
                self.password_entry.get(), self.login_details["password"]
            ):
                self.destroy()
            else:
                self.error_message.configure(text="Username or Password wrong")
        else:
            self.login_details: dict[str, str] = {
                "username": self.username_entry.get(),
                "password": hashlib.sha3_512(
                    self.password_entry.get().encode("utf-8")
                ).hexdigest(),
            }

            with open("login_details.json", "w") as f:
                json.dump(self.login_details, f, indent=4)

            self.destroy()

    def check_sha3_512(self, text: str, sha3_512: str) -> bool:
        guess = hashlib.sha3_512(text.encode("utf-8")).hexdigest()
        if guess == sha3_512:
            return True
        else:
            return False


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Login Page -- TESTING ENVIROMENT NOT FOR END USER --")
    root.geometry("960x480")
    root.update_idletasks()
    LoginPage(root, 960, 480).place(x=0, y=0)
    root.mainloop()
