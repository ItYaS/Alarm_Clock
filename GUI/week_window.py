# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'week_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 31))
        self.label.setObjectName("label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(280, 70, 181, 16))
        self.name_label.setObjectName("name_label")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(280, 90, 251, 20))
        self.name.setObjectName("name")
        self.hour_label = QtWidgets.QLabel(self.centralwidget)
        self.hour_label.setGeometry(QtCore.QRect(280, 115, 111, 21))
        self.hour_label.setObjectName("hour_label")
        self.hour = QtWidgets.QLineEdit(self.centralwidget)
        self.hour.setGeometry(QtCore.QRect(280, 140, 113, 20))
        self.hour.setObjectName("hour")
        self.minutes_label = QtWidgets.QLabel(self.centralwidget)
        self.minutes_label.setGeometry(QtCore.QRect(280, 166, 111, 20))
        self.minutes_label.setObjectName("minutes_label")
        self.minutes = QtWidgets.QLineEdit(self.centralwidget)
        self.minutes.setGeometry(QtCore.QRect(280, 190, 113, 20))
        self.minutes.setObjectName("minutes")
        self.monday = QtWidgets.QCheckBox(self.centralwidget)
        self.monday.setGeometry(QtCore.QRect(30, 80, 131, 17))
        self.monday.setObjectName("monday")
        self.tuesday = QtWidgets.QCheckBox(self.centralwidget)
        self.tuesday.setGeometry(QtCore.QRect(30, 110, 131, 17))
        self.tuesday.setObjectName("tuesday")
        self.wednesday = QtWidgets.QCheckBox(self.centralwidget)
        self.wednesday.setGeometry(QtCore.QRect(30, 140, 131, 17))
        self.wednesday.setObjectName("wednesday")
        self.thursday = QtWidgets.QCheckBox(self.centralwidget)
        self.thursday.setGeometry(QtCore.QRect(30, 170, 131, 17))
        self.thursday.setObjectName("thursday")
        self.friday = QtWidgets.QCheckBox(self.centralwidget)
        self.friday.setGeometry(QtCore.QRect(30, 200, 131, 17))
        self.friday.setObjectName("friday")
        self.saturday = QtWidgets.QCheckBox(self.centralwidget)
        self.saturday.setGeometry(QtCore.QRect(30, 230, 131, 17))
        self.saturday.setObjectName("saturday")
        self.sunday = QtWidgets.QCheckBox(self.centralwidget)
        self.sunday.setGeometry(QtCore.QRect(30, 260, 131, 17))
        self.sunday.setObjectName("sunday")
        self.button_of_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_of_save.setGeometry(QtCore.QRect(470, 350, 75, 23))
        self.button_of_save.setObjectName("button_of_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.name_label.setText(_translate("MainWindow", "название"))
        self.hour_label.setText(_translate("MainWindow", "час"))
        self.minutes_label.setText(_translate("MainWindow", "минуты"))
        self.monday.setText(_translate("MainWindow", "понедельник"))
        self.tuesday.setText(_translate("MainWindow", "вторник"))
        self.wednesday.setText(_translate("MainWindow", "среда"))
        self.thursday.setText(_translate("MainWindow", "четверг"))
        self.friday.setText(_translate("MainWindow", "пятница"))
        self.saturday.setText(_translate("MainWindow", "суббота"))
        self.sunday.setText(_translate("MainWindow", "воскресенье"))
        self.button_of_save.setText(_translate("MainWindow", "сохранить"))
