from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from zbxnotifier.modules.alertgenerator import AlertGenerator
from zbxnotifier.modules.settings import Settings
import logging
from datetime import datetime
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

    def update_data(self, actual_problems):
        """
        Updates data list only, if there's a difference in it.
        :param problems:
        :return:
        """
        actual_problems = self.filter_problems(actual_problems)

        self.problems.sort()
        actual_problems.sort()

        # Do we have new problems? -> if yes, then create an alert
        resolved_problems = set(self.problems) - set(actual_problems)
        new_problems = set(actual_problems) - set(self.problems)

        self.problems = actual_problems

        # If we have new problems:
        if len(new_problems) > 0:
            logging.debug("New alert detected, creating alert notirication(s).")
            self.alert_generator.add_alert("Zabbix alert notification",
                                           "New Zabbix alert received. Please check the alerts for more information.")

        if len(new_problems) > 0 or len(resolved_problems) > 0:
            logging.debug("Difference found in the problem lists, re-drawing problem list.")
            self._set_rows()
            self._refresh_data()

    def filter_problems(self, new_problems):
        filtered = []
        for problem in new_problems:
            if int(problem.trigger.severity) >= int(Settings.config.get('AlertFilter', 'min-severity')):
                filtered.append(problem)
        return filtered

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

            problem_clock = QTableWidgetItem(self._timestamp_to_str(problem.clock))
            trigger_description = QTableWidgetItem(problem.trigger.description)

            self.setItem(row, 0, problem_clock)
            self.setItem(row, 1, severity)
            self.setItem(row, 3, hostname)
            self.setItem(row, 4, trigger_description)
            row = row + 1
        self.update()
        self.show()

    def _timestamp_to_str(self, timestamp):
        return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

    def _set_rows(self):
        self.setRowCount(len(self.problems))

