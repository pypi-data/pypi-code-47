import sys

from PyQt5.QtWidgets import QApplication

from .gui.main import MainWindow
from .settings import Settings


settings = Settings.load("settings.json")

application = QApplication(sys.argv)
main_window = MainWindow(application=application, settings=settings)
main_window.show()

try:
    application.exec_()
finally:
    main_window.keylogger.stop()
