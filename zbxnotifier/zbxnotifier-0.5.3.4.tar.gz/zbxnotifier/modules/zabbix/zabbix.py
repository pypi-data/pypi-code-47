from pyzabbix.api import ZabbixAPI
from zbxnotifier.modules.settings import Settings
from zbxnotifier.modules.zabbix.elements import Trigger, Problem, Event, Host, HostGroup
from pyzabbix.api import ZabbixAPIException
import time
import logging

logger = logging.getLogger('basic')

class ZabbixConnection:

    connect = True
    connection = None
    token = None

    error = False
    error_message = ""

    retry_num = 0
    backoff_num = 1

    @staticmethod
    def get_user_data(logger):
        # Get user/server related data
        url = Settings.config.get('ZabbixSettings', 'server')
        username = Settings.config.get('ZabbixSettings', 'username')
        password = Settings.config.get('ZabbixSettings', 'password')

        # Check, if the required data is even set.
        if url == "" or username == "" or password == "":
            logger.warning("Url of Username or Password is empty. Auth process is disabled until further user changes.")
            ZabbixConnection.error = True
            ZabbixConnection.connect = False
            ZabbixConnection.error_message = "Please set Username, Password and Server URL in Settings!"
            raise ValueError

        return url, username, password

    @staticmethod
    def connect_thread(logger, queue):
        logger.info("Starting connection thread")
        while queue.empty():
            time.sleep(2)

            # The whole authentication process can be disabled
            if ZabbixConnection.connect is False:
                continue

            try:
                url, username, password = ZabbixConnection.get_user_data(logger)
            except ValueError:
                continue

            if ZabbixConnection.connection is None or ZabbixConnection.error is True:
                # Set message, as we are connecting
                ZabbixConnection.error = True
                ZabbixConnection.error_message = "Connecting..."

                logger.debug("New login cycle has been started to server: " + str(url))
                try:
                    logger.debug("Executing ZabbixAPI connection")
                    ZabbixConnection.connection = ZabbixAPI(url=url, user=username, password=password)
                except ZabbixAPIException as e:
                    logger.warning("Failed to connect to the ZabbixAPI: " + str(e.data))
                    ZabbixConnection.error = True
                    ZabbixConnection.error_message = e.data
                    ZabbixConnection.retry_num += 1
                    if "name or password is incorr" in e.data:
                        logger.critical("Login name or password is incorrect. Logging process is disabled now until user changes credentials.")
                        ZabbixConnection.error_message += " Logging process disabled until user changes credentials in settings."
                        ZabbixConnection.connect = False
                        continue
                except Exception as e:
                    logger.warning("Failed to connect to the Server: " + str(e))
                    ZabbixConnection.error = True
                    ZabbixConnection.error_message = str(e)
                    ZabbixConnection.retry_num += 1
                else:
                    logger.info("Successfully connected to the server: " + str(url))
                    ZabbixConnection.token = ZabbixConnection.connection.auth
                    ZabbixConnection.error_message = ""
                    ZabbixConnection.error = False

                    ZabbixConnection.retry_num = 0
                    ZabbixConnection.backoff_num = 1

                if ZabbixConnection.retry_num / ZabbixConnection.backoff_num > 3:
                    logger.debug("Backoff limit reached. Waiting for 10 seconds to retry. ")
                    ZabbixConnection.error_message += " Backoff limit reached, retying after 10 seconds.."
                    time.sleep(10)
                    ZabbixConnection.backoff_num += 1

        logger.info("Shutting down ZabbixAPI Connection...")
        ZabbixConnection.connection.user.logout()
        logger.info("Connection shut down.")

    @staticmethod
    def re_init():
        logger.info("Re-initializing Zabbix connection triggered.")
        ZabbixConnection.connection = None
        ZabbixConnection.token = None
        ZabbixConnection.error = True
        ZabbixConnection.error_message = "Connection re-initializing"
        ZabbixConnection.connect = True

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

    def get_hostgroups(self, groupids=None):
        """
        Returns a list of hostgroups, which are available for the user
        :return:
        """
        if groupids is None:
            data = ZabbixConnection.connection.hostgroup.get(output='extend')
        else:
            data = ZabbixConnection.connection.hostgroup.get(output='extend', groupids=groupids)

        host_groups = []
        for hostgroup in data:
            host_groups.append(HostGroup(hostgroup.get('groupid'), hostgroup.get('name')))
        return host_groups

    def get_hosts(self, groupids=None):
        if groupids is None:
            data = ZabbixConnection.connection.host.get(output='extend')
        else:
            data = ZabbixConnection.connection.host.get(output='extend', groupids=groupids)

        hosts = []
        for host in data:
            hosts.append(Host(host.get('host'), host.get('hostid')))
        return hosts

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




