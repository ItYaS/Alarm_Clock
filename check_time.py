import sys
import pygame
import datetime
from PyQt5 import QtWidgets
import notice_win
import help_file


def start_music_and_open_notice_win():
    pygame.init()
    pygame.mixer.music.load('more\\call_sound.mp3')
    pygame.mixer.music.play()

    app = QtWidgets.QApplication([])
    application = notice_win.WinOfNotice()
    application.show()
    sys.exit(app.exec())


while True:

    day_data = help_file.database.pull_data('data\\day.sqlite')
    week_data = help_file.database.pull_data('data\\week.sqlite')

    now_year = datetime.datetime.now().year
    now_month = datetime.datetime.now().month
    week_day = datetime.date.today().strftime('%w')
    now_day = datetime.datetime.now().day
    now_hour = datetime.datetime.now().hour
    now_minute = datetime.datetime.now().minute

    for data in day_data:
        date = data[2].split('.')  # потому что строка такая: DD.MM.YYYY

        if len(date) > 1:  # на случай если строка со значением 'undefined'(значение по умолчанию)
            if (int(date[2]) == now_year and int(date[1]) == now_month
                    and int(date[0]) == now_day and int(data[3]) == now_hour
                    and int(data[4]) == now_minute):
                index = day_data.index(data)  # для того, что бы знать какой кортеж с датой активный

                help_file.active_path = 'data\\day.sqlite'
                help_file.active_id = index + 1
                start_music_and_open_notice_win()

    for data in week_data:
        days = data[2]

        # замена значений на числа, которые можно проверить
        days = days.replace('Mon', '1')
        days = days.replace('Tue', '2')
        days = days.replace('Wed', '3')
        days = days.replace('Thu', '4')
        days = days.replace('Fri', '5')
        days = days.replace('Sat', '6')
        days = days.replace('Sun', '7')

        int_days = days.split()

        if str(week_day) in int_days:
            if int(data[3]) == now_hour and int(data[4]) == now_minute:
                index = week_data.index(data)  # для того, что бы знать какой кортеж с датой активный

                help_file.active_path = 'data\\week.sqlite'
                help_file.active_id = index + 1
                start_music_and_open_notice_win()
