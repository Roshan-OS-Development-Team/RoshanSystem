//
// Created by Roshan on 13/09/2026.
//

#define RoshanSystemCoreLib_EXPORTS

#include "filedialog.h"

namespace core
{
    SaveFileDialong::SaveFileDialong(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback):
    Window(parent, "Save a file", {960, 480}, "textures/fileexplorer.png")

    {
    }
}
