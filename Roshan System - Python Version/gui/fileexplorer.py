from gui.window import WindowPackManager
import customtkinter as ctk
from tkinter import StringVar
from typing import Callable
import os

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark") 

class FileExplorer(WindowPackManager):
    def __init__(self, master):
        super().__init__(master, "File Explorer", (600, 400), "textures/filexplorer.png")
        self.toolbar = ctk.CTkFrame(self)
        self.toolbar.pack(side="top", fill="x")
        self.main = ctk.CTkScrollableFrame(self)
        self.main.pack(side="top", fill="both", expand=True)
        initial_path = "user_dir"
        if not os.path.exists(initial_path):
            os.makedirs(initial_path)
        self.folder = StringVar(value=initial_path)
        self.last_folder = StringVar()
        self.image_exts = (".png", ".jpg", ".jpeg", ".ico", ".gif", ".bmp")
        self.open_folder(initial_path, "")
        self.backbtn = ctk.CTkButton(
            self.toolbar,
            text="<- Back",
            command=lambda: self.open_folder(self.last_folder.get(), self.folder.get()),
        )
        self.backbtn.pack(side="left")
        ctk.CTkEntry(self.toolbar, textvariable=self.folder).pack(
            side="left", fill="x", expand=True
        )
        ctk.CTkButton(
            self.toolbar,
            text="Go ->",
            command=lambda: self.open_folder(self.folder.get(), self.last_folder.get()),
        ).pack(side="left")

    def open_folder(self, filepath, last_filepath):
        for widget in self.main.winfo_children():
            widget.destroy()

        self.last_folder.set(last_filepath)
        self.folder.set(filepath)

        for file in os.listdir(filepath):
            full_path = os.path.join(filepath, file)
            if os.path.isdir(full_path):
                ctk.CTkButton(
                    self.main,
                    text=f"📁 {file}",
                    command=lambda f=full_path: self.open_folder(f, filepath),
                ).pack(side="top", fill="x", pady=2)
            elif file.lower().endswith(".txt"):
                ctk.CTkButton(
                    self.main,
                    text=f"📄 {file}",
                    command=lambda f=full_path: self.open_file(f),
                ).pack(side="top", fill="x", pady=2)
            elif file.lower().endswith(self.image_exts):
                ctk.CTkButton(
                    self.main,
                    text=f"🖼️ {file}",
                    command=lambda f=full_path: self.open_file(f),
                ).pack(side="top", fill="x", pady=2)

    def open_file(self, filepath):
        if filepath.endswith(".txt"):
            from gui.notepad import Notepad

            self.notepad = Notepad(self.master)
            with open(filepath, "r") as f:
                self.notepad.set_text(f.read())
            self.notepad.place(x=70, y=70)
            self.notepad.lift()
        if filepath.endswith(self.image_exts):
            from gui.imageviewer import ImageViewer

            self.imageviewer = ImageViewer(self.master)

            self.imageviewer.set_image(filepath)
            self.imageviewer.place(x=70, y=70)
            self.imageviewer.lift()


