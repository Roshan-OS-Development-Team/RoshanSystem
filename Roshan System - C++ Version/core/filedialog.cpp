//
// Created by Roshan on 13/09/2026.
//

#include <filesystem>
#include <qboxlayout.h>
#include <qobject.h>
#include <qpushbutton.h>
#include <qwidget.h>
#include <string>
#include <vector>

#include "filedialog.h"

namespace fs = std::filesystem;

namespace core
{
    SaveFileDialog::SaveFileDialog(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback):
    Window(parent, "Save a file", {960, 480}, "textures/explorer.png"), _fileExtensions(fileExtensions), _cb(callback)
    {
        this->filePages = new QWidget(this);
        this->filePages->setGeometry(10, 60, this->width() - 20, this->height() - 120);
        this->filePagesLayout = new QVBoxLayout(this->filePages);
        styles = core::get_qss_styles("styling/filedialog");
        this->makeGUI("user_dir");
    }

    bool SaveFileDialog::checkExtension(const std::string& fileName)
    {
        for (const std::string& fileExtension: _fileExtensions)
        {
            if (fileName.ends_with(fileExtension))
            {
                return true;
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
                    this->filePagesLayout->addWidget(FileBtn);
                }
            }
        }
    }

    OpenFileDialog::OpenFileDialog(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callbackFunction):
    _fileExtensions(fileExtensions), _cb(callbackFunction)
    {
        styles = core::get_qss_styles("styling/filedialog");
        filePages = new QWidget(this);
        filePages->setGeometry(10, 50, this->width() - 20, this->height() - 110);
        filePagesLayout = new QVBoxLayout(filePages);
        this->makeGUI("user_dir");
    }

    bool OpenFileDialog::checkExtension(const std::string& fileName)
    {
        for (const std::string& fileExtension: _fileExtensions)
        {
            if (fileName.ends_with(fileExtension))
            {
                return true;
            }
        }

        return false;
    }

    void OpenFileDialog::makeGUI(std::string path)
    {
        for (QPushButton* btn: filePages->findChildren<QPushButton*>())
        {
            btn->deleteLater();
        }

        fs::path filePath = path;

        for (auto file: fs::directory_iterator(filePath)) 
        {
            if (file.is_directory()) 
            {
                auto *folderBtn = new QPushButton(QString::fromStdString(file.path().stem().string()), filePages);
                folderBtn->setStyleSheet(QString::fromStdString(styles["button"]));
                this->connect(folderBtn, &QPushButton::clicked, [this, file]()
                {
                    this->makeGUI(file.path().string());
                });
                filePagesLayout->addWidget(folderBtn);
            }
            else
            {
                auto *fileBtn = new QPushButton(QString::fromStdString(file.path().stem().string()), this);
                fileBtn->setStyleSheet(QString::fromStdString(styles["button"]));
                filePagesLayout->addWidget(fileBtn);
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