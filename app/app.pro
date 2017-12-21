QT += core
QT -= gui

CONFIG += c++11

TARGET = app
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp \
    mycalc.cpp

HEADERS += \
    mycalc.h
