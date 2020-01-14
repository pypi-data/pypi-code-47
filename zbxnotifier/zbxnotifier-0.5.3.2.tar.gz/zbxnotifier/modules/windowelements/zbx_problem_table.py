from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from zbxnotifier.modules.alertgenerator import AlertGenerator
from zbxnotifier.modules.settings import Settings
import logging

logger = logging.getLogger('basic')


class ZbxProblemTable(QTableWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Current Zabbix Alerts")
        self.resize(400, 250)

        self.problems = []
        self.init_table()

        self.alert_generator = AlertGenerator()

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

    @staticmethod
    def _color_str_to_list(color):
        colors = []
        for color in color.split(':'):
            colors.append(int(color))
        return colors

    @staticmethod
    def _get_bg_color(severity):
        logger.debug("BG Color. severity: " + str(severity))
        if severity == '0':
            return ZbxProblemTable._color_str_to_list(Settings.config.get('ProblemColors', 'not_classified'))
        elif severity == '1':
            return ZbxProblemTable._color_str_to_list(Settings.config.get('ProblemColors', 'information'))
        elif severity == '2':
            return ZbxProblemTable._color_str_to_list(Settings.config.get('ProblemColors', 'warning'))
        elif severity == '3':
            return ZbxProblemTable._color_str_to_list(Settings.config.get('ProblemColors', 'average'))
        elif severity == '4':
            return ZbxProblemTable._color_str_to_list(Settings.config.get('ProblemColors', 'high'))
        elif severity == '5':
            return ZbxProblemTable._color_str_to_list(Settings.config.get('ProblemColors', 'disaster'))
        logger.critical("Invalid severity received, can't decode to color: " + str(severity))
        return [0, 0, 0]

    def update_data(self, problems):
        """
        Updates data list only, if there's a difference in it.
        :param problems:
        :return:
        """
        if self.problems is not None and problems is not None:
            self.problems.sort()
            problems.sort()

        if self.problems != problems:
            self.alert_generator.add_alert("New Zabbix alert created.", "Please check the alerts for more information.")

            self.problems = self.filter_problems(problems)
            self._set_rows()
            self._refresh_data()

    def filter_problems(self, new_problems):
        filtered = []
        try:
            for problem in new_problems:
                if int(problem.trigger.severity) >= int(Settings.config.get('AlertFilter', 'min-severity')):
                    filtered.append(problem)
        except Exception as e:
            print(e)

    def _refresh_data(self):
        row = 0
        for problem in self.problems:
            severity = problem.trigger.severity_desc
            hostnames = []
            for host in problem.event.hosts:
                hostnames.append(host.hostname)

            severity = QTableWidgetItem(severity)
            severity.setBackground(QColor(*ZbxProblemTable._get_bg_color(problem.trigger.severity)))

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
        self.setRowCount(len(self.problems))

