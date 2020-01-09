import os
import select
import sys
import threading
import time
from collections import OrderedDict
from threading import Thread
import threading
import ClientDatabase as db
# from importlib.machinery import SourceFileLoader
# utilities = SourceFileLoader("Utilities.py", "../Client/Utilities.py").load_module()
import Utilities as ut
import socket


class DataExchangeThread(Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.messageQueue = []

    def RemoveDuplicates(self, mylist):
        res = list(OrderedDict.fromkeys(mylist))
        return res

    def writeMessage(self, message):
        size = (str(len(message)) + "!end!").encode()
        message = size + message
        if self.conn.fileno() == -1:
            return
        list = [self.conn]
        readable, writable, exceptional = select.select(list, list, list)
        for fds in writable:
            if fds is self.conn:
                try:
                    self.conn.send(message)
                except socket.error as error:
                    print("Error ", error)
                    self.conn.close()

    def sendData(self):
        records = db.readSqliteTable("Files")
        for row in records:
            try:
                mtime = os.path.getmtime(row[1])
            except OSError:
                # File is out of date on client device
                mtime = 0
            message = ("FileInfo!end!" + ut.username + "!end!" + row[1] + "!end!" + str(
                mtime) + "!end!").encode()
            self.messageQueue.append(message)
        self.RemoveDuplicates(self.messageQueue)

    def RequestFiles(self):
        message = ("RequestFiles!end!" + ut.username + "!end!").encode()
        self.messageQueue.append(message)
        self.RemoveDuplicates(self.messageQueue)

    def run(self):
        while True:
            for message in self.messageQueue:
                self.writeMessage(message)
                try:
                    self.messageQueue.remove(message)
                except ValueError:
                    pass  # do nothing!
            self.RequestFiles()
            self.sendData()
            time.sleep(2)