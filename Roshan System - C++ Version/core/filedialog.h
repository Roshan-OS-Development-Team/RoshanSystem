//
// Created by Roshan on 13/09/2026.
//

#ifdef ROSHANSYSTEMLIB_API
#undef ROSHANSYSTEMLIB_API
#endif

#ifdef _WIN32
    #ifdef RoshanSystemCoreLib_EXPORTS
        #define ROSHANSYSTEMLIB_API extern "C" __declspec(dllexport)
    #else
        #define ROSHANSYSTEMLIB_API extern "C" __declspec(dllimport)
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
#include <unordered_map>
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
        std::unordered_map<std::string, std::string> styles;
        bool checkExtension(std::string fileName);
    public:
        SaveFileDialong(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback);
    };
}

#endif //ROSHANSYSTEM_FILEDIALOG_H

ROSHANSYSTEMLIB_API core::SaveFileDialong* createSaveFileDialog(QWidget* parent, const char* fileExtensions[], int fileExtensionCount, callbackFunction* callbackFunction);