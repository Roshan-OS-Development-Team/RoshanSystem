//
// Created by Roshan on 13/09/2026.
//

#include "filedialog.h"

namespace core
{
    SaveFileDialog::SaveFileDialog(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback):
    Window(parent, "Save a file", {960, 480}, "textures/explorer.png"), _fileExtensions(fileExtensions), _cb(callback)
    {
        this->filePages = new QWidget(this);
        this->filePages->setGeometry(10, 60, this->width() - 20, this->height() - 70);
        this->filePagesLayout = new QVBoxLayout(this->filePages);
        styles = core::get_qss_styles("styling/filedialog");
        this->makeGUI("user_dir");
    }

    bool SaveFileDialog::checkExtension(const std::string& fileName)
    {
        for (std::string& fileExtension: _fileExtensions)
        {
            if (fileName.ends_with(fileExtension))
            {
                return true;
            }
            else
            {
                continue;
            }
        }

        return false;
    }

    void SaveFileDialog::makeGUI(std::string path)
    {
        fs::path _path = path;

        for (QPushButton *btn: this->filePages->findChildren<QPushButton*>())
        {
            btn->deleteLater();
        }

        for (auto file : fs::directory_iterator(_path))
        {
            if (file.is_directory())
            {
                auto *FolderBtn = new QPushButton(this->filePages);
                FolderBtn->setText(QString::fromStdString(file.path().filename().stem().string()));
                this->connect(FolderBtn, &QPushButton::clicked, [this, file]()
                {
                   this->makeGUI(file.path().string());
                });
                FolderBtn->setStyleSheet(QString::fromStdString(this->styles["button"]));
                this->filePagesLayout->addWidget(FolderBtn);
            }
            else
            {
                if (checkExtension(file.path().filename().string()))
                {
                    auto *FileBtn = new QPushButton(this->filePages);
                    FileBtn->setText(QString::fromStdString(file.path().filename().string()));
                    FileBtn->setStyleSheet(QString::fromStdString(this->styles["button"]));
                }
            }
        }
    }
}

ROSHANSYSTEMLIB_API core::SaveFileDialog* createSaveFileDialog(QWidget* parent, const char* fileExtensions[], int fileExtensionCount, callbackFunction* callbackFunction)
{
    std::vector<std::string> _fileExtensions;

    for (int index = 0; index <= fileExtensionCount - 1; ++index)
    {
        std::string temp(fileExtensions[index]);
        _fileExtensions.push_back(temp);
    }

    return new core::SaveFileDialog(parent, _fileExtensions, callbackFunction);
}
