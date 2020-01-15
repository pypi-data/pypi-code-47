from PyQt5.QtCore import QRunnable, pyqtSlot
from zbxnotifier.modules.zabbix.zabbix import Zabbix, ZabbixConnection
from zbxnotifier.modules.zabbix.signals import WorkerSignals
from zbxnotifier.modules.zabbix.hostgroups import HostGroups
from zbxnotifier.modules.settings import Settings
import sys
import time


class ProblemsWorker(QRunnable):
    def __init__(self):
        super(ProblemsWorker, self).__init__()
        self.signals = WorkerSignals()
        self.zbx = Zabbix()

    @pyqtSlot()
    def run(self):
        try:
            problems = self.get_problems()
            self.signals.result.emit(problems)
        except:
            (type, value, traceback) = sys.exc_info()
            print(type)
            print(value)

    def get_problems(self):
        # Get all the problems
        if not ZabbixConnection.is_connected():
            return []

        problems = self.zbx.get_problems()

        # Get all the triggers
        trigger_ids = []
        for problem in problems:
            trigger_ids.append(problem.triggerid)
        triggers = self.zbx.get_triggers(trigger_ids)

        for problem in problems:
            for trigger in triggers:
                # Sometimes, there's no trigger id for the problemid
                try:
                    if problem.triggerid == trigger.triggerid:
                        problem.trigger = trigger
                except AttributeError:
                    problem.trigger = None

        # Get all events based on the trigger IDs
        events = self.zbx.get_events(trigger_ids)

        for problem in problems:
            for event in events:
                try:
                    if problem.trigger.triggerid == event.triggerid:
                        problem.event = event
                except AttributeError:
                    problem.event = None

        # Search for faulty problems, when there's no trigger or event
        clear_problems = []
        for problem in problems:
            if problem.trigger is not None and problem.event is not None:
                clear_problems.append(problem)

        return self._filter_by_hostgroup(clear_problems)

    def _filter_by_hostgroup(self, problems):
        hostgroup_to_filter = Settings.config.get('AlertFilter', 'group')
        if hostgroup_to_filter == "":
            return problems

        while HostGroups.initialized is False:
            time.sleep(1)

        filter_group = None
        for hostgroup in HostGroups.groups:
            if hostgroup.name == hostgroup_to_filter:
                filter_group = hostgroup

        hostgroup_hosts = self.zbx.get_hosts(filter_group.groupid)

        filtered_problems = []
        for problem in problems:
            for host in problem.event.hosts:
                if host in hostgroup_hosts:
                    filtered_problems.append(problem)
                    continue

        return filtered_problems