import shelve
from PyQt5 import QtWidgets
from GUI.exit_alarm_tool import Ui_MainWindow
import help_file


class WinOfNotice(QtWidgets.QMainWindow):
    def __init__(self):
        super(WinOfNotice, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        data = shelve.open('saves data\\data')

        self.ui.name.setText(data['act_name'])
        self.ui.date.setText('{}.{}.{}'.format(data['act_day'], data['act_month'], data['act_year']))
        self.ui.days.setText('{}'.format(data['act_days']))
        self.ui.time.setText('время: {}:{}'.format(data['act_hour'], data['act_minutes']))

        self.ui.pushButton.clicked.connect(self.just_close)

    # функция закрытие окна
    def just_close(self):
        data = shelve.open('saves data\\data')
        path = help_file.active_time
        data[path + 'name'] = 'название'
        data[path + 'year'] = 'год'
        data[path + 'month'] = 'месяц'
        data[path + 'day'] = 'день'
        data[path + 'hour'] = 'час'
        data[path + 'minutes'] = 'минуты'
        data[path + 'days'] = 'пн вт ср чт пт сб вс'
        data.close()
        # вызов исключения для закрытия окна
        raise NameError
