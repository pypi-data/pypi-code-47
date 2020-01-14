import re
import json


class MailLogEater:
    def __init__(self):
        self.counter = {
            "bounced": 0,
            "deferred": 0,
            "sent": 0,
            "expired": 0,
        }

    def __str__(self):
        return self.format("json")

    def eat(self, line):
        for s in self.counter.keys():
            matcher = "status=" + s
            if matcher in line:
                self.counter[s] += 1
                return True
        return False

    def format(self, fmt):
        if fmt == "json":
            return json.dumps(self.counter)
        else:
            raise "Unknown format type: %s" % fmt
