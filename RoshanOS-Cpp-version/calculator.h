#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <QMainWindow>

namespace Ui {
class Calculator;
}

class Calculator : public QMainWindow
{
    Q_OBJECT

public:
    explicit Calculator(QWidget *parent = nullptr);
    ~Calculator();

private slots:
    void on_addbtn_clicked();

    void on_subtractbtn_clicked();

    void on_timesbtn_clicked();

    void on_dividebtn_clicked();

private:
    Ui::Calculator *ui;
};

#endif // CALCULATOR_H
