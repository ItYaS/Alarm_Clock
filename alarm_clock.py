import sys
from PyQt5 import QtWidgets
import help_file


# открытие класса с будильниками
app = QtWidgets.QApplication([])
help_file.main_class.open_main_window()

sys.exit(app.exec())  # выключит сам себя
