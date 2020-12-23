import importlib
from PyQt5 import QtWidgets, QtGui, QtCore
from GUI.day_window import Ui_MainWindow
import help_file
import main_win


class WinOfDays(QtWidgets.QMainWindow):
    def __init__(self):
        super(WinOfDays, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.save_button.clicked.connect(self.save_and_close)

    def save_and_close(self):
        query = f"""
                    UPDATE data SET 
                         name = '{self.ui.name.text()}',
                         days = '{self.ui.day.text()}.{self.ui.month.text()}.{self.ui.year.text()}',
                         hour = '{self.ui.hour.text()}',
                         minutes = '{self.ui.minutes.text()}'
                    WHERE id = {help_file.active_id}
                """
        help_file.database.update_data('data\\day.sqlite', query)

        # закрытие окон и открытие обновленного main_win
        help_file.main_class.close_main_win()
        importlib.reload(main_win)
        help_file.main_class.open_main_win()
        help_file.main_class.close_day_win()
