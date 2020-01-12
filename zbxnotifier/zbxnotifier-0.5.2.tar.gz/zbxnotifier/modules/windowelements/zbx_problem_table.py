from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ZbxProblemTable(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Current Zabbix Alerts")
        self.resize(400, 250)

        self.problems = []
        self.init_table()

    def init_table(self):
        """
        Initial setup of the table. Sets the column headers.
        :return:
        """
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(['Time', 'Severity', 'Status', 'Host', 'Problem', 'Duration'])

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)
        header.setSectionResizeMode(5, QHeaderView.Stretch)

        self._set_rows()

    def _get_bg_color(self, severity):
        if severity == '1':
            return [151, 170, 179]
        elif severity == '2':
            return [116, 153, 255]
        elif severity == '3':
            return [255, 200, 89]
        elif severity == '4':
            return [255, 160, 89]
        elif severity == '5':
            return [233, 118, 89]
        elif severity == '6':
            return [228, 89, 89]

    def update_data(self, problems):
        self.problems = problems
        self._set_rows()
        self._refresh_data()

    def _refresh_data(self):
        row = 0
        for problem in self.problems:
            severity = problem.trigger.severity
            hostnames = []
            for host in problem.event.hosts:
                hostnames.append(host.hostname)

            severity = QTableWidgetItem(severity)
            severity.setBackground(QColor(*self._get_bg_color(problem.trigger.severity)))

            hostname = QTableWidgetItem(', '.join(hostnames))
            problem_clock = QTableWidgetItem(problem.clock)
            trigger_description = QTableWidgetItem(problem.trigger.description)

            self.setItem(row, 0, problem_clock)
            self.setItem(row, 1, severity)
            self.setItem(row, 3, hostname)
            self.setItem(row, 4, trigger_description)
            row = row + 1
        self.update()
        self.show()

    def _set_rows(self):
        self.setRowCount(len(self.problems)+1)

