from zbxnotifier.modules.settings import Settings
from zbxnotifier.modules.windowelements.zbx_problem_table import ZbxProblemTable
from zbxnotifier.modules.zabbix.problems import ProblemsWorker
from zbxnotifier.modules.windowelements.statusbar import StatusWorker
from zbxnotifier.modules.windowelements.statusbar import Statusbar
import logging
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer, QThreadPool

logger = logging.getLogger('basic')


class MainWindow(QMainWindow):
    def __init__(self, signal_queue, parent=None):
        self.signal_queue = signal_queue
        logger.info("Initializing main window and elements")
        super().__init__(parent)

        self.setWindowTitle(Settings.config.get('WindowSettings', 'title'))
        self.window().resize(int(Settings.config.get('WindowSettings', 'width')), int(Settings.config.get('WindowSettings', 'height')))

        self.init_ui()

        self.problem_table_timer = QTimer()
        self.problem_table_timer.setInterval(1000)
        self.problem_table_timer.timeout.connect(self.update_problem_table_worker)
        self.problem_table_timer.start()

        self.statusbar_timer = QTimer()
        self.statusbar_timer.setInterval(500)
        self.statusbar_timer.timeout.connect(self.update_bar_worker)
        self.statusbar_timer.start()

    def init_ui(self):
        self._create_central_widget()
        self._create_statusbar()

        self.threadpool = QThreadPool()
        logger.info("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def _create_central_widget(self):
        """
        Initial setup of the widgets
        :return:
        """
        self.zbx_problem_table = ZbxProblemTable()
        self.setCentralWidget(self.zbx_problem_table)

    def _create_statusbar(self):
        self.statusbar = Statusbar()
        self.setStatusBar(self.statusbar)

    def update_bar_worker(self):
        worker = StatusWorker()
        worker.signals.result.connect(self.update_bar)

        self.threadpool.start(worker)

    def update_bar(self):
        self.statusbar.update_elements()

    def update_problem_table_worker(self):
        worker = ProblemsWorker()
        worker.signals.result.connect(self.update_problem_table)

        self.threadpool.start(worker)

    def update_problem_table(self, data):
        self.zbx_problem_table.update_data(data)
        self.update()

        self.size()

    def closeEvent(self, *args, **kwargs):
        logger.info("Shutting down the application")
        self.signal_queue.put(object())








