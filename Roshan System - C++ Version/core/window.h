//
// Created by Roshan on 01/09/2026.
//

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
        int posX = 0;
        int posY = 0;
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
    };
} // core

#endif //ROSHANSYSTEM_WINDOW_H
