import sqlite3
import main_win
import day_win
import week_win
import notice_win


active_id = 1
active_path = 'data\\day.sqlite'


class MainClass:
    def open_main_win(self):
        self.mw = main_win.MainWin()
        self.mw.show()

    def open_edit_win(self):
        self.ew = day_win.WinOfDays()
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
    # создание БД
    def create_database(self):
        # создание таблицы
        table = """
                    CREATE TABLE IF NOT EXISTS data (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      days DATE,
                      hour INTEGER,
                      minutes INTEGER
                    );
                    """

        self.insert_query('data\\day.sqlite', table)
        self.insert_query('data\\week.sqlite', table)

        # добавление данных по умолчанию
        query = """
                    INSERT INTO
                      data (name, days, hour, minutes)
                    VALUES
                      (NULL, NULL, NULL, NULL);
                    """

        database.insert_query('data\\day.sqlite', query)
        database.insert_query('data\\day.sqlite', query)
        database.insert_query('data\\day.sqlite', query)
        database.insert_query('data\\day.sqlite', query)
        # потому что только по одной операции можно делать
        database.insert_query('data\\week.sqlite', query)
        database.insert_query('data\\week.sqlite', query)
        database.insert_query('data\\week.sqlite', query)
        database.insert_query('data\\week.sqlite', query)

    # подключение к БД
    def create_connection(self, path):
        return sqlite3.connect(path)

    # добавление данных или изменение
    def insert_query(self, path, query):
        connection = self.create_connection(path)

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    # чтение данных
    def pull_query(self, path, query):
        connection = self.create_connection(path)

        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


main_class = MainClass()
database = DataBase()

if __name__ == '__main__':
    database.create_database()

    # изменение данных
    q = """
            UPDATE data SET
                name = 'hey!',
                days = '15.12.2020',
                hour = 12,
                minutes = 01
            WHERE id = 1
        """
    database.insert_query('data\\day.sqlite', q)

    print(database.pull_query('data\\day.sqlite', "SELECT * FROM data"))

    print('______________________________________')
    # вытаскивание конкретных данных по id

    data = database.pull_query(active_path, f"SELECT * FROM data WHERE id={active_id}")
    query = f"""
                UPDATE data SET
                    name = NULL,
                    days = NULL,
                    hour = NULL,
                    minutes = NULL
                WHERE id = 1
            """
    database.insert_query('day.sqlite', query)
    print(database.pull_query('data\\day.sqlite', "SELECT * FROM data"))
