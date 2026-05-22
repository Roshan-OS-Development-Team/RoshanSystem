#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow() override;

private slots:
    //void on_pushButton_clicked();

    void on_StartMenuButton_clicked();

    void on_calculatorbtn_clicked();

private:
    Ui::MainWindow *ui;
    bool StartMenuOpened = false;
};
#endif // MAINWINDOW_H
