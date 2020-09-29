import shelve
import importlib
from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.edit_window import Ui_MainWindow
import help_file
import main_win


class WinOfDays(QtWidgets.QMainWindow):
    # конструктор
    def __init__(self):
        super(WinOfDays, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Window for one-time call')
        self.setWindowIcon(QtGui.QIcon('more\\image.jpg'))

        self.ui.label.setText('Введите характеристики')
        self.ui.label.setFont(QtGui.QFont('SansSerif', 13))
        self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 25))

        self.ui.name.setMaxLength(100)
        self.ui.year.setMaxLength(4)
        self.ui.month.setMaxLength(2)
        self.ui.day.setMaxLength(2)
        self.ui.hour.setMaxLength(2)
        self.ui.minutes.setMaxLength(2)

        self.ui.name_label.setText('название будильника')
        self.ui.year_label.setText('год')
        self.ui.month_label.setText('месяц')
        self.ui.day_label.setText('день')
        self.ui.hour_label.setText('час')
        self.ui.minutes_label.setText('минуты')

        self.ui.button_of_save.clicked.connect(self.save_and_close)

    # функция сохранения и открытия нового окна
    def save_and_close(self):
        # сохранение введенных данных
        data = shelve.open('saves data\\data')
        path = help_file.active_time
        data[path + 'name'] = str(self.ui.name.text())
        data[path + 'year'] = str(self.ui.year.text())
        data[path + 'month'] = str(self.ui.month.text())
        data[path + 'day'] = str(self.ui.day.text())
        data[path + 'hour'] = str(self.ui.hour.text())
        data[path + 'minutes'] = str(self.ui.minutes.text())
        data.close()
        # открытие и закрытие окон
        help_file.main_class.close_main_win()
        importlib.reload(main_win)
        help_file.main_class.open_main_win()
        help_file.main_class.close_edit_win()
