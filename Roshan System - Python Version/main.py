from PIL import Image, ImageTk
from messagebox import MessageBoxYesNo
import customtkinter as ctk
import os
from tkinter import PhotoImage
from gui.taskbar import Taskbar
from gui.notepad import Notepad
from gui.startmenu import StartMenu
from gui.fileexplorer import FileExplorer
from gui.imageviewer import ImageViewer
from gui.calculator import Calculator
from gui.window import WindowPackManager
from gui.paint import  Paint

os.chdir(os.path.abspath(os.path.dirname(__file__)))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roshan System")
        self.attributes("-fullscreen", True)
        self.geometry("1200x800")
        self.update_idletasks()
        self.protocol("WM_DELETE_WINDOW", self.shutdown)
        self.backgroundimg = Image.open("textures/background7.png")
        self.backgroundctk = ctk.CTkImage(self.backgroundimg, size=(self.winfo_width(), self.winfo_height()))
        self.background = ctk.CTkLabel(self, text="", image=self.backgroundctk)
        self.background.pack(fill="both", side="top")
        self.bind("<Configure>", self.resize_background)
        if not os.path.exists("user_dir"):
            os.makedirs("user_dir")
        self.taskbar = Taskbar(
            self.background,
            width=self.winfo_width(),
            corner_radius=50,
        )

        # Start Menu Stuff
        startbtnimg = Image.open("textures/startmenu.png")
        startbtnimgctk = ctk.CTkImage(startbtnimg, size=(70, 70))
        self.startbtn = ctk.CTkButton(
            self.taskbar,
            image=startbtnimgctk,
            text="",
            bg_color="transparent",
            fg_color="transparent",
            width=70,
            height=70,
            hover_color="#353434",
            command=self.toggle_start_menu,
        )
        self.startbtn.pack(side="left")
        self.startmenu = StartMenu(self.background)
        self.startmenuopened = False

        # Notepad Stuff
        notepadimg = Image.open("textures/notepad.png")
        notepadimgctk = ctk.CTkImage(notepadimg, size=(40, 51))
        self.notepadbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            image=notepadimgctk,
            width=70,
            height=70,
            hover_color="#353434",
            text="",
            fg_color="transparent",
            bg_color="transparent",
            command=lambda: self.open_app(self.notepad),
        )
        self.notepadbtn.pack(side="left")
        self.notepad = Notepad(self)

        # Calculator Stuff
        calculatorimage = Image.open("textures/calculator.png")
        calculatorimagectk = ctk.CTkImage(calculatorimage, size=(36, 52))
        self.calculator = Calculator(self)
        self.calculatorbtn = ctk.CTkButton(
            self.taskbar,
            text="",
            fg_color="transparent",
            bg_color="transparent",
            hover_color="#343435",
            image=calculatorimagectk,
            width=70,
            height=70,
            command=lambda: self.open_app(self.calculator),
        )
        self.calculatorbtn.pack(side="left")

        # File Explorer Stuff
        fileexplorerimg = Image.open("textures/filexplorer.png")
        fileexplorerimgctk = ctk.CTkImage(fileexplorerimg, size=(60, 60))
        self.fileexplorerbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            image=fileexplorerimgctk,
            width=70,
            height=70,
            hover_color="#343435",
            text="",
            bg_color="transparent",
            fg_color="transparent",
            command=lambda: self.open_app(self.fileexplorer),
        )
        self.fileexplorerbtn.pack(side="left")
        self.fileexplorer = FileExplorer(self)

        # Image Viewer Stuff
        imageviewerimg = Image.open("textures/imageviewer.png")
        imageviewerimgctk = ctk.CTkImage(imageviewerimg, imageviewerimg, size=(70, 70))
        self.imageviewer = ImageViewer(self)
        self.imageviewerbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            width=70,
            height=70,
            hover_color="#343435",
            text="",
            bg_color="transparent",
            fg_color="transparent",
            image=imageviewerimgctk,
            command=lambda: self.open_app(self.imageviewer),
        )
        self.imageviewerbtn.pack(side="left")

        paintimg = Image.open("textures/Paint.png")
        paintimgctk = ctk.CTkImage(paintimg, size=(70, 70))
        self.paint = Paint(self)

        self.paintbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            width=70,
            height=70,
            hover_color="#343435",
            text="",
            bg_color="transparent",
            fg_color="transparent",
            image=paintimgctk,
            command=lambda: self.open_app(self.paint)
        )
        self.paintbtn.pack(
            side="left"
        )

        self.ctrl_panel = self.create_ctrl_panel()
        ctrl_panel_img = Image.open("textures/ctrlpanel.png")
        ctrl_panel_img_ctk = ctk.CTkImage(ctrl_panel_img, size=(70, 70))
        self.ctrl_panel_btn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            width=70,
            height=70,
            hover_color="#343435",
            text="",
            bg_color="transparent",
            fg_color="transparent",
            image=ctrl_panel_img_ctk,
            command=lambda: self.open_app(self.ctrl_panel)
        )
        self.ctrl_panel_btn.pack(
            side="left"
        )

        shutdownimg = Image.open("textures/closeicon.png")
        shutdownimgctk = ctk.CTkImage(shutdownimg, size=(70, 70))
        self.shutdownbtn = ctk.CTkButton(
            self.taskbar,
            border_width=0,
            width=70,
            height=70,
            hover_color="#343435",
            text="",
            bg_color="transparent",
            fg_color="transparent",
            image=shutdownimgctk,
            command=self.shutdown,
        )
        self.shutdownbtn.pack(side="left")

        self.startmenuio = ctk.CTkFrame(self, width=50, height=410)
        self.startmenuio.pack_propagate(False)

    @staticmethod
    def open_app(app: WindowPackManager):
        app.place(x=app.position["x"], y=app.position["y"])
        app.lift()

    def resize_background(self, event):
        if event.widget == self:
            self.backgroundctk.configure(size=(self.winfo_width(), self.winfo_height()))
            self.background.configure(image=self.backgroundctk)
            self.taskbar.configure(width=self.winfo_width(), height=70)
            self.taskbar.pack_propagate(False)
            self.taskbar.place(x=0, y=self.winfo_height() - 70)

    def toggle_start_menu(self):
        if not self.startmenuopened:
            self.startmenu.place(x=50, y=self.winfo_height() - 480)
            self.startmenuio.place(x=0, y=self.winfo_height() - 480)
            self.startmenuopened = True
        else:
            self.startmenu.place_forget()
            self.startmenuio.place_forget()
            self.startmenuopened = False

    def _shutdown(self):
        self.destroy()

    def shutdown(self):
        ShutdownMsgBox = MessageBoxYesNo(
            self,
            "Shutdown",
            "Are you sure you want to shutdown",
            self._shutdown,
            image="textures/information.png"
        )
        ShutdownMsgBox.place(x=60, y=60)
        
    def change_background(self, filepath: str):
        self.backgroundimg = Image.open(filepath)
        self.backgroundctk = ctk.CTkImage(self.backgroundimg, size=(self.winfo_width(), self.winfo_height()))
        self.background.configure(image=self.backgroundctk)

    def create_ctrl_panel(self) -> WindowPackManager:
        ctrl_panel = WindowPackManager(self, "Control Panel", (960, 480), "textures/ctrlpanel.png")

        tabs = ctk.CTkTabview(ctrl_panel)

        tabs_list: list[str] = ["Personalization", "Preferences"]

        for tab in tabs_list:
            tabs.add(tab)

        personalization_tab = ctk.CTkScrollableFrame(tabs.tab("Personalization"))
        personalization_tab.pack(fill="both", expand=True)

        background_choices = None

        def _change_appearance_mode(appearance_mode: str):
            if appearance_mode == "Light":
                for btn in self.taskbar.winfo_children():
                    if type(btn) == ctk.CTkButton:
                        btn.configure(hover_color="#b8b8b8")

                if background_choices:
                    for btn in background_choices.winfo_children():
                        if type(btn) == ctk.CTkButton:
                            btn.configure(hover_color="#b8b8b8")

                ctk.set_appearance_mode(appearance_mode)

                ctk.set_appearance_mode(appearance_mode)
            elif appearance_mode == "Dark":
                for btn in self.taskbar.winfo_children():
                    if type(btn) == ctk.CTkButton:
                        btn.configure(hover_color="#343435")

                if background_choices:
                    for btn in background_choices.winfo_children():
                        if type(btn) == ctk.CTkButton:
                            btn.configure(hover_color="#343435")

                ctk.set_appearance_mode(appearance_mode)

        ctk.CTkOptionMenu(
            master=personalization_tab,
            values=["Dark", "Light"],
            command=_change_appearance_mode
        ).pack(
            side="top",
            pady=5,
            padx=5
        )

        background_choices = ctk.CTkFrame(personalization_tab)
        background_choices.pack(side="top")

        row_num: int = 0
        column_num: int = 0
        background_num: int = 0

        for file in os.listdir("textures"):
            if "background" in file:
                file_path = f"textures/background{background_num}.png"
                img = Image.open(file_path)
                img.thumbnail(size=(100, 100))
                imgctk = ctk.CTkImage(img, size=img.size)
                ctk.CTkButton(
                    background_choices,
                    text="",
                    fg_color="transparent",
                    hover_color="#343435",
                    image=imgctk,
                    width=100,
                    height=100,
                    command=lambda background = file_path: self.change_background(background)
                ).grid(
                    row=row_num,
                    column=column_num
                )
                column_num += 1
                background_num += 1
            if column_num == 5:
                row_num += 1
                column_num = 0

        preferences_frame = ctk.CTkScrollableFrame(tabs.tab("Preferences"))
        preferences_frame.pack(fill="both", expand=True)

        shutdown_var = ctk.BooleanVar(value=False)

        def _messagebox_shutdown():
            if shutdown_var.get() == True:
                self.shutdownbtn.configure(command=self.shutdown)
                self.protocol("WM_DELETE_WINDOW", self.shutdown)
            elif shutdown_var.get() == False:
                self.shutdownbtn.configure(command=self._shutdown)
                self.protocol("WM_DELETE_WINDOW", self._shutdown)

        messagebox_shutdown_switch = ctk.CTkSwitch(
            preferences_frame,
            text="Toggle Messagebox Shutdown",
            variable=shutdown_var,
            command=_messagebox_shutdown
        )
        messagebox_shutdown_switch.select()
        messagebox_shutdown_switch.pack(side="top")

        fullscreen_var = ctk.BooleanVar(value=False)

        def _fullscreen():
            if not fullscreen_var.get():
                self.attributes("-fullscreen", False)
                self.winico = PhotoImage(file="textures/startmenu.png")
                self.iconphoto(False, self.winico)
            elif fullscreen_var.get():
                self.attributes("-fullscreen", True)
                self.winico = PhotoImage(file="textures/startmenu.png")
                self.iconphoto(False, self.winico)

        fullscreen_switch = ctk.CTkSwitch(
            preferences_frame,
            text="Toggle Fullscreen",
            variable=fullscreen_var,
            command=_fullscreen
        )

        fullscreen_switch.select()
        fullscreen_switch.pack(side="top")

        tabs.pack(fill="both", expand=True)

        return ctrl_panel

if __name__ == "__main__":
    root = App()
    root.mainloop()
