from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def setup_ui(self, window):
        window.setObjectName('WeekWindow')
        window.resize(558, 419)

        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName('central_widget')
        window.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menu_bar.setObjectName('menu_bar')
        window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(window)
        self.status_bar.setObjectName('status_bar')
        window.setStatusBar(self.status_bar)

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 421, 31))
        self.label.setObjectName('label')

        self.name_label = QtWidgets.QLabel(self.central_widget)
        self.name_label.setGeometry(QtCore.QRect(280, 70, 181, 16))
        self.name_label.setObjectName('name_label')

        self.hour_label = QtWidgets.QLabel(self.central_widget)
        self.hour_label.setGeometry(QtCore.QRect(280, 115, 111, 21))
        self.hour_label.setObjectName('hour_label')

        self.minutes_label = QtWidgets.QLabel(self.central_widget)
        self.minutes_label.setGeometry(QtCore.QRect(280, 166, 111, 20))
        self.minutes_label.setObjectName('minutes_label')

        # ниже элементы для взаимодействия с пользователем

        self.name = QtWidgets.QLineEdit(self.central_widget)
        self.name.setGeometry(QtCore.QRect(280, 90, 251, 20))
        self.name.setObjectName('name')
        self.name.setMaxLength(100)

        self.hour = QtWidgets.QLineEdit(self.central_widget)
        self.hour.setGeometry(QtCore.QRect(280, 140, 113, 20))
        self.hour.setObjectName('hour')
        self.hour.setMaxLength(2)

        self.minutes = QtWidgets.QLineEdit(self.central_widget)
        self.minutes.setGeometry(QtCore.QRect(280, 190, 113, 20))
        self.minutes.setObjectName('minutes')
        self.minutes.setMaxLength(2)

        self.monday = QtWidgets.QCheckBox(self.central_widget)
        self.monday.setGeometry(QtCore.QRect(30, 80, 131, 17))
        self.monday.setObjectName('monday')

        self.tuesday = QtWidgets.QCheckBox(self.central_widget)
        self.tuesday.setGeometry(QtCore.QRect(30, 110, 131, 17))
        self.tuesday.setObjectName('tuesday')

        self.wednesday = QtWidgets.QCheckBox(self.central_widget)
        self.wednesday.setGeometry(QtCore.QRect(30, 140, 131, 17))
        self.wednesday.setObjectName('wednesday')

        self.thursday = QtWidgets.QCheckBox(self.central_widget)
        self.thursday.setGeometry(QtCore.QRect(30, 170, 131, 17))
        self.thursday.setObjectName('thursday')

        self.friday = QtWidgets.QCheckBox(self.central_widget)
        self.friday.setGeometry(QtCore.QRect(30, 200, 131, 17))
        self.friday.setObjectName('friday')

        self.saturday = QtWidgets.QCheckBox(self.central_widget)
        self.saturday.setGeometry(QtCore.QRect(30, 230, 131, 17))
        self.saturday.setObjectName('saturday')

        self.sunday = QtWidgets.QCheckBox(self.central_widget)
        self.sunday.setGeometry(QtCore.QRect(30, 260, 131, 17))
        self.sunday.setObjectName('sunday')

        self.save_button = QtWidgets.QPushButton(self.central_widget)
        self.save_button.setGeometry(QtCore.QRect(470, 350, 75, 23))
        self.save_button.setObjectName('save_button')

        self.translate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def translate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate('WeekWindow', 'Window for weekly call'))
        window.setWindowIcon(QtGui.QIcon('more\\logo.jpg'))

        self.label.setText(_translate('WeekWindow', 'Enter time'))
        self.label.setFont(QtGui.QFont('SansSerif', 13))
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 25))

        self.name_label.setText(_translate('WeekWindow', 'name call'))
        self.hour_label.setText(_translate('WeekWindow', 'hour'))
        self.minutes_label.setText(_translate('WeekWindow', 'minutes'))

        self.monday.setText(_translate('WeekWindow', 'monday'))
        self.tuesday.setText(_translate('WeekWindow', 'tuesday'))
        self.wednesday.setText(_translate('WeekWindow', 'wednesday'))
        self.thursday.setText(_translate('WeekWindow', 'thursday'))
        self.friday.setText(_translate('WeekWindow', 'friday'))
        self.saturday.setText(_translate('WeekWindow', 'saturday'))
        self.sunday.setText(_translate('WeekWindow', 'sunday'))

        self.save_button.setText(_translate('WeekWindow', 'save'))
