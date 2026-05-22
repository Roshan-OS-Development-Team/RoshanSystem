#include "mainwindow.h"
#include "calculator.h"
#include "ui_mainwindow.h"
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->background->setScaledContents(true);
    ui->StartMenu->setVisible(StartMenuOpened);
}

MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_StartMenuButton_clicked()
{
    StartMenuOpened = !StartMenuOpened;
    ui->StartMenu->setVisible(StartMenuOpened);
}


void MainWindow::on_calculatorbtn_clicked()
{
    Calculator *calculator = new Calculator(this);
    calculator->show();
}

