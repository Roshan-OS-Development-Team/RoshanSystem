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
#include <iostream>
#include "mainWidgets/taskbar.h"
#include <boost/dll/import.hpp>

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
    std::map<std::string, QWidget*> apps;
    std::map<std::string, boost::dll::shared_library*> loadedDlls;

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

        fs::path _settingsFile = "settings.json";

        if (fs::exists(_settingsFile) && fs::file_size(_settingsFile) > 0)
        {
            std::ifstream settingsFile(_settingsFile);
            if (settingsFile.is_open())
            {
                settingsJSON = json::parse(settingsFile);
            }
            settingsFile.close();
        }
        else
        {
            std::ofstream settingsFile(_settingsFile);
            settingsJSON = {
                {"theme", "dark"},
                {"background", "textures/background7.png"},
                {"fullscreen", true}
            };
            settingsFile << settingsJSON.dump(4);
            settingsFile.close();
        }
        this->backgroundimg.load(QString::fromStdString(settingsJSON["background"].get<std::string>()));

        json appsJSON;
        fs::path _appsFile = "apps.json";
        if (fs::exists(_appsFile) || fs::file_size(_appsFile) > 0)
        {
            std::ifstream appsFile(_appsFile);
            if (appsFile.is_open())
            {
                appsJSON = json::parse(appsFile);
            }
            appsFile.close();
        }
        else
        {
            appsJSON = {};
        }

        std::vector<std::pair<std::string, std::string>> dllPaths;

        for (const auto& [key, value]: appsJSON.items())
        {
            dllPaths.push_back({key, value["filepath"].get<std::string>()});
        }

        for (const auto& [key, value] : dllPaths)
        {
            fs::path dllPath = value;

            try
            {
                this->loadedDlls[key] = new boost::dll::shared_library(dllPath);
                std::cout << "1. Put dll reference in the std::map\n";
                auto createApp = this->loadedDlls[key]->get<QWidget*(QWidget*)>("createApp");
                std::cout << "2. CreateApp reference got\n";
                QWidget* app = createApp(this);
                app->setParent(this);
                std::cout << "3. Created App\n";
                this->apps[key] = app;
                std::cout << "4. Put App reference in the apps std::map" << std::endl;
            }
            catch (std::exception& e)
            {
                std::cerr << "Error: " << e.what() << " of loading app " << key;
            }
        }

        this->ready = true;
        // auto *test = createWindow(this, "Test", 960, 480, "textures/logo.png");
        // showWin(test);
    }
    ~App()
    {
        for (const auto& [key, ptr]: this->loadedDlls)
        {
            delete ptr;
        }
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    App win;

    if (win.settingsJSON.value("fullscreen", true))
    {
        win.showFullScreen();
    } else
    {
        win.show();
    }

    return QApplication::exec();
}