import shelve
import sqlite3
import main_win
import edit_win
import week_win
import notice_win

list_of_days = list()

active_time = ''


# функция, которая ставит на все значение по умолчанию
def clean_data():
    data = shelve.open('saves data\\data')
    for name in ('day0_', 'day1_', 'day2_', 'day3_'):
        data[name + 'name'] = 'название'
        data[name + 'year'] = 'год'
        data[name + 'month'] = 'месяц'
        data[name + 'day'] = 'день'
        data[name + 'hour'] = 'час'
        data[name + 'minutes'] = 'минуты'
    data.close()

    data = shelve.open('saves data\\data')
    for name in ('week0_', 'week1_', 'week2_', 'week3_'):
        data[name + 'name'] = 'название'
        data[name + 'hour'] = 'час'
        data[name + 'minutes'] = 'минуты'
        data[name + 'days'] = 'пн вт ср чт пт сб вс'
        data[name + 'list'] = []
    data.close()


class MainClass:

    def open_main_win(self):
        self.mw = main_win.MainWin()
        self.mw.show()

    def open_edit_win(self):
        self.ew = edit_win.WinOfDays()
        self.ew.show()

    def open_week_win(self):
        self.ww = week_win.WinOfWeek()
        self.ww.show()

    def open_notice_win(self):
        self.ex = notice_win.WinOfNotice()
        self.ex.show()

    def close_main_win(self):
        self.mw.close()

    def close_edit_win(self):
        self.ew.close()

    def close_week_win(self):
        self.ww.close()

    def close_notice_win(self):
        self.ex.close()


class DataBase:
    # создание и запись обязательных строчек для начала работы
    def create_database(self):
        path = 'database.sqlite'
        query = """
            CREATE TABLE IF NOT EXISTS data (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              year INTEGER,
              month INTEGER,
              day INTEGER,
              hour INTEGER,
              minutes INTEGER
            );
            """

        connection = self.create_connection(path)
        self.insert_query(connection, query)  # создание БД

    # подключение к БД (обязательно)
    def create_connection(self, path):
        return sqlite3.connect(path)

    # записать в БД
    def insert_query(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    # прочитать из БД
    def pull_query(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


main_class = MainClass()
database = DataBase()
