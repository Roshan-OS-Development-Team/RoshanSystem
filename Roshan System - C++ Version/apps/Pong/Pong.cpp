//
// Created by Roshan on 16/09/2026.
//

#define RoshanSystemPong_EXPORTS
#include "Pong.h"

#include <QTimer>

PongGame::PongGame(QWidget* parent): QGraphicsView(parent)
{
    this->setFixedSize(940, 420);
    this->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    this->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    this->setBackgroundBrush(Qt::black);
}

void PongGame::resetBall()
{
    ball->setPos((int)(this->width() / 2), (int)(this->height() / 2));
    ballVx = -ballVx;
    ballVy = -ballVy;
}

void PongGame::updateScoreboard()
{
    scoreDisplay->setPlainText(QString::number(playerScore) + " " + QString::number(player2Score));
    scoreDisplay->setPos((int)(this->width() / 2) - (int)(scoreDisplay->boundingRect().width() / 2), 20);
}

void PongGame::updateGame()
{
    qreal player1PaddleHeight = player1Paddle->boundingRect().height();
    qreal ballHeight = ball->boundingRect().height();
    qreal player2PaddleHeight = player2Paddle->boundingRect().height();

    if (keyPressed[Qt::Key_W])
    {
        player1Paddle->setPos(player1Paddle->x(), player1Paddle->y() - paddleSpeed);
    }

    if (keyPressed[Qt::Key_S])
    {
        player1Paddle->setPos(player1Paddle->x(), player1Paddle->y() + paddleSpeed);
    }

    if (keyPressed[Qt::Key_Up])
    {
        player2Paddle->setPos(player2Paddle->x(), player2Paddle->y() - paddleSpeed);
    }

    if (keyPressed[Qt::Key_Down])
    {
        player2Paddle->setPos(player2Paddle->x(), player2Paddle->y() + paddleSpeed);
    }

    ball->setPos(ball->x() + ballVx, ball->y() + ballVy);

    if (ball->y() <= 0)
    {
        ball->setPos(ball->x(), 0);
        ballVy = -ballVy;
    }
    else if (ball->y() + ball->boundingRect().height() >= this->height())
    {
        ball->setPos(ball->x(), this->height() - ball->boundingRect().height());
        ballVy = -ballVy;
    }

    if (ball->collidesWithItem(player1Paddle) && ballVx < 0)
    {
        ballVx = -ballVx;
    }

    else if (ball->collidesWithItem(player2Paddle) && ballVx > 0)
    {
        ballVx = -ballVx;
    }

    if (ball->x() < 0)
    {
        player2Score++;
        this->updateScoreboard();
        resetBall();
    }
    else if (ball->x() + ball->boundingRect().width() > this->width())
    {
        playerScore++;
        this->updateScoreboard();
        resetBall();
    }
}

void PongGame::keyPressEvent(QKeyEvent* event)
{
    int key = event->key();

    if (key >= 0 && key < 1024)
    {
        keyPressed[key] = true;
    }
}

void PongGame::keyReleaseEvent(QKeyEvent* event)
{
    int key = event->key();

    if (key >= 0 && key < 1024)
    {
        keyPressed[key] = false;
    }
}

void PongGame::showEvent(QShowEvent* event)
{
    QGraphicsView::showEvent(event);

    if (!scene)
    {
        scene = new QGraphicsScene(0, 0, 940, 420);
        this->setScene(scene);

        QPixmap ballImage = QPixmap("textures/ball.png");
        QPixmap paddleImage = QPixmap("textures/paddle.png");

        ball = new QGraphicsPixmapItem(ballImage);
        player1Paddle = new QGraphicsPixmapItem(paddleImage);
        player2Paddle = new QGraphicsPixmapItem(paddleImage);

        scene->addItem(ball);
        scene->addItem(player1Paddle);
        scene->addItem(player2Paddle);

        scoreDisplay = new QGraphicsTextItem();
        scoreDisplay->setDefaultTextColor(Qt::white);
        scoreDisplay->setFont(QFont("Arial", 30, QFont::Bold));

        scene->addItem(scoreDisplay);

        this->updateScoreboard();
        this->resetBall();

        player1Paddle->setPos(30, (420 / 2) - (player1Paddle->boundingRect().height() / 2));
        player2Paddle->setPos(940 - 50, (420 / 2) - (player2Paddle->boundingRect().height() / 2));

        this->setFocusPolicy(Qt::StrongFocus);
        this->setFocus();

        QTimer *gameLoop = new QTimer(this);
        this->connect(gameLoop, &QTimer::timeout, this, [this]()
        {
            this->updateGame();
        });
        gameLoop->start(16);
    }
}

extern "C" ROSHANSYSTEMLIB_API QWidget* createApp(QWidget* parent)
{
    core::Window* app = createWindow(parent, "Pong", 960, 480, "textures/Pong.png");
    PongGame *game = new PongGame(nullptr);
    game->setParent(app);
    game->setGeometry(10, 50, 920, 420);
    game->show();
    return static_cast<QWidget*>(app);
}