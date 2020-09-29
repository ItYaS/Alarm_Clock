import shelve
import importlib
from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.week_window import Ui_MainWindow
import help_file
import main_win


class WinOfWeek(QtWidgets.QMainWindow):
    # конструктор
    def __init__(self):
        super(WinOfWeek, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Window for weekly call')
        self.setWindowIcon(QtGui.QIcon('more\\image.jpg'))

        self.ui.label.setText('Введите характеристики')
        self.ui.label.setFont(QtGui.QFont('SansSerif', 13))
        self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 25))

        self.ui.name.setMaxLength(100)
        self.ui.hour.setMaxLength(2)
        self.ui.minutes.setMaxLength(2)

        self.ui.name_label.setText('название')
        self.ui.hour_label.setText('час')
        self.ui.minutes_label.setText('минуты')

        self.ui.button_of_save.clicked.connect(self.save_and_close)

    # функция сохранения и открытие нового окна
    def save_and_close(self):
        # сохранение введенных данных
        data = shelve.open('saves data\\data')
        path = help_file.active_time
        data[path + 'days'] = 'дни: '
        if self.ui.monday.isChecked():
            help_file.list_of_days.append(0)
            data[path + 'days'] += 'пн '
        if self.ui.tuesday.isChecked():
            help_file.list_of_days.append(1)
            data[path + 'days'] += 'вт '
        if self.ui.wednesday.isChecked():
            help_file.list_of_days.append(2)
            data[path + 'days'] += 'ср '
        if self.ui.thursday.isChecked():
            help_file.list_of_days.append(3)
            data[path + 'days'] += 'чт '
        if self.ui.friday.isChecked():
            help_file.list_of_days.append(4)
            data[path + 'days'] += 'пт '
        if self.ui.saturday.isChecked():
            help_file.list_of_days.append(5)
            data[path + 'days'] += 'сб '
        if self.ui.sunday.isChecked():
            help_file.list_of_days.append(6)
            data[path + 'days'] += 'вс'

        data[path + 'name'] = str(self.ui.name.text())
        data[path + 'hour'] = str(self.ui.hour.text())
        data[path + 'minutes'] = str(self.ui.minutes.text())
        data[path + 'list'] = help_file.list_of_days
        data.close()
        # закрытие и открытие окон
        help_file.main_class.close_main_win()
        importlib.reload(main_win)
        help_file.main_class.open_main_win()
        help_file.main_class.close_week_win()
