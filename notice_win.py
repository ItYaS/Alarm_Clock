from PyQt5 import QtWidgets
from GUI.exit_alarm_tool import Ui_MainWindow
import help_file


class WinOfNotice(QtWidgets.QMainWindow):
    def __init__(self):
        super(WinOfNotice, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        data = help_file.database.pull_query(help_file.active_path)
        turpl = data[0]

        self.ui.name.setText(turpl[1])
        self.ui.date.setText(turpl[2])
        self.ui.time.setText('время: {}:{}'.format(turpl[3], turpl[4]))

        self.ui.pushButton.clicked.connect(self.close_win)

    # функция закрытие окна
    def close_win(self):
        query = f"""
                    UPDATE data SET
                        name = NULL,
                        days = NULL,
                        hour = NULL,
                        minutes = NULL
                    WHERE id = {int(help_file.active_id)}
                """
        help_file.database.insert_query('day.sqlite', query)
        # вызов исключения для закрытия окна
        raise NameError
