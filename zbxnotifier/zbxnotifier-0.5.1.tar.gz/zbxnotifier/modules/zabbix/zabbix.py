from pyzabbix.api import ZabbixAPI
from zbxnotifier.modules.settings import Settings
from zbxnotifier.modules.zabbix.elements import Trigger, Problem, Event, Host
from pyzabbix.api import ZabbixAPIException


class ZabbixConnection:
    connection = None
    token = None
    error = False
    error_message = ""

    @staticmethod
    def init():
        if ZabbixConnection.connection is None:
            try:
                ZabbixConnection.error = True
                ZabbixConnection.error_message = "Connecting..."
                ZabbixConnection.connection = ZabbixAPI(url=Settings.config.get('ZabbixSettings', 'server'), user=Settings.config.get('ZabbixSettings', 'username'), password=Settings.config.get('ZabbixSettings', 'password'))
                ZabbixConnection.token = ZabbixConnection.connection.auth
                ZabbixConnection.error_message = ""
                ZabbixConnection.error = False
            except ZabbixAPIException as e:
                ZabbixConnection.error = True
                ZabbixConnection.error_message = e.data

    @staticmethod
    def re_init():
        ZabbixConnection.connection = None
        ZabbixConnection.token = None
        ZabbixConnection.error = True
        ZabbixConnection.error_message = "Connection re-initializing"
        ZabbixConnection.init()

    @staticmethod
    def get_status_desc():
        if ZabbixConnection.connection is not None and ZabbixConnection.token is not None and ZabbixConnection.error is False:
            return "Connected"
        elif ZabbixConnection.connection is None and ZabbixConnection.token is None and ZabbixConnection.error is False:
            return "Logging in"
        elif ZabbixConnection.connection is None and ZabbixConnection.token is None and ZabbixConnection.error is True:
            return "Error: " + str(ZabbixConnection.error_message)
        return "Disconnected"

    @staticmethod
    def is_connected():
        if ZabbixConnection.connection is None:
            return False
        return True


class Zabbix:

    def __init__(self):
        ZabbixConnection.init()

    def get_problems(self):
        """
        Problems give object ids.
        If object is X, object id is:
            X=0: trigger
            X=4: item
            X=5 LLD rule
        :return: object_id list
        """
        data = ZabbixConnection.connection.problem.get(output='extend', selectAcknowledges="extend", selectTags="extend", selectSuppressionData="extend")
        problems = []
        for problem in data:
            problems.append(Problem(problem.get('objectid'), problem.get('clock')))
        return problems

    def get_events(self, trigger_ids):
        """
        Gets and event based on the event id
        objectid is always a trigger
        :param event_id:
        :return:
        """
        data = ZabbixConnection.connection.event.get(output="extend", objectids=trigger_ids, selectHosts="extend")
        events = []
        for event in data:
            hosts = []
            for host in event.get('hosts'):
                hosts.append(Host(host.get('name'), host.get('hostid')))
            events.append(Event(event.get('objectid'), event.get('eventid'), hosts))

        return events

    def get_triggers(self, trigger_ids):
        """
        Returns a trigger based on the trigger_id
        :param trigger_id:
        :return:
        """
        data = ZabbixConnection.connection.trigger.get(output="extend", triggerids=trigger_ids, expandDescription=True, status=0)
        triggers = []
        for trigger in data:
            triggers.append(Trigger(trigger.get('triggerid'), trigger.get('description'), trigger.get('priority'), trigger.get('lastchange')))

        return triggers




