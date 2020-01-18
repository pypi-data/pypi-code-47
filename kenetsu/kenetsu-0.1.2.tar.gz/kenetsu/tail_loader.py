import os
import time

from file_read_backwards import FileReadBackwards


class TailLoader():
    TIME_PATTERN = "%b %d %H:%M:%S"

    def __init__(self, path, duration):
        self.path = path
        self.duration = duration
        self.current = time.localtime()
        self.current_epoch = time.mktime(self.current)

    def readlines(self):
        """Returns continuation for reading lines which are enough new.
        """
        do_print = True
        with FileReadBackwards(self.path, encoding="utf-8") as frb:
            for line in frb:
                if not self.is_new(line):
                    return
                yield line.rstrip()

    def is_new(self, line):
        """Returns whether the given line is enough new based on its duration.
        Time format of line is first 16 characters in that.
        """
        logtime = time.strptime(line[0:15], TailLoader.TIME_PATTERN)
        nlogtime = time.mktime((self.current[0], ) + logtime[1:])
        diff = self.current_epoch - nlogtime
        if diff <= self.duration:
            return True
        return False
