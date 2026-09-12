//
// Created by Roshan on 01/09/2026.
//

#ifdef RoshanSystemCoreLib_EXPORTS
#define ROSHANSYSTEMLIB_API __declspec(dllexport)
#else
#define ROSHANSYSTEMLIB_API __declspec(dllimport)
#endif

#ifndef ROSHANSYSTEM_WINDOW_H
#define ROSHANSYSTEM_WINDOW_H

#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QPixmap>
#include <QMouseEvent>

#include <string>
#include <utility>
#include <map>


#include "style.h"

namespace core
{
    class Window: public QWidget
    {
        Q_OBJECT
    private:
        int startX = 0;
        int startY = 0;
        std::map<std::string, std::string> style = core::get_qss_styles("../styling/window");
    protected:
        void mousePressEvent(QMouseEvent* event) override;
        void mouseMoveEvent(QMouseEvent* event) override;
    public:
        Window(
            QWidget* parent = nullptr,
            std::string title = "Roshan OS Window",
            std::pair<int, int> size = {960, 480},
            std::string icon_path = "textures/generic app.png"
        );
        int posX = 0;
        int posY = 0;
    };
} // core

extern "C" {
ROSHANSYSTEMLIB_API core::Window* createWindow(
    QWidget* parent = nullptr,
    const char* title = "Roshan OS Window",
    int width = 960,
    int height = 480,
    const char *icon_path = "textures/generic app.png"
    );
ROSHANSYSTEMLIB_API void delWindow(core::Window* window);
ROSHANSYSTEMLIB_API int getWinX(core::Window* window);
ROSHANSYSTEMLIB_API int getWinY(core::Window* window);
ROSHANSYSTEMLIB_API void moveWin(core::Window* window, int x, int y);
ROSHANSYSTEMLIB_API void showWin(core::Window* window);
}

#endif //ROSHANSYSTEM_WINDOW_H
