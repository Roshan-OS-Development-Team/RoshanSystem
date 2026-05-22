#include "calculator.h"
#include "ui_calculator.h"
#include <QString>

Calculator::Calculator(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Calculator)
{
    ui->setupUi(this);
}

Calculator::~Calculator()
{
    delete ui;
}

void Calculator::on_addbtn_clicked()
{
    double value1 = ui->value1->value();
    double value2 = ui->value2->value();

    double value3 = value1 + value2;

    ui->answerlabel->setText(QString::number(value3));
}


void Calculator::on_subtractbtn_clicked()
{
    double value1 = ui->value1->value();
    double value2 = ui->value2->value();

    double value3 = value1 - value2;

    ui->answerlabel->setText(QString::number(value3));
}


void Calculator::on_timesbtn_clicked()
{
    double value1 = ui->value1->value();
    double value2 = ui->value2->value();

    double value3 = value1 * value2;

    ui->answerlabel->setText(QString::number(value3));
}


void Calculator::on_dividebtn_clicked()
{
    double value1 = ui->value1->value();
    double value2 = ui->value2->value();

    double value3 = value1 / value2;

    ui->answerlabel->setText(QString::number(value3));
}

