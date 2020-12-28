from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 478)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.name_one_time = QtWidgets.QLabel(self.centralwidget)
        self.name_one_time.setGeometry(QtCore.QRect(36, 10, 381, 20))
        self.name_one_time.setObjectName("name_one_time")

        self.name_every_time = QtWidgets.QLabel(self.centralwidget)
        self.name_every_time.setGeometry(QtCore.QRect(460, 10, 351, 16))
        self.name_every_time.setObjectName("name_every_time")

        self.name0_0 = QtWidgets.QLabel(self.centralwidget)
        self.name0_0.setGeometry(QtCore.QRect(110, 60, 190, 13))
        self.name0_0.setObjectName("name0_0")
        self.date0_0 = QtWidgets.QLabel(self.centralwidget)
        self.date0_0.setGeometry(QtCore.QRect(30, 80, 141, 16))
        self.date0_0.setObjectName("date0_0")
        self.time0_0 = QtWidgets.QLabel(self.centralwidget)
        self.time0_0.setGeometry(QtCore.QRect(30, 100, 141, 16))
        self.time0_0.setObjectName("time0_0")

        self.name0_1 = QtWidgets.QLabel(self.centralwidget)
        self.name0_1.setGeometry(QtCore.QRect(110, 150, 190, 13))
        self.name0_1.setObjectName("name0_1")
        self.date0_1 = QtWidgets.QLabel(self.centralwidget)
        self.date0_1.setGeometry(QtCore.QRect(30, 170, 141, 16))
        self.date0_1.setObjectName("date0_1")
        self.time0_1 = QtWidgets.QLabel(self.centralwidget)
        self.time0_1.setGeometry(QtCore.QRect(30, 190, 141, 16))
        self.time0_1.setObjectName("time0_1")

        self.name0_2 = QtWidgets.QLabel(self.centralwidget)
        self.name0_2.setGeometry(QtCore.QRect(110, 250, 190, 13))
        self.name0_2.setObjectName("name0_2")
        self.date0_2 = QtWidgets.QLabel(self.centralwidget)
        self.date0_2.setGeometry(QtCore.QRect(30, 270, 141, 16))
        self.date0_2.setObjectName("date0_2")
        self.time0_2 = QtWidgets.QLabel(self.centralwidget)
        self.time0_2.setGeometry(QtCore.QRect(30, 290, 141, 16))
        self.time0_2.setObjectName("time0_2")

        self.name0_3 = QtWidgets.QLabel(self.centralwidget)
        self.name0_3.setGeometry(QtCore.QRect(110, 350, 190, 13))
        self.name0_3.setObjectName("name0_3")
        self.date0_3 = QtWidgets.QLabel(self.centralwidget)
        self.date0_3.setGeometry(QtCore.QRect(30, 370, 141, 16))
        self.date0_3.setObjectName("date0_3")
        self.time0_3 = QtWidgets.QLabel(self.centralwidget)
        self.time0_3.setGeometry(QtCore.QRect(30, 390, 141, 16))
        self.time0_3.setObjectName("time0_3")

        self.name1_0 = QtWidgets.QLabel(self.centralwidget)
        self.name1_0.setGeometry(QtCore.QRect(510, 60, 201, 16))
        self.name1_0.setObjectName("name1_0")
        self.date1_0 = QtWidgets.QLabel(self.centralwidget)
        self.date1_0.setGeometry(QtCore.QRect(470, 80, 151, 16))
        self.date1_0.setObjectName("date1_0")
        self.time1_0 = QtWidgets.QLabel(self.centralwidget)
        self.time1_0.setGeometry(QtCore.QRect(470, 100, 171, 16))
        self.time1_0.setObjectName("time1_0")

        self.name1_1 = QtWidgets.QLabel(self.centralwidget)
        self.name1_1.setGeometry(QtCore.QRect(510, 150, 201, 16))
        self.name1_1.setObjectName("name1_1")
        self.date1_1 = QtWidgets.QLabel(self.centralwidget)
        self.date1_1.setGeometry(QtCore.QRect(470, 170, 181, 16))
        self.date1_1.setObjectName("date1_1")
        self.time1_1 = QtWidgets.QLabel(self.centralwidget)
        self.time1_1.setGeometry(QtCore.QRect(470, 190, 181, 16))
        self.time1_1.setObjectName("time1_1")

        self.name1_2 = QtWidgets.QLabel(self.centralwidget)
        self.name1_2.setGeometry(QtCore.QRect(510, 250, 201, 16))
        self.name1_2.setObjectName("name1_2")
        self.date1_2 = QtWidgets.QLabel(self.centralwidget)
        self.date1_2.setGeometry(QtCore.QRect(470, 270, 181, 16))
        self.date1_2.setObjectName("date1_2")
        self.time1_2 = QtWidgets.QLabel(self.centralwidget)
        self.time1_2.setGeometry(QtCore.QRect(470, 290, 181, 16))
        self.time1_2.setObjectName("time1_2")

        self.name1_3 = QtWidgets.QLabel(self.centralwidget)
        self.name1_3.setGeometry(QtCore.QRect(510, 350, 201, 16))
        self.name1_3.setObjectName("name1_3")
        self.date1_3 = QtWidgets.QLabel(self.centralwidget)
        self.date1_3.setGeometry(QtCore.QRect(470, 370, 181, 16))
        self.date1_3.setObjectName("date1_3")
        self.time1_3 = QtWidgets.QLabel(self.centralwidget)
        self.time1_3.setGeometry(QtCore.QRect(470, 390, 181, 16))
        self.time1_3.setObjectName("time1_3")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(430, 20, 21, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 120, 421, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 230, 421, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 330, 421, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(450, 120, 391, 31))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(450, 230, 391, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(450, 330, 391, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 30, 831, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.delete0_0 = QtWidgets.QPushButton(self.centralwidget)
        self.delete0_0.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.delete0_0.setObjectName("delete0_0")
        self.add0_0 = QtWidgets.QPushButton(self.centralwidget)
        self.add0_0.setGeometry(QtCore.QRect(260, 90, 75, 23))
        self.add0_0.setObjectName("add0_0")

        self.delete0_1 = QtWidgets.QPushButton(self.centralwidget)
        self.delete0_1.setGeometry(QtCore.QRect(350, 180, 75, 23))
        self.delete0_1.setObjectName("delete0_1")
        self.add0_1 = QtWidgets.QPushButton(self.centralwidget)
        self.add0_1.setGeometry(QtCore.QRect(260, 180, 75, 23))
        self.add0_1.setObjectName("add0_1")

        self.delete0_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete0_2.setGeometry(QtCore.QRect(350, 280, 75, 23))
        self.delete0_2.setObjectName("delete0_2")
        self.add0_2 = QtWidgets.QPushButton(self.centralwidget)
        self.add0_2.setGeometry(QtCore.QRect(260, 280, 75, 23))
        self.add0_2.setObjectName("add0_2")

        self.delete0_3 = QtWidgets.QPushButton(self.centralwidget)
        self.delete0_3.setGeometry(QtCore.QRect(350, 380, 75, 23))
        self.delete0_3.setObjectName("delete0_3")
        self.add0_3 = QtWidgets.QPushButton(self.centralwidget)
        self.add0_3.setGeometry(QtCore.QRect(260, 380, 75, 23))
        self.add0_3.setObjectName("add0_3")

        self.delete1_0 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1_0.setGeometry(QtCore.QRect(760, 90, 75, 23))
        self.delete1_0.setObjectName("delete1_0")
        self.add1_0 = QtWidgets.QPushButton(self.centralwidget)
        self.add1_0.setGeometry(QtCore.QRect(670, 90, 75, 23))
        self.add1_0.setObjectName("add1_0")

        self.delete1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1_1.setGeometry(QtCore.QRect(760, 180, 75, 23))
        self.delete1_1.setObjectName("delete1_1")
        self.add1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.add1_1.setGeometry(QtCore.QRect(670, 180, 75, 23))
        self.add1_1.setObjectName("add1_1")

        self.delete1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1_2.setGeometry(QtCore.QRect(760, 280, 75, 23))
        self.delete1_2.setObjectName("delete1_2")
        self.add1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.add1_2.setGeometry(QtCore.QRect(670, 280, 75, 23))
        self.add1_2.setObjectName("add1_2")

        self.delete1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1_3.setGeometry(QtCore.QRect(760, 380, 75, 23))
        self.delete1_3.setObjectName("delete1_3")
        self.add1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.add1_3.setGeometry(QtCore.QRect(670, 380, 75, 23))
        self.add1_3.setObjectName("add1_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alarm Clock"))
        MainWindow.setWindowIcon(QtGui.QIcon('more\\logo.jpg'))

        self.name_one_time.setText(_translate("MainWindow", "\t\t Alarm clocks for one-time call"))
        self.name_every_time.setText(_translate("MainWindow", "\t\t Alarm clocks for weekly call"))

        self.name0_0.setText(_translate("MainWindow", ""))
        self.date0_0.setText(_translate("MainWindow", ""))
        self.time0_0.setText(_translate("MainWindow", ""))

        self.name0_1.setText(_translate("MainWindow", ""))
        self.date0_1.setText(_translate("MainWindow", ""))
        self.time0_1.setText(_translate("MainWindow", ""))

        self.name0_2.setText(_translate("MainWindow", ""))
        self.date0_2.setText(_translate("MainWindow", ""))
        self.time0_2.setText(_translate("MainWindow", ""))

        self.name0_3.setText(_translate("MainWindow", ""))
        self.date0_3.setText(_translate("MainWindow", ""))
        self.time0_3.setText(_translate("MainWindow", ""))

        self.name1_0.setText(_translate("MainWindow", ""))
        self.date1_0.setText(_translate("MainWindow", ""))
        self.time1_0.setText(_translate("MainWindow", ""))

        self.name1_1.setText(_translate("MainWindow", ""))
        self.date1_1.setText(_translate("MainWindow", ""))
        self.time1_1.setText(_translate("MainWindow", ""))

        self.name1_2.setText(_translate("MainWindow", ""))
        self.date1_2.setText(_translate("MainWindow", ""))
        self.time1_2.setText(_translate("MainWindow", ""))

        self.name1_3.setText(_translate("MainWindow", ""))
        self.date1_3.setText(_translate("MainWindow", ""))
        self.time1_3.setText(_translate("MainWindow", ""))

        self.delete0_0.setText(_translate("MainWindow", "delete"))
        self.add0_0.setText(_translate("MainWindow", "add"))

        self.delete0_1.setText(_translate("MainWindow", "delete"))
        self.add0_1.setText(_translate("MainWindow", "add"))

        self.delete0_2.setText(_translate("MainWindow", "delete"))
        self.add0_2.setText(_translate("MainWindow", "add"))

        self.delete0_3.setText(_translate("MainWindow", "delete"))
        self.add0_3.setText(_translate("MainWindow", "add"))

        self.delete1_0.setText(_translate("MainWindow", "delete"))
        self.add1_0.setText(_translate("MainWindow", "add"))

        self.delete1_1.setText(_translate("MainWindow", "delete"))
        self.add1_1.setText(_translate("MainWindow", "add"))

        self.delete1_2.setText(_translate("MainWindow", "delete"))
        self.add1_2.setText(_translate("MainWindow", "add"))

        self.delete1_3.setText(_translate("MainWindow", "delete"))
        self.add1_3.setText(_translate("MainWindow", "add"))
