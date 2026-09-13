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
        this->setAttribute(Qt::WA_TranslucentBackground);
        this->setFixedSize(size.first, size.second);
        this->setWindowTitle(QString::fromStdString(title));
        this->setWindowFlag(Qt::FramelessWindowHint, true);
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
        titleLbl->setStyleSheet(QString::fromStdString(style["titleLbl"]));
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

    void Window::paintEvent(QPaintEvent* event)
    {
        QPainter painter(this);
        painter.setRenderHint(QPainter::Antialiasing);

        QPainterPath clipPath;
        clipPath.addRoundedRect(this->rect(), 10, 10);
        painter.setClipPath(clipPath);

        if (this->parentWidget())
        {
            bool wasVisible = this->isVisible();
            this->blockSignals(true);
            this->setVisible(false);

            QPixmap background = this->parentWidget()->grab(geometry());

            this->blockSignals(false);
            this->setVisible(wasVisible);

            auto *blur = new QGraphicsBlurEffect(this);
            blur->setBlurRadius(15);
            blur->setBlurHints(QGraphicsBlurEffect::PerformanceHint);

            QGraphicsScene scene;
            QGraphicsPixmapItem item;

            item.setPixmap(background);
            item.setGraphicsEffect(blur);
            scene.addItem(&item);

            QImage blurredImage(this->size(), QImage::Format_ARGB32_Premultiplied);
            blurredImage.fill(Qt::transparent);

            QPainter imagePainter(&blurredImage);
            scene.render(&imagePainter, QRectF(), QRectF(0, 0, this->width(), this->height()));

            painter.drawImage(0, 0, blurredImage);
        }

        painter.setBrush(QColor(0, 0, 0, 140));
        painter.setPen(Qt::NoPen);
        painter.drawRect(this->rect());

        QWidget::paintEvent(event);
    }
} // core

ROSHANSYSTEMLIB_API core::Window* createWindow(
    QWidget* parent,
    const char* title,
    int width,
    int height,
    const char* icon_path
    )
{
    return new core::Window(
        parent,
        std::string(title),
{width, height},
std::string(icon_path)
    );
}

ROSHANSYSTEMLIB_API void delWindow(core::Window* window)
{
    delete window;
    window = nullptr;
}

ROSHANSYSTEMLIB_API int getWinX(core::Window* window)
{
    return window->posX;
}

ROSHANSYSTEMLIB_API int getWinY(core::Window* window)
{
    return window->posY;
}

ROSHANSYSTEMLIB_API void moveWin(core::Window* window, int x, int y)
{
    window->move(x, y);
}

ROSHANSYSTEMLIB_API void showWin(core::Window* window)
{
    window->show();
}

ROSHANSYSTEMLIB_API void hideWin(core::Window *window)
{
    window->hide();
}