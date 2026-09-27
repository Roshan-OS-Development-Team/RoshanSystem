//
// Created by Roshan on 13/09/2026.
//

#ifdef ROSHANSYSTEMLIB_API
#undef ROSHANSYSTEMLIB_API
#endif

#ifdef RoshanSystemCoreLib_EXPORTS
#ifdef _WIN32
#define ROSHANSYSTEMLIB_API extern "C" __declspec(dllexport)
#endif
#else
#define ROSHANSYSTEMLIB_API extern "C"
#endif

#ifndef ROSHANSYSTEM_FILEDIALOG_H
#define ROSHANSYSTEM_FILEDIALOG_H

#include "window.h"
#include <QWidget>
#include <vector>
#include <string>
#include <QPushButton>
#include <QVBoxLayout>
#include <filesystem>
#include <string>
#include <iterator>
#include <span>
#include <map>
#include "style.h"

namespace fs = std::filesystem;

typedef void callbackFunction(const char* filename);

namespace core
{
    class SaveFileDialong: public Window
    {
        Q_OBJECT
    private:
        void makeGUI(std::string path);
        std::vector<std::string> _fileExtensions;
        callbackFunction* _cb;
        QWidget* filePages;
        QVBoxLayout* filePagesLayout;
        std::map<std::string, std::string> styles;
        bool checkExtension(std::string fileName);
    public:
        SaveFileDialong(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback);
    };
}

#endif //ROSHANSYSTEM_FILEDIALOG_H

ROSHANSYSTEMLIB_API core::SaveFileDialong* createSaveFileDialog(QWidget* parent, const char* fileExtensions[], int fileExtensionCount, callbackFunction* callbackFunction);