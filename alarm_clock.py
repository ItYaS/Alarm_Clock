import sys
from PyQt5 import QtWidgets
import help_file


help_file.databases.create_databases()  # подключение БД

# открытие класса с будильниками
app = QtWidgets.QApplication([])
help_file.main_class.open_main_win()

sys.exit(app.exec())  # выключит сам себя
