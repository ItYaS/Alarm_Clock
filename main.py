import sys
import shelve
import pygame
import datetime
from PyQt5 import QtWidgets
import notice_win
import help_file

# перевод данных в целочисленный тип
data = shelve.open('saves data\\data')

# перевод значений окон первого вида
try:
    name0 = data['day0_name']
    year0 = int(data['day0_year'])
    month0 = int(data['day0_month'])
    day0 = int(data['day0_day'])
    hour0 = int(data['day0_hour'])
    minute0 = int(data['day0_minutes'])
except (TypeError, ValueError):
    name0 = ''
    year0 = 0
    month0 = 0
    day0 = 0
    hour0 = 0
    minute0 = 0

try:
    name1 = data['day1_name']
    year1 = int(data['day1_year'])
    month1 = int(data['day1_month'])
    day1 = int(data['day1_day'])
    hour1 = int(data['day1_hour'])
    minute1 = int(data['day1_minutes'])
except (TypeError, ValueError):
    name1 = ''
    year1 = 0
    month1 = 0
    day1 = 0
    hour1 = 0
    minute1 = 0

try:
    name2 = data['day2_name']
    year2 = int(data['day2_year'])
    month2 = int(data['day2_month'])
    day2 = int(data['day2_day'])
    hour2 = int(data['day2_hour'])
    minute2 = int(data['day2_minutes'])
except (TypeError, ValueError):
    name2 = ''
    year2 = 0
    month2 = 0
    day2 = 0
    hour2 = 0
    minute2 = 0

try:
    name3 = data['day3_name']
    year3 = int(data['day3_year'])
    month3 = int(data['day3_month'])
    day3 = int(data['day3_day'])
    hour3 = int(data['day3_hour'])
    minute3 = int(data['day3_minutes'])
except (TypeError, ValueError):
    name3 = ''
    year3 = 0
    month3 = 0
    day3 = 0
    hour3 = 0
    minute3 = 0

# перевод значений окон второго вида
try:
    week_name0 = data['week0_name']
    list_week_days0 = data['week0_list']
    str_days0 = data['week0_days']
    week_hour0 = int(data['week0_hour'])
    week_minute0 = int(data['week0_minutes'])
    win0 = True
except (TypeError, ValueError):
    week_name0 = 0
    list_week_days0 = []
    str_days0 = ''
    week_hour0 = 0
    week_minute0 = 0

try:
    week_name1 = data['week1_name']
    list_week_days1 = data['week1_list']
    str_days1 = data['week1_days']
    week_hour1 = int(data['week1_hour'])
    week_minute1 = int(data['week1_minutes'])
    win1 = True
except (TypeError, ValueError):
    week_name1 = 0
    list_week_days1 = []
    str_days1 = ''
    week_hour1 = 0
    week_minute1 = 0

try:
    week_name2 = data['week2_name']
    list_week_days2 = data['week2_list']
    str_days2 = data['week2_days']
    week_hour2 = int(data['week2_hour'])
    week_minute2 = int(data['week2_minutes'])
    win2 = True
except (TypeError, ValueError):
    week_name2 = 0
    list_week_days2 = []
    str_days2 = ''
    week_hour2 = 0
    week_minute2 = 0

try:
    week_name3 = data['week3_name']
    list_week_days3 = data['week3_list']
    str_days3 = data['week3_days']
    week_hour3 = int(data['week3_hour'])
    week_minute3 = int(data['week3_minutes'])
    win3 = True
except (TypeError, ValueError):
    week_name3 = 0
    list_week_days3 = []
    str_days3 = ''
    week_hour3 = 0
    week_minute3 = 0

data.close()


