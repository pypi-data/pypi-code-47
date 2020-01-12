

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


class Trigger:
    def __init__(self, triggerid, description, severity, lastchange_timestamp):
        self.triggerid = triggerid
        self.description = description
        self.severity = severity
        self.lastchange_timestamp = lastchange_timestamp

        self.severity_desc = None
        self.set_priority()

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


class Event:
    def __init__(self, triggerid, eventid, hosts):
        self.eventid = eventid
        self.triggerid = triggerid
        self.hosts = hosts


