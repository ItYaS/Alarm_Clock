from PyQt5 import QtWidgets
from GUI.main_window import Ui_MainWindow
import help_file


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.update_screen()  # вывод значений

        # lambda для того чтобы функциям можно было передавать аргументы

        self.ui.add0_0.clicked.connect(lambda: self.open_day_win('1'))
        self.ui.add0_1.clicked.connect(lambda: self.open_day_win('2'))
        self.ui.add0_2.clicked.connect(lambda: self.open_day_win('3'))
        self.ui.add0_3.clicked.connect(lambda: self.open_day_win('4'))

        self.ui.add1_0.clicked.connect(lambda: self.open_week_win('1'))
        self.ui.add1_1.clicked.connect(lambda: self.open_week_win('2'))
        self.ui.add1_2.clicked.connect(lambda: self.open_week_win('3'))
        self.ui.add1_3.clicked.connect(lambda: self.open_week_win('4'))

        day_path = 'data\\day.sqlite'
        self.ui.delete0_0.clicked.connect(lambda: self.delete_data(day_path, '1'))
        self.ui.delete0_1.clicked.connect(lambda: self.delete_data(day_path, '2'))
        self.ui.delete0_2.clicked.connect(lambda: self.delete_data(day_path, '3'))
        self.ui.delete0_3.clicked.connect(lambda: self.delete_data(day_path, '4'))

        week_path = 'data\\week.sqlite'
        self.ui.delete1_0.clicked.connect(lambda: self.delete_data(week_path, '1'))
        self.ui.delete1_1.clicked.connect(lambda: self.delete_data(week_path, '2'))
        self.ui.delete1_2.clicked.connect(lambda: self.delete_data(week_path, '3'))
        self.ui.delete1_3.clicked.connect(lambda: self.delete_data(week_path, '4'))

    def update_screen(self):
        day_data = help_file.database.pull_data('data\\day.sqlite')
        week_data = help_file.database.pull_data('data\\week.sqlite')

        self.ui.name0_0.setText(day_data[0][1])
        self.ui.date0_0.setText(day_data[0][2])
        self.ui.time0_0.setText('{}:{}'.format(day_data[0][3], day_data[0][4]))
        self.ui.name0_1.setText(day_data[1][1])
        self.ui.date0_1.setText(day_data[1][2])
        self.ui.time0_1.setText('{}:{}'.format(day_data[1][3], day_data[1][4]))
        self.ui.name0_2.setText(day_data[2][1])
        self.ui.date0_2.setText(day_data[2][2])
        self.ui.time0_2.setText('{}:{}'.format(day_data[2][3], day_data[2][4]))
        self.ui.name0_3.setText(day_data[3][1])
        self.ui.date0_3.setText(day_data[3][2])
        self.ui.time0_3.setText('{}:{}'.format(day_data[3][3], day_data[3][4]))

        self.ui.name1_0.setText(week_data[0][1])
        self.ui.date1_0.setText(week_data[0][2])
        self.ui.time1_0.setText('{}:{}'.format(week_data[0][3], week_data[0][4]))
        self.ui.name1_1.setText(week_data[1][1])
        self.ui.date1_1.setText(week_data[1][2])
        self.ui.time1_1.setText('{}:{}'.format(week_data[1][3], week_data[1][4]))
        self.ui.name1_2.setText(week_data[2][1])
        self.ui.date1_2.setText(week_data[2][2])
        self.ui.time1_2.setText('{}:{}'.format(week_data[2][3], week_data[2][4]))
        self.ui.name1_3.setText(week_data[3][1])
        self.ui.date1_3.setText(week_data[3][2])
        self.ui.time1_3.setText('{}:{}'.format(week_data[3][3], week_data[3][4]))

    def open_day_win(self, active_data):
        # использование аргумента для определения пути
        help_file.active_id = active_data
        help_file.main_class.open_day_win()

    def open_week_win(self, active_id):
        # использование аргумента для определения id данных в БД
        help_file.active_id = active_id
        help_file.main_class.open_week_win()

    def delete_data(self, path, active_id):
        query = f"""
                    UPDATE data SET
                        name = 'undefined',
                        days = 'undefined',
                        hour = 'undefined',
                        minutes = 'undefined'
                    WHERE id = {active_id}
                """
        help_file.database.update_data(path, query)

        self.update_screen()
