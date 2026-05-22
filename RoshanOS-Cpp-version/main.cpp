#include "mainwindow.h"
#include <QApplication>
//#include <QResource>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    // Q_INIT_RESOURCE(resources);

    MainWindow w;
    w.show();

    return a.exec();
}