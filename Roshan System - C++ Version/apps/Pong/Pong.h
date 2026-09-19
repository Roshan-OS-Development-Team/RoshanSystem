//
// Created by Roshan on 16/09/2026.
//

#ifndef ROSHANSYSTEM_PONG_H
#define ROSHANSYSTEM_PONG_H
#include "../../core/window.h"
#include <QWidget>
#include <QTimer>
#include <QKeyEvent>
#include <QGraphicsView>
#include <QGraphicsPixmapItem>
#include <QGraphicsScene>
#include <QGraphicsTextItem>
#include <QPixmap>
#include <QShowEvent>
#include <set>

class PongGame: public QGraphicsView
{
    Q_OBJECT
private:
    QGraphicsScene *scene;

    QGraphicsPixmapItem *ball;
    QGraphicsPixmapItem *player1Paddle;
    QGraphicsPixmapItem *player2Paddle;
    QGraphicsTextItem *scoreDisplay;

    QTimer gameTimer;

    qreal ballVx = 5.0;
    qreal ballVy = 3.0;

    const qreal paddleSpeed = 6.0;

    int playerScore = 0;
    int player2Score = 0;

    bool keyPressed[1024] = {false};

    void resetBall();
    void updateScoreboard();

public:
    PongGame(QWidget *parent);
public slots:
    void updateGame();
protected:
    void keyPressEvent(QKeyEvent* event) override;
    void keyReleaseEvent(QKeyEvent* event) override;
    void showEvent(QShowEvent* event) override;
};

#ifdef RoshanSystemPong_EXPORTS
#define ROSHANSYSTEMLIB_API __declspec(dllexport)
#else
#define ROSHANSYSTEMLIB_API __declspec(dllimport)
#endif

extern "C" {
    ROSHANSYSTEMLIB_API QWidget* createApp(QWidget* parent);
}

#endif //ROSHANSYSTEM_PONG_H
