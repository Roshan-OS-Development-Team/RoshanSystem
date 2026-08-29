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


class PackageManager(core.Window):
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

        self.runAppsTab = QScrollArea(self.tabView)
        self.runAppsTab.setWidgetResizable(True)
        self.runAppsTabWidget = QWidget(self.appsTab)
        self.runAppsTabLayout = QVBoxLayout(self.runAppsTabWidget)
        self.runAppsTabLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.runAppsTab.setWidget(self.runAppsTabWidget)
        self.runAppsTab.setStyleSheet(style["appbar"])

        self.tabView.addTab(self.runAppsTab, "Run Apps")

        self.drawGUI()

    def drawGUI(self):

        for children in self.appsTabWidget.findChildren(QWidget):
            children.deleteLater()

        for packageName in self.packagesJSON:
            packageJSON = self.packagesJSON[packageName]
            isPackageInstalled = (
                packageName in self.installedPackages
                and os.path.splitext(
                    os.path.basename(unquote(packageJSON["download_link"]))
                )[0]
                in os.listdir("packages")
            )
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
                case "run_app":
                    if isPackageInstalled:
                        installOrUninstallBtn.clicked.connect(
                            lambda checked, app=packageName: self.uninstallRunApp(app)
                        )
                    else:
                        installOrUninstallBtn.clicked.connect(
                            lambda checked, app=packageName: self.installRunApp(app)
                        )
                    self.runAppsTabLayout.addWidget(appBar)

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
            json.dump(self.installedPackages, f, indent=4)

        with open("apps.json", "r") as f:
            appsJSON = json.load(f)

        appsJSON[app] = {
            "module": f"packages.{app}.{os.path.splitext(self.packagesJSON[app]['main_app_file'])[0]}",
            "class_or_func": self.packagesJSON[app]["main_app_class"],
            "startmenu_btn": self.packagesJSON[app]["startmenu_btn"],
            "taskbar_btn": self.packagesJSON[app]["taskbar_btn"],
            "icon": f"packages/{app}/{self.packagesJSON[app]['main_app_icon']}",
        }

        with open("apps.json", "w") as f:
            json.dump(appsJSON, f, indent=4)

        self.drawGUI()

    def uninstallApp(self, app: str):
        shutil.rmtree(f"packages/{app}")
        self.installedPackages.remove(app)
        with open("installed_packages.json", "w") as f:
            json.dump(self.installedPackages, f, indent=4)

        with open("apps.json", "r") as f:
            appsJSON: dict = json.load(f)

        appsJSON.pop(app)

        with open("apps.json", "w") as f:
            json.dump(dict(sorted(appsJSON)), f, indent=4)

        self.drawGUI()

    def installRunApp(self, app: str):
        appRequest = requests.get(self.packagesJSON[app]["download_link"])
        appRequest.raise_for_status()

        with open("temp.zip", "wb") as f:
            f.write(appRequest.content)

        shutil.unpack_archive("temp.zip", "packages")
        os.remove("temp.zip")

        self.installedPackages.append(app)

        with open("installed_packages.json", "w") as f:
            json.dump(self.installedPackages, f, indent=4)

        with open("run_apps/run_apps.json", "r") as f:
            runAppsJSON = json.load(f)  # I think this loads the run apps ig?

        runAppsJSON[app] = {
            "module": f"packages.{app}.{os.path.splitext(self.packagesJSON[app]['main_app_file'])[0]}",
            "class_or_func": self.packagesJSON[app]["main_app_class"],
        }

        with open("run_apps/run_apps.json", "w") as f:
            json.dump(runAppsJSON, f, indent=4)

        self.drawGUI()

    def uninstallRunApp(self, app: str):
        shutil.rmtree(f"packages/{app}")
        self.installedPackages.remove(app)

        with open("installed_packages.json", "w") as f:
            json.dump(self.installedPackages, f, indent=4)

        with open("run_apps/run_apps.json", "r") as f:
            runAppsJSON: dict = json.load(f)

        runAppsJSON.pop(app)

        with open("run_apps/run_apps.json", "w") as f:
            json.dump(runAppsJSON, f, indent=4)


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.resize(960, 480)
    packageManager = PackageManager(win)
    packageManager.show()
    win.show()
    app.exec()
