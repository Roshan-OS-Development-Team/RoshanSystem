//
// Created by Roshan on 13/09/2026.
//

#ifndef ROSHANSYSTEM_TASKBAR_H
#define ROSHANSYSTEM_TASKBAR_H

#include <QWidget>
#include <QPaintEvent>
#include <QPainter>
#include <QGraphicsBlurEffect>
#include <QGraphicsScene>
#include <QGraphicsPixmapItem>
#include <QPixmap>
#include <QImage>
#include <QPainterPath>

class Taskbar: public QWidget
{
protected:
    void paintEvent(QPaintEvent *event);
public:
    Taskbar(QWidget* parent);
};


#endif //ROSHANSYSTEM_TASKBAR_H
