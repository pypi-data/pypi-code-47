import sys
from zbxnotifier.modules.windowelements.main_window import MainWindow
from zbxnotifier.modules.settings import Settings
from PyQt5.QtWidgets import QApplication


class Application:
    def __init__(self):
        app = QApplication(sys.argv)

        Settings.init_config()

        window = MainWindow()
        window.show()

        sys.exit(app.exec())

