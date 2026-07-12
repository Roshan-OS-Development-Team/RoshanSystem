__lazy_modules__: tuple[str, ...] = (
    "gui.fileexplorer",
    "gui.window"
)

from PIL import Image
import customtkinter as ctk
from gui.fileexplorer import OpenAsFilename
from gui.window import WindowPackManager

class ImageViewer(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "Image Viewer", (600, 400), "textures/imageviewer.png")
        self.toolbarframe = ctk.CTkFrame(self)
        self.toolbarframe.pack(side="top", fill="x")
        self.open_image_btn = ctk.CTkButton(
            self.toolbarframe, text="Open Image", command=self.open_image
        )
        self.open_image_btn.pack(side="left")
        self.imglabel = ctk.CTkLabel(self, text="")
        self.imglabel.pack(side="top", fill="both", expand=True)

    def open_image(self):
        OpenAsFilename(
            self.master,
            (".png", ".jpg", ".jpeg", ".ico", ".gif", ".bmp"),
            self.preform_open_image,
        )

    def preform_open_image(self, filename):
        img = Image.open(filename)
        img.thumbnail((600, 400))
        ctkimg = ctk.CTkImage(img, size=img.size)
        self.imglabel.configure(image=ctkimg)

    def set_image(self, filename):
        img = Image.open(filename)
        img.thumbnail((600, 400))
        ctkimg = ctk.CTkImage(img, size=img.size)
        self.imglabel.configure(image=ctkimg)
