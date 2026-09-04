#include <QApplication>
#include <QMainWindow>
#include <QLabel>
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
    QPixmap background;
    QLabel *backgroundLabel;
    QWidget *taskbar;
    QHBoxLayout *taskbarLayout;
    json settingsJSON;
    std::map <std::string, std::string> style = core::get_qss_styles("styling/main");
    bool ready = false;

    void resizeEvent(QResizeEvent* event) override
    {
        if (this->ready)
        {
            this->background = QPixmap(
                QString::fromStdString(
                    settingsJSON["background"].get<std::string>()
                    )
                ).scaled(
                this->width(),
                this->height(),
                Qt::IgnoreAspectRatio,
                Qt::SmoothTransformation
            );
            this->backgroundLabel->setGeometry(0, 0, this->width(), this->height());
            this->backgroundLabel->setPixmap(this->background);
            this->taskbar->setGeometry(0, this->height() - 70, this->width(), 70);
            this->taskbarLayout = new QHBoxLayout(this->taskbar);
        }
    }
public:
    App()
    {
        this->setWindowTitle("Roshan System");
        this->resize(1200, 800);
        this->backgroundLabel = new QLabel(this);
        this->taskbar = new QWidget(this);
        this->taskbar->setStyleSheet(QString::fromStdString(style["taskbar"]));

        if (std::filesystem::exists(fs::path("settings.json")))
        {
            std::ifstream settingsFile("settings.json");
            std::string settingsContents;
            if (settingsFile.is_open())
            {
                settingsJSON = json::parse(settingsFile);
            }
        }
        else
        {
            std::ofstream settingsFile("settings.json");
            settingsJSON = {
                {"theme", "dark"},
                {"background", "textures/background7.png"}
            };
            settingsFile << settingsJSON.dump(4);
        }

        this->ready = true;
        auto *test = new core::Window(this, "Test Window", {960, 480}, "textures/logo.png");
    }

    ~App()
    {
        for (QWidget *widget: this->findChildren<QWidget *>())
        {
            widget->deleteLater();
        }
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    App *win = new App();
    win->showFullScreen();

    return app.exec();
}