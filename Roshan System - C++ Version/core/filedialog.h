//
// Created by Roshan on 13/09/2026.
//

#ifdef RoshanSystemCoreLib_EXPORTS
#define ROSHANSYSTEMLIB_API __declspec(dllexport)
#else
#define ROSHANSYSTEMLIB_API __declspec(dllimport)
#endif

#include "window.h"

#include <QWidget>
#include <vector>
#include <string>
#include <QPushButton>
#include <QVBoxLayout>
#include <filesystem>

namespace fs = std::filesystem;

typedef void callbackFunction(std::string filename);

#ifndef ROSHANSYSTEM_FILEDIALOG_H
#define ROSHANSYSTEM_FILEDIALOG_H

namespace core
{
    class SaveFileDialong: public Window
    {
    public:
        SaveFileDialong(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback);
    };
}

#endif //ROSHANSYSTEM_FILEDIALOG_H
