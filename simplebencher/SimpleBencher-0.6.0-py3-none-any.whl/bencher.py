from pathlib import Path
import platform
import os
import time

__version__ = "0.6.0"

class Bencher():
    def __init__(self, suite_name):
        self.start_time = 0
        self.stop_time = 0
        self.is_running = False
        self.location = str(Path.home())
        if platform.system() == "Linux":
            self.location += "/.bencher/"
        else:
            self.location += "\\.bencher\\"
        try:
            os.makedirs(self.location)
        except:
            pass
        self.filename = self.location + suite_name + ".bench"
        try:
            open(self.filename, "r")
        except:
            open(self.filename, "w")
    def start(self):
        self.start_time = time.time()
        self.is_running = True
    def stop(self):
        self.stop_time = time.time()
        self.is_running = False
        return self.stop_time - self.start_time
    def get_time(self):
        if self.is_running:
            return time.time() - self.start_time
        else:
            return self.stop_time - self.start_time
    def __str__(self):
        if self.is_running:
            return "[Since " + str(time.time() - self.start_time) + "sec running]"
        else:
            return "[Finished in " + str(time.time() - self.start_time) + "s]"
    def save(self):
        if not self.is_running and self.get_time() != 0:
            savestr = __version__ + "," + str(int(self.start_time)) + "," + str(round(self.get_time(), 4)) + "\n"
            open(self.filename, "a").write(savestr)

    def reset(self):
        self.is_running = False
        self.stop_time = self.start_time
    


if __name__ == "__main__":
    Bencher("testing")