from PyQt5.QtWidgets import QApplication
from threading import Thread
import sys
import logging

from zbxnotifier.modules.windowelements.main_window import MainWindow
from zbxnotifier.modules.settings import Settings
from zbxnotifier.modules.zabbix.zabbix import ZabbixConnection
from zbxnotifier.modules.logging import Logging
import queue


class Application:
    def __init__(self):
        signal_queue = queue.Queue()

        logger = logging.getLogger('basic')
        logger.info("Starting application")

        Settings.init_basic_config()
        Logging.init()
        Settings.init_rest_config()
        Logging.change_level(Settings.config.get('Application', 'LogLevel'))

        app = QApplication(sys.argv)

        zbx_conn_thread = Thread(target=ZabbixConnection().connect_thread, args=[logger, signal_queue])
        zbx_conn_thread.start()


        window = MainWindow(signal_queue)
        window.show()

        sys.exit(app.exec())

