from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def setup_ui(self, window):
        window.setObjectName('NoticeWindow')
        window.resize(290, 275)

        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName('central_widget')
        window.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menu_bar.setObjectName('menu_bar')
        window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(window)
        self.status_bar.setObjectName('status_bar')
        window.setStatusBar(self.status_bar)

        self.name = QtWidgets.QLabel(self.central_widget)
        self.name.setGeometry(QtCore.QRect(75, 10, 221, 16))
        self.name.setObjectName('name')

        self.date = QtWidgets.QLabel(self.central_widget)
        self.date.setGeometry(QtCore.QRect(40, 50, 271, 16))
        self.date.setObjectName('date')

        self.time = QtWidgets.QLabel(self.central_widget)
        self.time.setGeometry(QtCore.QRect(40, 90, 271, 16))
        self.time.setObjectName('time')

        self.deactivate_button = QtWidgets.QPushButton(self.central_widget)
        self.deactivate_button.setGeometry(QtCore.QRect(90, 200, 111, 51))
        self.deactivate_button.setObjectName('deactivate_button')

        self.translate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def translate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate('NoticeWindow', 'Notice about time'))
        window.setWindowIcon(QtGui.QIcon('more\\logo.jpg'))

        self.deactivate_button.setText(_translate('NoticeWindow', 'deactivate'))
