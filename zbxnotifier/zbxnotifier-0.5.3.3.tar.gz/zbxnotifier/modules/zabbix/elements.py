

class Problem:
    def __init__(self, triggerid, clock):
        self.triggerid = triggerid
        self.clock = clock
        self.trigger = None
        self.event = None

    def __str__(self):
        return self.triggerid + " " + self.clock + str(self.trigger)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.triggerid == other.triggerid and self.trigger == other.trigger and self.event == other.event:
            return True
        return False

    def __lt__(self, other):
        if self.triggerid > other.triggerid:
            return True
        return False

    def __hash__(self):
        return int(self.triggerid)


class Trigger:
    def __init__(self, triggerid, description, severity, lastchange_timestamp):
        self.triggerid = triggerid
        self.description = description
        self.severity = severity
        self.lastchange_timestamp = lastchange_timestamp

        self.severity_desc = None
        self.set_priority()

    def __eq__(self, other):
        if self.triggerid == other.triggerid and self.description == other.description and self.severity == other.severity and self.lastchange_timestamp == other.lastchange_timestamp:
            return True
        return False

    def set_priority(self):
        if self.severity == '0':
            self.severity_desc = "Not Classified"
        elif self.severity == '1':
            self.severity_desc = "Information"
        elif self.severity == '2':
            self.severity_desc = "Warning"
        elif self.severity == '3':
            self.severity_desc = "Average"
        elif self.severity == '4':
            self.severity_desc = "High"
        elif self.severity == '5':
            self.severity_desc = "Critical"
        else:
            self.severity_desc = "UNKNOWN"

    def __str__(self):
        return self.severity + " " + self.description


class Host:
    def __init__(self, hostname, hostid):
        self.hostname = hostname
        self.hostid = hostid

    def __str__(self):
        return "Hostname: " + self.hostname + " " + self.hostid

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.hostname == other.hostname and self.hostid == other.hostid:
            return True
        return False


class Event:
    def __init__(self, triggerid, eventid, hosts):
        self.eventid = eventid
        self.triggerid = triggerid
        self.hosts = hosts

    def __eq__(self, other):
        if self.eventid == other.eventid and self.triggerid == other.triggerid and self.hosts == other.hosts:
            return True
        return False


class HostGroup:
    def __init__(self, groupid, name):
        self.groupid = groupid
        self.name = name


