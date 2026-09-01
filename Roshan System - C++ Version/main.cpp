#include <QApplication>
#include <QMainWindow>
#include <QLabel>
#include <QPixmap>
#include <QWidget>
#include <QHBoxLayout>
#include "core/style.h"
#include "core/window.h"
#include <map>
#include <QString>

class App: public QMainWindow
{
protected:
    QPixmap background;
    QLabel *backgroundLabel;
    QWidget *taskbar;
    QHBoxLayout *taskbarLayout = new QHBoxLayout(taskbar);
    std::map <std::string, std::string> style = core::get_qss_styles("styling/main");

    void resizeEvent(QResizeEvent* event) override
    {
        this->background = QPixmap("textures/background7.png").scaled(
            this->width(),
            this->height(),
            Qt::IgnoreAspectRatio,
            Qt::SmoothTransformation
        );
        this->backgroundLabel->setGeometry(0, 0, this->width(), this->height());
        this->backgroundLabel->setPixmap(this->background);
        this->taskbar->setGeometry(0, this->height() - 70, this->width(), 70);
    }
public:
    App()
    {
        this->setWindowTitle("Roshan System");
        this->resize(1200, 800);
        this->backgroundLabel = new QLabel(this);
        this->taskbar = new QWidget(this);
        this->taskbar->setStyleSheet(QString::fromStdString(style["taskbar"]));
        core::Window *test = new core::Window(this, "Test Window", {960, 480}, "textures/start.png");
        test->move(10, 10);
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    App *win = new App();
    win->showFullScreen();

    return app.exec();
}