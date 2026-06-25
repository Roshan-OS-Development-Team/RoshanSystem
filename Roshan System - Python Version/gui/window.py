import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark") 

class WindowGridManager(ctk.CTkFrame):
    """A window that uses the grid module,
    You have to input the title,
    Inputting size is optional"""

    def __init__(self, master, title: str, size: tuple[int, int] | None = None):
        super().__init__(master)
        if not size == None:
            self.configure(width=size[0], height=size[1])
            self.grid_propagate(False)
        self.title_bar = ctk.CTkLabel(self, text=title, cursor="fleur")
        self.title_bar.grid(row=0, column=0, sticky="w")
        self.title_bar.bind("<Button-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.do_drag)
        self.position: dict[str, int] = {"x": 0, "y": 0}
        self.closebtn = ctk.CTkButton(
            self,
            command=self.place_forget,
            text="X",
            fg_color="red",
            width=25,
            hover_color="#A00000",
        )
        self.closebtn.grid(row=0, column=1, sticky="e")

    def start_drag(self, event):
        self.startX = event.x_root - self.winfo_x()
        self.startY = event.y_root - self.winfo_y()
        self.lift()

    def do_drag(self, event):
        self.position["x"] = event.x_root - self.startX
        self.position["y"] = event.y_root - self.startY
        self.place(x=self.position["x"], y=self.position["y"])


class WindowPackManager(ctk.CTkFrame):
    """A window that uses the pack manager,
    You need to input the title,
    Inputting size is optional"""

    def __init__(self, master, title: str, size: tuple[int, int] | None = None):
        super().__init__(master)
        if not size == None:
            self.pack_propagate(False)
            self.configure(width=size[0], height=size[1])
        self.title_bar_frame = ctk.CTkFrame(self)
        self.title_bar_frame.pack(side="top", fill="x")
        self.title_bar = ctk.CTkLabel(self.title_bar_frame, text=title).pack(
            side="left", fill="x"
        )
        self.position: dict[str, int] = {"x": 0, "y": 0}
        ctk.CTkButton(
            self.title_bar_frame,
            text="X",
            width=25,
            command=self.place_forget,
            fg_color="red",
            hover_color="#A00000",
        ).pack(side="right")
        self.title_bar_frame.bind("<Button-1>", self.start_drag)
        self.title_bar_frame.bind("<B1-Motion>", self.do_drag)

    def start_drag(self, event):
        self.startX = event.x_root - self.winfo_x()
        self.startY = event.y_root - self.winfo_y()
        self.lift()

    def do_drag(self, event):
        self.position["x"] = event.x_root - self.startX
        self.position["y"] = event.y_root - self.startY
        self.place(x=self.position["x"], y=self.position["y"])
