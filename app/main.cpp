#include <QCoreApplication>
#include <iostream>
#include "mycalc.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    MyCalc obj;
    std::cout << obj.calc(7, 6) << std::endl;

    return a.exec();
}
