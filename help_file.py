import sqlite3
import main_win
import day_win
import week_win
import notice_win


active_id = None  # id данных, которые нужно изменить в другом окне
active_path = ''  # путь БД с которой надо работать в других окнах


class MainClass:
    def open_main_win(self):
        self.MainWin = main_win.MainWin()
        self.MainWin.show()

    def open_day_win(self):
        self.DayWin = day_win.WinOfDays()
        self.DayWin.show()

    def open_week_win(self):
        self.WeekWin = week_win.WinOfWeek()
        self.WeekWin.show()

    def open_notice_win(self):
        self.NoticeWin = notice_win.WinOfNotice()
        self.NoticeWin.show()

    def close_main_win(self):
        self.MainWin.close()

    def close_day_win(self):
        self.DayWin.close()

    def close_week_win(self):
        self.WeekWin.close()

    def close_notice_win(self):
        self.NoticeWin.close()


class DataBase:
    # удаление и обновление БД
    def create_database(self):
        # удаление всех данных и таблиц
        del_query = 'DROP TABLE data'

        self.update_data('data\\day.sqlite', del_query)
        self.update_data('data\\week.sqlite', del_query)

        # создание таблиц
        table = """
                    CREATE TABLE IF NOT EXISTS data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        days DATE,
                        hour TEXT,
                        minutes TEXT
                    );
                """

        self.update_data('data\\day.sqlite', table)
        self.update_data('data\\week.sqlite', table)

        # добавление данных по умолчанию
        query = """
                    INSERT INTO
                        data (name, days, hour, minutes)
                    VALUES
                        ('undefined', 'undefined', 'undefined', 'undefined');
                """

        database.update_data('data\\day.sqlite', query)
        database.update_data('data\\day.sqlite', query)
        database.update_data('data\\day.sqlite', query)
        database.update_data('data\\day.sqlite', query)
        # потому что только одну операцию можно делать за один раз
        database.update_data('data\\week.sqlite', query)
        database.update_data('data\\week.sqlite', query)
        database.update_data('data\\week.sqlite', query)
        database.update_data('data\\week.sqlite', query)

    def create_connection(self, path):
        return sqlite3.connect(path)

    def update_data(self, path, query):
        connection = self.create_connection(path)

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def pull_data(self, path):
        query = 'SELECT * from data'
        connection = self.create_connection(path)

        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


main_class = MainClass()
database = DataBase()

if __name__ == '__main__':
    database.create_database()

    day_data = database.pull_data('data\\day.sqlite')
    week_data = database.pull_data('data\\week.sqlite')

    print(day_data)
    print(week_data)
