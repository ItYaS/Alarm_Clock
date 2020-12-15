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
        days = ''

        if self.ui.monday.isChecked():
            days += 'пн '
        if self.ui.tuesday.isChecked():
            days += 'вт '
        if self.ui.wednesday.isChecked():
            days += 'ср '
        if self.ui.thursday.isChecked():
            days += 'чт '
        if self.ui.friday.isChecked():
            days += 'пт '
        if self.ui.saturday.isChecked():
            days += 'сб '
        if self.ui.sunday.isChecked():
            days += 'вс'

        query = f"""
                    UPDATE data SET
                        name = {self.ui.name.text()},
                        days = {days},
                        hour = {self.ui.hour.text()},
                        minutes = {self.ui.minutes.text()}
                    WHERE id = {int(help_file.active_id)}
            """
        help_file.database.insert_query('week.sqlite', query)

        # закрытие и открытие окон
        help_file.main_class.close_main_win()
        importlib.reload(main_win)
        help_file.main_class.open_main_win()
        help_file.main_class.close_week_win()
