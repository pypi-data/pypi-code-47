import os
import time


class TailLoader():
    TIME_PATTERN = "%b %d %H:%M:%S"

    def __init__(self, path, duration):
        self.path = path
        self.duration = duration
        self.current = time.localtime()

    def readlines(self):
        """Returns continuation for reading lines which are enough new.
        """
        do_print = False
        with open(self.path) as f:
            for line in f:
                if not do_print:
                    if self.is_new(line):
                        do_print = True
                    else:
                        continue
                yield line.rstrip()

    def is_new(self, line):
        """Returns whether the given line is enough new based on its duration.
        Time format of line is first 16 characters in that.
        """
        logtime = time.strptime(line[0:15], TailLoader.TIME_PATTERN)
        nlogtime = time.mktime((self.current[0], ) + logtime[1:])
        diff = time.mktime(self.current) - nlogtime
        if diff <= self.duration:
            return True
        return False
