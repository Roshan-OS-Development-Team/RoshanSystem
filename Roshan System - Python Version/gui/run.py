from gui.window import WindowPackManager
import customtkinter as ctk
import json as javascript_object_notation
import importlib


class Run(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "Run", (640, 260), "textures/runnew.png")
        with open("run_apps/run_apps.json", "r") as f:
            apps: dict[str, dict[str, str]] = javascript_object_notation.load(f)

        self.apps: dict[str, WindowPackManager] = {}

        for app in apps:
            app_json = apps[app]
            app_module = importlib.import_module(
                app_json["module"]
                if "." in app_json["module"]
                else "run_apps." + app_json["module"]
            )
            app_class = getattr(app_module, app_json["class"])
            class_instance = app_class(master)
            self.apps[app.lower()] = class_instance

        self.app_name = ctk.CTkEntry(self)
        self.app_name.pack(fill="x", padx=20, pady=20)

        self.btns_frame = ctk.CTkFrame(self)
        self.btns_frame.pack(side="top", padx=30, pady=30)

        ctk.CTkButton(self.btns_frame, text="Cancel", command=self.place_forget).pack(
            side="left", padx=20, pady=20
        )

        ctk.CTkButton(
            self.btns_frame, text="Ok", command=self._handle_app_opening
        ).pack(side="left", padx=20, pady=20)

    def _handle_app_opening(self):
        if self.app_name.get().lower() in self.apps:
            self.apps[self.app_name.get().lower()].place(
                x=self.apps[self.app_name.get().lower()].position["x"],
                y=self.apps[self.app_name.get().lower()].position["y"],
            )
        else:
            self.app_name.set("App not found try another one")


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Run -- TESTING ENVIROMENT NOT FOR END USER --")
    root.geometry("640x260")
    Run(root).place(x=0, y=0)
    root.mainloop()
