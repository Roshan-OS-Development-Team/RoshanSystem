from PIL import Image
import customtkinter as ctk
from gui.window import WindowPackManager


class ImageViewer(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "Image Viewer", (640, 360))
        self.imglabel = ctk.CTkLabel(self)
        self.imglabel.pack(side="top", fill="both")
