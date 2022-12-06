import sys

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication

from main_window import MainWindow

app = QApplication(sys.argv)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("strokes.sqlite")
db.open()

window = MainWindow(db)
window.show()

app.exec()

db.close()
