//
// Created by Roshan on 13/09/2026.
//

#ifdef RoshanSystemCoreLib_EXPORTS
#define ROSHANSYSTEMLIB_API __declspec(dllexport)
#else
#define ROSHANSYSTEMLIB_API __declspec(dllimport)
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
#include <map>
#include "style.h"

namespace fs = std::filesystem;

typedef void callbackFunction(std::string filename);

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
    public:
        SaveFileDialong(QWidget* parent, std::vector<std::string> fileExtensions, callbackFunction* callback);
    };
}

#endif //ROSHANSYSTEM_FILEDIALOG_H
