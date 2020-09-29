import sys
from PyQt5 import QtWidgets
import help_file

# открытие класса с будильниками
app = QtWidgets.QApplication([])
help_file.main_class.open_main_win()
# выключит сам себя (строчка нужна для того, что бы не придумывать
#                    где(и при каком условии) писать закрытие класса)
sys.exit(app.exec())