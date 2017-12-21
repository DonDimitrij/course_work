#-------------------------------------------------
#
# Project created by QtCreator 2017-12-21T15:08:06
#
#-------------------------------------------------

QT       += testlib

QT       -= gui

TARGET = tst_testtest
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app

INCLUDEPATH += ../app
DEPENDPATH += ../app

SOURCES += tst_testtest.cpp \
    ../app/mycalc.cpp
DEFINES += SRCDIR=\\\"$$PWD/\\\"
