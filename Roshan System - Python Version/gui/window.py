import customtkinter as ctk
from PIL import Image

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

class WindowPackManager(ctk.CTkFrame):
    """A window that uses the pack manager,
    You need to input the title,
    Inputting size is optional"""

    def __init__(
            self,
            master,
            title: str,
            size: tuple[int, int] | None = None,
            icon_path: str | None = None
    ):
        super().__init__(master)
        if size is not None:
            self.pack_propagate(False)
            self.configure(width=size[0], height=size[1])
        self.title_bar_frame = ctk.CTkFrame(self)
        self.title_bar_frame.pack(side="top", fill="x")

        if icon_path is not None:
            icon_img = Image.open(icon_path)
            icon_img.thumbnail((20, 20))
            icon_img_ctk = ctk.CTkImage(icon_img, size=icon_img.size)

            ctk.CTkLabel(
                self.title_bar_frame,
                text="",
                fg_color="transparent",
                image=icon_img_ctk,
                width=20,
                height=20
            ).pack(
                side="left",
                padx=2
            )

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

        self.startX: int = 0
        self.startY: int = 0

    def start_drag(self, event):
        self.startX = event.x_root - self.winfo_x()
        self.startY = event.y_root - self.winfo_y()
        self.lift()

    def do_drag(self, event):
        self.position["x"] = event.x_root - self.startX
        self.position["y"] = event.y_root - self.startY
        self.place(x=self.position["x"], y=self.position["y"])