class SaveAsFilename(WindowPackManager):
    def __init__(self, master, filetype: tuple[str, ...] | str, callback: Callable):
        super().__init__(master, title=f"Save {filetype} file", size=(600, 300))
        self.place(x=60, y=60)
        self.filetype = filetype
        self.callback = callback
        self.toolbar = ctk.CTkFrame(self)
        self.toolbar.pack(side="top", fill="x")
        self.contentsframe = ctk.CTkScrollableFrame(self)
        self.contentsframe.pack(side="top", fill="both")
        self.folder = StringVar(value="user_dir")
        self.last_folder = StringVar()
        self.bottomframe = ctk.CTkFrame(self)
        self.bottomframe.pack(side="bottom", fill="x")
        self.filename = StringVar()
        self.open_folder("user_dir", "")
        self.backbtn = ctk.CTkButton(
            self.toolbar,
            text="<- Back",
            command=lambda: self.open_folder(self.last_folder.get(), self.folder.get()),
        )
        self.backbtn.pack(side="left")
        ctk.CTkEntry(self.toolbar, textvariable=self.folder).pack(
            side="left", fill="x", expand=True
        )
        ctk.CTkButton(
            self.toolbar,
            text="Go ->",
            command=lambda: self.open_folder(self.folder.get(), self.last_folder.get()),
        ).pack(side="left")
        ctk.CTkButton(self.bottomframe, text="Cancel", command=self.destroy).pack(
            side="left"
        )
        ctk.CTkLabel(self.bottomframe, text=f"Filename: ").pack(side="left")
        ctk.CTkEntry(self.bottomframe, textvariable=self.filename).pack(
            side="left", fill="x", expand=True
        )
        ctk.CTkButton(self.bottomframe, text="Save", command=self.prefrom_save).pack(
            side="left"
        )

    def open_folder(self, filepath, last_filepath):
        for widget in self.contentsframe.winfo_children():
            widget.destroy()
        self.folder.set(filepath)
        self.last_folder.set(last_filepath)
        for file in os.listdir(filepath):
            if os.path.isdir(os.path.join("user_dir", file)):
                full_path = os.path.join("user_dir", file)
                ctk.CTkButton(
                    self.contentsframe,
                    text=f"Folder: {file}",
                    command=lambda f=full_path: self.open_folder(f, filepath),
                ).pack(side="top", fill="x", pady=2)
            if file.endswith(self.filetype):
                ctk.CTkButton(
                    self.contentsframe,
                    text=f"{self.filetype}: {file}",
                    command=lambda f=file: self.filename.set(f),
                ).pack(side="top", fill="x", pady=2)

    def prefrom_save(self):
        self.callback(os.path.join(self.folder.get(), self.filename.get()))


class OpenAsFilename(WindowPackManager):
    def __init__(self, master, filetype: tuple[str, ...] | str, callback: Callable):
        super().__init__(master, f"Open {filetype} file", (600, 400))
        self.place(x=60, y=60)
        self.filetype = filetype
        self.callback = callback
        self.toolbar = ctk.CTkFrame(self)
        self.toolbar.pack(side="top", fill="x")
        self.contentsframe = ctk.CTkScrollableFrame(self)
        self.contentsframe.pack(side="top", fill="both")
        self.folder = StringVar(value="user_dir")
        self.last_folder = StringVar()
        self.bottomframe = ctk.CTkFrame(self)
        self.bottomframe.pack(side="bottom", fill="x")
        self.filename = StringVar()
        self.open_folder("user_dir", "")
        self.backbtn = ctk.CTkButton(
            self.toolbar,
            text="<- Back",
            command=lambda: self.open_folder(self.last_folder.get(), self.folder.get()),
        )
        self.backbtn.pack(side="left")
        ctk.CTkEntry(self.toolbar, textvariable=self.folder).pack(
            side="left", fill="x", expand=True
        )
        ctk.CTkButton(
            self.toolbar,
            text="Go ->",
            command=lambda: self.open_folder(self.folder.get(), self.last_folder.get()),
        ).pack(side="left")
        ctk.CTkButton(self.bottomframe, text="Cancel", command=self.destroy).pack(
            side="left"
        )
        ctk.CTkLabel(self.bottomframe, text=f"Filename: ").pack(side="left")
        ctk.CTkEntry(self.bottomframe, textvariable=self.filename).pack(
            side="left", fill="x", expand=True
        )
        ctk.CTkButton(self.bottomframe, text="Open", command=self.prefrom_save).pack(
            side="left"
        )

    def open_folder(self, filepath, last_filepath):
        for widget in self.contentsframe.winfo_children():
            widget.destroy()
        self.folder.set(filepath)
        self.last_folder.set(last_filepath)
        for file in os.listdir(filepath):
            if os.path.isdir(os.path.join("user_dir", file)):
                full_path = os.path.join("user_dir", file)
                ctk.CTkButton(
                    self.contentsframe,
                    text=f"Folder: {file}",
                    command=lambda f=full_path: self.open_folder(f, filepath),
                ).pack(side="top", fill="x", pady=2)
            if file.endswith(self.filetype):
                ctk.CTkButton(
                    self.contentsframe,
                    text=f"{self.filetype}: {file}",
                    command=lambda f=file: self.filename.set(f),
                ).pack(side="top", fill="x", pady=2)

    def prefrom_save(self):
        self.callback(os.path.join(self.folder.get(), self.filename.get()))
