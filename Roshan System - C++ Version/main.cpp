#include <QApplication>
#include <QMainWindow>
#include <QLabel>
#include <QImage>
#include <QPixmap>
#include <QWidget>
#include <QHBoxLayout>
#include "core/core.h"
#include <map>
#include <QString>
#include <fstream>
#include <filesystem>
#include <nlohmann/json.hpp>
#include <string>

using json = nlohmann::json;
namespace fs = std::filesystem;

class App: public QMainWindow
{
protected:
    QImage backgroundimg;
    QPixmap background;
    QLabel *backgroundLabel;
    QWidget *taskbar;
    QHBoxLayout *taskbarLayout;
    json style;
    bool ready = false;

    void resizeEvent(QResizeEvent* event) override
    {
        if (this->ready && !this->backgroundimg.isNull())
        {
            this->background = QPixmap::fromImage(
                this->backgroundimg.scaled(
                    this->width(),
                    this->height(),
                    Qt::IgnoreAspectRatio,
                    Qt::SmoothTransformation
                )
            );
            this->backgroundLabel->setGeometry(0, 0, this->width(), this->height());
            this->backgroundLabel->setPixmap(this->background);
            this->taskbar->setGeometry(0, this->height() - 70, this->width(), 70);
        }
    }
    void openApp(auto *app)
    {
        moveWin(app, getWinX(app), getWinY(app));
    }
public:
    json settingsJSON;
    App()
    {
        this->setWindowTitle("Roshan System");
        this->resize(1200, 800);
        this->setWindowIcon(QPixmap("textures/Start.png"));

        this->style = json::parse(get_qss_styles("styling/main"));

        this->backgroundLabel = new QLabel(this);
        this->backgroundLabel->setSizePolicy(QSizePolicy::Ignored, QSizePolicy::Ignored);
        this->backgroundLabel->setScaledContents(true);
        this->taskbar = new QWidget(this);
        this->taskbar->setStyleSheet(QString::fromStdString(style["taskbar"]));
        this->taskbarLayout = new QHBoxLayout(this->taskbar);

        if (fs::exists(fs::path("settings.json")) && fs::file_size(fs::path("settings.json")) > 0)
        {
            std::ifstream settingsFile("settings.json");
            std::string settingsContents;
            if (settingsFile.is_open())
            {
                settingsJSON = json::parse(settingsFile);
            }
            settingsFile.close();
        }
        else
        {
            std::ofstream settingsFile("settings.json");
            settingsJSON = {
                {"theme", "dark"},
                {"background", "textures/background7.png"},
                {"fullscreen", true}
            };
            settingsFile << settingsJSON.dump(4);
            settingsFile.close();
        }
        this->backgroundimg.load(QString::fromStdString(settingsJSON["background"].get<std::string>()));

        this->ready = true;
        auto *test = createWindow(this, "Test", 960, 480, "textures/logo.png");
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    App win;
    std::ifstream settingsFile("settings.json");

    if (win.settingsJSON.value("fullscreen", true))
    {
        win.showFullScreen();
    } else
    {
        win.show();
    }

    return QApplication::exec();
}