def func_main_alg():
    # алгоритм проверки на время
    while True:
        # значения, которые будут меняться
        now_year = datetime.datetime.now().year
        now_month = datetime.datetime.now().month
        week_day = datetime.date.today().strftime('%w')
        now_day = datetime.datetime.now().day
        now_hour = datetime.datetime.now().hour
        now_minute = datetime.datetime.now().minute

        # проверка значений окон первого вида
        if (year0 == now_year and month0 == now_month
                and day0 == now_day and hour0 == now_hour
                and minute0 == now_minute):
            help_file.active_time = 'day0_'
            data = shelve.open('saves data\\data')
            data['act_name'] = name0
            data['act_year'] = year0
            data['act_month'] = month0
            data['act_days'] = ''
            data['act_day'] = day0
            data['act_hour'] = hour0
            data['act_minutes'] = minute0
            data.close()
            break
        # вторые значения
        if (year1 == now_year and month1 == now_month
                and day1 == now_day and hour1 == now_hour
                and minute1 == now_minute):
            help_file.active_time = 'day1_'
            data = shelve.open('saves data\\data')
            data['act_name'] = name1
            data['act_year'] = year1
            data['act_month'] = month1
            data['act_days'] = ''
            data['act_day'] = day1
            data['act_hour'] = hour1
            data['act_minutes'] = minute1
            data.close()
            break
        # третие значения
        if (year2 == now_year and month2 == now_month
                and day2 == now_day and hour2 == now_hour
                and minute2 == now_minute):
            help_file.active_time = 'day2_'
            data = shelve.open('saves data\\data')
            data['act_name'] = name2
            data['act_year'] = year2
            data['act_month'] = month2
            data['act_days'] = ''
            data['act_day'] = day2
            data['act_hour'] = hour2
            data['act_minutes'] = minute2
            data.close()
            break
        # четвертые значения
        if (year3 == now_year and month3 == now_month
                and day3 == now_day and hour3 == now_hour
                and minute3 == now_minute):
            help_file.active_time = 'day3_'
            data = shelve.open('saves data\\data')
            data['act_name'] = name3
            data['act_year'] = year3
            data['act_month'] = month3
            data['act_days'] = ''
            data['act_day'] = day3
            data['act_hour'] = hour3
            data['act_minutes'] = minute3
            data.close()
            break
        # проверка значений окон второго вида
        if int(week_day) in list_week_days0:
            if week_hour0 == now_hour and week_minute0 == now_minute:
                help_file.active_time = 'week0_'
                data = shelve.open('saves data\\data')
                data['act_name'] = week_name0
                data['act_year'] = ''
                data['act_month'] = ''
                data['act_days'] = str_days0
                data['act_day'] = ''
                data['act_hour'] = week_hour0
                data['act_minutes'] = week_minute0
                data.close()
            break
        # вторые значения
        if int(week_day) in list_week_days1:
            if week_hour1 == now_hour and week_minute1 == now_minute:
                help_file.active_time = 'week1_'
                data = shelve.open('saves data\\data')
                data['act_name'] = week_name1
                data['act_year'] = ''
                data['act_month'] = ''
                data['act_days'] = str_days1
                data['act_day'] = ''
                data['act_hour'] = week_hour1
                data['act_minutes'] = week_minute1
                data.close()
            break
        # третие значения
        if int(week_day) in list_week_days2:
            if week_hour2 == now_hour and week_minute2 == now_minute:
                help_file.active_time = 'week2_'
                data = shelve.open('saves data\\data')
                data['act_name'] = week_name2
                data['act_year'] = ''
                data['act_month'] = ''
                data['act_days'] = str_days2
                data['act_day'] = ''
                data['act_hour'] = week_hour2
                data['act_minutes'] = week_minute2
                data.close()
            break
        # четвертые значения
        if int(week_day) in list_week_days3:
            if week_hour3 == now_hour and week_minute3 == now_minute:
                help_file.active_time = 'week3_'
                data = shelve.open('saves data\\data')
                data['act_name'] = week_name3
                data['act_year'] = ''
                data['act_month'] = ''
                data['act_days'] = str_days3
                data['act_day'] = ''
                data['act_hour'] = week_hour3
                data['act_minutes'] = week_minute3
                data.close()
            break
    app = QtWidgets.QApplication([])
    application = notice_win.WinOfNotice()
    application.show()
    # воспроизведение музыки
    pygame.init()
    pygame.mixer.music.load('more\\sound_4_call.mp3')
    pygame.mixer.music.play()
    sys.exit(app.exec())


func_main_alg()
