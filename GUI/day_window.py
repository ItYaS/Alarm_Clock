from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def setup_ui(self, window):
        window.setObjectName('DayWindow')
        window.resize(539, 414)

        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName('central_widget')
        window.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menu_bar.setObjectName('menu_bar')
        window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(window)
        self.status_bar.setObjectName('status_bar')
        window.setStatusBar(self.status_bar)

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(30, 10, 81, 16))
        self.label.setFont(QtGui.QFont('SansSerif', 13))
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 25))
        self.label.setObjectName('label')

        self.name_label = QtWidgets.QLabel(self.central_widget)
        self.name_label.setGeometry(QtCore.QRect(100, 60, 221, 16))
        self.name_label.setObjectName('name_label')

        self.year_label = QtWidgets.QLabel(self.central_widget)
        self.year_label.setGeometry(QtCore.QRect(100, 110, 221, 16))
        self.year_label.setObjectName('year_label')

        self.month_label = QtWidgets.QLabel(self.central_widget)
        self.month_label.setGeometry(QtCore.QRect(100, 160, 221, 16))
        self.month_label.setObjectName('month_label')

        self.day_label = QtWidgets.QLabel(self.central_widget)
        self.day_label.setGeometry(QtCore.QRect(100, 210, 221, 16))
        self.day_label.setObjectName('day_label')

        self.hour_label = QtWidgets.QLabel(self.central_widget)
        self.hour_label.setGeometry(QtCore.QRect(100, 260, 221, 16))
        self.hour_label.setObjectName('hour_label')

        self.minutes_label = QtWidgets.QLabel(self.central_widget)
        self.minutes_label.setGeometry(QtCore.QRect(100, 310, 221, 16))
        self.minutes_label.setObjectName('minutes_label')

        # ниже элементы для взаимодействия с пользователем

        self.name = QtWidgets.QLineEdit(self.central_widget)
        self.name.setGeometry(QtCore.QRect(100, 80, 221, 20))
        self.name.setObjectName('name')
        self.name.setMaxLength(100)

        self.year = QtWidgets.QLineEdit(self.central_widget)
        self.year.setGeometry(QtCore.QRect(100, 130, 71, 20))
        self.year.setObjectName('year')
        self.year.setMaxLength(4)

        self.month = QtWidgets.QLineEdit(self.central_widget)
        self.month.setGeometry(QtCore.QRect(100, 180, 71, 20))
        self.month.setObjectName('month')
        self.month.setMaxLength(2)

        self.day = QtWidgets.QLineEdit(self.central_widget)
        self.day.setGeometry(QtCore.QRect(100, 230, 71, 20))
        self.day.setObjectName('day')
        self.day.setMaxLength(2)

        self.hour = QtWidgets.QLineEdit(self.central_widget)
        self.hour.setGeometry(QtCore.QRect(100, 280, 71, 20))
        self.hour.setObjectName('hour')
        self.hour.setMaxLength(2)

        self.minutes = QtWidgets.QLineEdit(self.central_widget)
        self.minutes.setGeometry(QtCore.QRect(100, 330, 71, 20))
        self.minutes.setObjectName('minutes')
        self.minutes.setMaxLength(2)

        self.save_button = QtWidgets.QPushButton(self.central_widget)
        self.save_button.setGeometry(QtCore.QRect(450, 350, 75, 23))
        self.save_button.setObjectName('save_button')

        self.translate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def translate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate('DayWindow', 'Window for one-time call'))
        window.setWindowIcon(QtGui.QIcon('more\\logo.jpg'))

        self.label.setText(_translate('DayWindow', 'Enter time'))
        self.label.setFont(QtGui.QFont('SansSerif', 13))
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 25))

        self.name_label.setText(_translate('DayWindow', 'name call'))
        self.year_label.setText(_translate('DayWindow', 'year'))
        self.month_label.setText(_translate('DayWindow', 'month'))
        self.day_label.setText(_translate('DayWindow', 'day'))
        self.hour_label.setText(_translate('DayWindow', 'hour'))
        self.minutes_label.setText(_translate('DayWindow', 'minutes'))

        self.save_button.setText(_translate('DayWindow', 'save'))
