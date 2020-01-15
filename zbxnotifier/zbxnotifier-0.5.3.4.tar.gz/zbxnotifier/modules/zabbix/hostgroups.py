from zbxnotifier.modules.zabbix.zabbix import Zabbix, ZabbixConnection
import sys
from threading import Thread
import time


class HostGroups(Thread):
    groups = None
    initialized = False

    def __init__(self):
        super(HostGroups, self).__init__()
        self.zbx = Zabbix()
        HostGroups.groups = []

    def run(self):
        try:
            HostGroups.groups = self._get_host_group()
            HostGroups.initialized = True
        except:
            (type, value, traceback) = sys.exc_info()
            print(type)
            print(value)

    def _get_host_group(self):
        while True:
            if ZabbixConnection.connection is not None and ZabbixConnection.error is False:
                return self.zbx.get_hostgroups()
            else:
                time.sleep(5)
