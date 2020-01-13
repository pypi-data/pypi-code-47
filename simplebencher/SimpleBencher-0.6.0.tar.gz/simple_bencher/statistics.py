import platform
import os
import time
from pathlib import Path

class Statter():
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.location = str(Path.home())
        if platform.system() == "Linux":
            self.location += "/.bencher/"
        else:
            self.location += "\\.bencher\\"
        self.filename = self.location + suite_name + ".bench"
        file = open(self.filename, "r")
        self.data = file.read().split("\n")[:-1]
        self.times = [float(i.split(",")[2]) for i in self.data]
        self.sorted = False

    def sum(self):
        return sum([float(i.split(",")[2]) for i in self.data])

    def avg(self):
        self.times = [float(i.split(",")[2]) for i in self.data]
        return sum(self.times) / len(self.times)

    def median(self):
        if not self.sorted:
            self.times = sorted(self.times)
            self.sorted = True
        return self.times[int(len(self.times) / 2)]



    def count(self):
        return len(self.data)
