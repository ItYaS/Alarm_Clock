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
        query = f"""
                    UPDATE data SET
                        name = {self.ui.name.text()}
                        days = {self.ui.day.text()}.{self.ui.month.text()}.{self.ui.year.text()}
                        hour = {self.ui.hour.text()}
                        minutes = {self.ui.minutes.text()}
                    WHERE id = {int(help_file.active_id)}
                """
        help_file.database.insert_query('day.sqlite', query)

        # открытие и закрытие окон
        help_file.main_class.close_main_win()
        importlib.reload(main_win)
        help_file.main_class.open_main_win()
        help_file.main_class.close_edit_win()
