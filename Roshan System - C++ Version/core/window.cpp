//
// Created by Roshan on 01/09/2026.
//

#include "window.h"

namespace core
{
    Window::Window(
        QWidget* parent,
        std::string title,
        std::pair<int, int> size,
        std::string icon_path
    ):
    QWidget(parent)
    {
        this->setFixedSize(size.first, size.second);
        auto background = new QWidget(this);
        background->setGeometry(0, 0, this->width(), this->height());
        background->setStyleSheet(QString::fromStdString(style["window"]));
        QPixmap winIco = QPixmap(QString::fromStdString(icon_path)).scaled(
            20,
            20,
            Qt::KeepAspectRatio,
            Qt::SmoothTransformation
        );
        auto winIcoLbl = new QLabel(this);
        winIcoLbl->setPixmap(winIco);
        winIcoLbl->move(10, 10);

        auto titleLbl = new QLabel(this);
        titleLbl->setText(QString::fromStdString(title));
        titleLbl->move(40, 10);

        auto closeBtn = new QPushButton(this);
        closeBtn->setText("X");
        closeBtn->setFixedSize(30, 30);
        closeBtn->move(this->width() - 40, 10);
        closeBtn->setStyleSheet(QString::fromStdString(style["closeBtn"]));
        connect(closeBtn, &QPushButton::clicked, this, &Window::hide);
    }

    void Window::mousePressEvent(QMouseEvent* event)
    {
        if (event->button() == Qt::LeftButton)
        {
            startX = (int)(event->position().x());
            startY = (int)(event->position().y());
        }

        QWidget::mousePressEvent(event);
    }

    void Window::mouseMoveEvent(QMouseEvent* event)
    {
        if (event->buttons() & Qt::LeftButton)
        {
            posX = this->x() + (int)(event->position().x()) - startX;
            posY = this->y() + (int)(event->position().y()) - startY;
            this->move(posX, posY);
        }

        QWidget::mouseMoveEvent(event);
    }
} // core