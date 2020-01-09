import os

class File:   #class for storing file info
    def __init__(self, path):
        self.path = path
        self.time = None

    def updateTime(self):
        self.time = os.path.getmtime(self.path)

    def getTime(self):
        return self.time

    def getPath(self):
        return self.path

    def setTime(self):
        self.time = os.path.getmtime(self.path)