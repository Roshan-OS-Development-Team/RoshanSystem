//
// Created by Roshan on 13/09/2026.
//

#define RoshanSystemCoreLib_EXPORTS

#include "filedialog.h"

namespace core
{
    SaveFileDialong::SaveFileDialong(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback):
    Window(parent, "Save a file", {960, 480}, "textures/fileexplorer.png"), _fileExtensions(fileExtensions), _cb(callback)
    {
        filePages = new QWidget(this);
        filePages->setGeometry(10, 60, this->width() - 20, this->height() - 70);
        filePagesLayout = new QVBoxLayout(filePages);
        styles = core::get_qss_styles("styling/filedialog");
    }

    void SaveFileDialong::makeGUI(std::string path)
    {
        fs::path _path = path;

        for (auto file : fs::directory_iterator(_path))
        {
            
        }
    }
}
