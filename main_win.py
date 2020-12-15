import shelve
from PyQt5 import QtWidgets, QtGui
from GUI.main_window import Ui_MainWindow
import help_file


class MainWin(QtWidgets.QMainWindow):
    # конструктор
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Main window')
        self.setWindowIcon(QtGui.QIcon('more\\image.jpg'))

        # вывод значений
        self.edit_label()

        # кнопки добавления будильника
        self.ui.edit0_0.clicked.connect(lambda: self.open_day_win('1'))
        self.ui.edit0_1.clicked.connect(lambda: self.open_day_win('2'))
        self.ui.edit0_2.clicked.connect(lambda: self.open_day_win('3'))
        self.ui.edit0_3.clicked.connect(lambda: self.open_day_win('4'))

        self.ui.edit1_0.clicked.connect(lambda: self.open_week_win('1'))
        self.ui.edit1_1.clicked.connect(lambda: self.open_week_win('2'))
        self.ui.edit1_2.clicked.connect(lambda: self.open_week_win('3'))
        self.ui.edit1_3.clicked.connect(lambda: self.open_week_win('4'))

        # кнопки удаления будильников
        self.ui.delete0_0.clicked.connect(lambda: self.del_data('1'))
        self.ui.delete0_1.clicked.connect(lambda: self.del_data('2'))
        self.ui.delete0_2.clicked.connect(lambda: self.del_data('3'))
        self.ui.delete0_3.clicked.connect(lambda: self.del_data('4'))

        self.ui.delete1_0.clicked.connect(lambda: self.del_data('1'))
        self.ui.delete1_1.clicked.connect(lambda: self.del_data('2'))
        self.ui.delete1_2.clicked.connect(lambda: self.del_data('3'))
        self.ui.delete1_3.clicked.connect(lambda: self.del_data('4'))

    # функция вывода значений
    def edit_label(self):
        data = shelve.open('saves data\\data')

        self.ui.name0_0.setText(data['day0_name'])
        self.ui.date0_0.setText('{}.{}.{}'.format(data['day0_day'], data['day0_month'], data['day0_year']))
        self.ui.time0_0.setText('{}:{}'.format(data['day0_hour'], data['day0_minutes']))
        self.ui.name0_1.setText(data['day1_name'])
        self.ui.date0_1.setText('{}.{}.{}'.format(data['day1_day'], data['day1_month'], data['day1_year']))
        self.ui.time0_1.setText('{}:{}'.format(data['day1_hour'], data['day1_minutes']))
        self.ui.name0_2.setText(data['day2_name'])
        self.ui.date0_2.setText('{}.{}.{}'.format(data['day2_day'], data['day2_month'], data['day2_year']))
        self.ui.time0_2.setText('{}:{}'.format(data['day2_hour'], data['day2_minutes']))
        self.ui.name0_3.setText(data['day3_name'])
        self.ui.date0_3.setText('{}.{}.{}'.format(data['day3_day'], data['day3_month'], data['day3_year']))
        self.ui.time0_3.setText('{}:{}'.format(data['day3_hour'], data['day3_minutes']))

        self.ui.name1_0.setText(data['week0_name'])
        self.ui.date1_0.setText(data['week0_days'])
        self.ui.time1_0.setText('{}:{}'.format(data['week0_hour'], data['week0_minutes']))
        self.ui.name1_1.setText(data['week1_name'])
        self.ui.date1_1.setText(data['week1_days'])
        self.ui.time1_1.setText('{}:{}'.format(data['week1_hour'], data['week1_minutes']))
        self.ui.name1_2.setText(data['week2_name'])
        self.ui.date1_2.setText(data['week2_days'])
        self.ui.time1_2.setText('{}:{}'.format(data['week2_hour'], data['week2_minutes']))
        self.ui.name1_3.setText(data['week3_name'])
        self.ui.date1_3.setText(data['week3_days'])
        self.ui.time1_3.setText('{}:{}'.format(data['week3_hour'], data['week3_minutes']))

        data.close()

    # функция открытия окна редактирования
    def open_day_win(self, active_data):
        # использование аргумента для определения пути
        help_file.active_time = active_data
        # открытие окна с редактированием будильника
        help_file.main_class.open_edit_win()

    # функция открытия окна с неделями
    def open_week_win(self, active_data):
        # использование аргумента для определения пути
        help_file.active_time = active_data
        # открытие окна с редактированием будильника
        help_file.main_class.open_week_win()

    # функция изменения значений первого окна в БД на значения по умолчанию
    def del_data(self, active_data):
        # открытие базы данных
        data = shelve.open('saves data\\data')
        path = str(active_data)
        data[path + 'name'] = 'название'
        data[path + 'year'] = 'год'
        data[path + 'month'] = 'месяц'
        data[path + 'day'] = 'день'
        data[path + 'hour'] = 'час'
        data[path + 'minutes'] = 'минуты'
        data[path + 'days'] = 'пн вт ср чт пт сб вс'
        # закрытие базы данных
        data.close()
        self.edit_label()
