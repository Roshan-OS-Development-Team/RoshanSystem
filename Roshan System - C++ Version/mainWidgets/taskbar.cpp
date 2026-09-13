//
// Created by Roshan on 13/09/2026.
//

#include "taskbar.h"

Taskbar::Taskbar(QWidget* parent):
QWidget(parent)
{

}

void Taskbar::paintEvent(QPaintEvent* event)
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
