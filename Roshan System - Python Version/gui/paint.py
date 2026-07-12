__lazy_modules: tuple[str, ...] = (
    "gui.window",
)

from gui.window import WindowPackManager
import customtkinter as ctk
from tkinter import StringVar
from PIL import Image, ImageDraw

class Paint(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "Paint", (960, 480), "textures/paint.png")
        self.colors_frame = ctk.CTkFrame(self)
        self.colors_frame.pack(side="top", fill="x", pady=5)
        self.color = StringVar(value="black")
        self.colors: list[str] = [
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Purple",
            "Violet",
            "Black",
            "White",
            "Gray"
        ]
        row: int = 0
        column: int = 0

        self.canvas = ctk.CTkCanvas(self)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.update_idletasks()

        self.image = Image.new(
            "RGB",
            (self.canvas.winfo_width(), self.canvas.winfo_height())
        )

        self.draw = ImageDraw.Draw(self.image)

        for i in range(len(self.colors)):
            ctk.CTkButton(
                self.colors_frame,
                text="",
                fg_color=self.colors[i],
                command=lambda color=self.colors[i]: self.color.set(color),
                hover_color=self.colors[i],
                width=50,
                height=50
            ).grid(
                row=row,
                column=column,
                padx=5,
                pady=5
            )

            column += 1

            if column == 5:
                column = 0
                row += 1

        self.canvas.bind("<Button-1>", self.paint)
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        self.canvas.create_oval(
            event.x - 3,
            event.y - 3,
            event.x + 3,
            event.y + 3,
            fill=self.color.get(),
            outline=self.color.get()
        )
        self.draw.ellipse(
            [
                event.x - 3,
                event.y - 3,
                event.x + 3,
                event.y + 3,
            ],
            fill=self.color.get(),
            outline=self.color.get()
        )

if __name__ == '__main__':
    root = ctk.CTk()
    root.title("Paint")
    root.geometry("960x480")
    Paint(root).place(x=0, y=0)
    root.mainloop()
