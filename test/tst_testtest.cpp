#include <QString>
#include <QtTest>

#include "mycalc.h"

class TestTest : public QObject
{
    Q_OBJECT

public:
    TestTest();

private Q_SLOTS:
    void testCase1();
};

TestTest::TestTest()
{
}

void TestTest::testCase1()
{
    MyCalc obj;
    QCOMPARE(obj.calc(9, 6), 14);
}

QTEST_APPLESS_MAIN(TestTest)

#include "tst_testtest.moc"
