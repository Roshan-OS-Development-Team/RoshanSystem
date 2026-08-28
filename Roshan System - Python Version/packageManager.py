import json
import os
import shutil
from urllib.parse import unquote

import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

import core

style = core.get_qss_styles("styling/packageManager")


class PackageManger(core.Window):
    def __init__(self, master):
        super().__init__(
            master, "Package Manager", (960, 480), "textures/packagemanager.png"
        )
        self.packages = requests.get(
            "https://raw.githubusercontent.com/Roshan-OS-Development-Team/packages/main/packages.json"
        )

        self.packages.raise_for_status()

        self.packagesJSON = self.packages.json()

        if (
            os.path.exists("installed_packages.json")
            and os.path.getsize("installed_packages.json") > 0
        ):
            with open("installed_packages.json") as f:
                self.installedPackages = json.load(f)
        else:
            self.installedPackages = []

        self.tabView = QTabWidget(self)
        self.tabView.setGeometry(10, 50, self.width() - 20, self.height() - 70)

        self.appsTab = QScrollArea(self.tabView)
        self.appsTab.setWidgetResizable(True)
        self.appsTabWidget = QWidget(self.appsTab)
        self.appsTabLayout = QVBoxLayout(self.appsTabWidget)
        self.appsTabLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.appsTab.setWidget(self.appsTabWidget)
        self.appsTab.setStyleSheet(style["appbar"])

        self.tabView.addTab(self.appsTab, "Apps")

        for packageName in self.packagesJSON:
            packageJSON = self.packagesJSON[packageName]
            isPackageInstalled = packageName in self.installedPackages and os.path.splitext(os.path.basename(unquote(packageJSON["download_link"])))[0] in os.listdir("packages")
            appBar = QWidget()
            appBar.setStyleSheet(style["appbar"])
            appBarLayout = QHBoxLayout(appBar)
            appMetadata = QLabel(appBar)
            appMetadata.setText(
                f"Name: {packageName}\n"
                f"Author: {packageJSON['author']}\n"
                f"Version: {packageJSON['version']}\n"
                f"Description: {packageJSON['description']}"
            )
            appBarLayout.addWidget(appMetadata)
            appBar.setFixedHeight(4 * 26)
            actionsPanel = QWidget()
            actionsPanel.setFixedWidth(200)
            actionsPanelLayout = QVBoxLayout(actionsPanel)
            appBarLayout.addWidget(actionsPanel)

            installOrUninstallBtn = QPushButton(actionsPanel)
            installOrUninstallBtn.setStyleSheet(
                style["uninstallbtn"] if isPackageInstalled else style["installbtn"]
            )
            installOrUninstallBtn.setText(
                "Uninstall" if isPackageInstalled else "Install"
            )

            actionsPanelLayout.addWidget(installOrUninstallBtn)
            match packageJSON["type"].lower():
                case "app":
                    if isPackageInstalled:
                        installOrUninstallBtn.clicked.connect(
                            lambda checked, app=packageName: self.uninstallApp(app)
                        )
                    else:
                        installOrUninstallBtn.clicked.connect(
                            lambda checked, app=packageName: self.installApp(app)
                        )
                    self.appsTabLayout.addWidget(appBar)

    def installApp(self, app: str):
        appRequest = requests.get(self.packagesJSON[app]["download_link"])
        appRequest.raise_for_status()
        with open("temp.zip", "wb") as f:
            f.write(appRequest.content)

        shutil.unpack_archive("temp.zip", "packages")
        os.remove("temp.zip")
        if app in self.installedPackages:
            self.installedPackages.remove(app)
        self.installedPackages.append(app)
        with open("installed_packages.json", "w") as f:
            json.dump(self.installedPackages, f)

    def uninstallApp(self, app: str):
        shutil.rmtree(f"packages/{app}")
        self.installedPackages.remove(app)
        with open("installed_packages.json", "w") as f:
            json.dump(self.installedPackages, f)


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.resize(960, 480)
    packageManager = PackageManger(win)
    packageManager.show()
    win.show()
    app.exec()
