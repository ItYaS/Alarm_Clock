from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 275)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(75, 10, 221, 16))
        self.name.setObjectName("name")

        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(40, 50, 271, 16))
        self.date.setObjectName("date")

        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(40, 90, 271, 16))
        self.time.setObjectName("time")

        self.deactivate_button = QtWidgets.QPushButton(self.centralwidget)
        self.deactivate_button.setGeometry(QtCore.QRect(90, 200, 111, 51))
        self.deactivate_button.setObjectName("deactivate_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notice about time"))
        MainWindow.setWindowIcon(QtGui.QIcon('more\\logo.jpg'))

        self.name.setText(_translate("MainWindow", ""))
        self.date.setText(_translate("MainWindow", ""))
        self.time.setText(_translate("MainWindow", ""))
        self.deactivate_button.setText(_translate("MainWindow", "deactivate"))
