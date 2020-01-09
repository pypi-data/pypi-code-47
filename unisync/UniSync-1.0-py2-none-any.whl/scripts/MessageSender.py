import threading
import socket
import select
import Utilities as ut
from collections import OrderedDict

class MessageSender(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

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

    def RemoveDuplicates(self, mylist):
        res = list(OrderedDict.fromkeys(mylist))

        return res

    def run(self):
        while True:
            for message in ut.messageQueue:
                self.writeMessage(message)
                ut.messageQueue = self.RemoveDuplicates(ut.messageQueue)
                try:
                    ut.messageQueue.remove(message)
                except ValueError:
                    pass  # do nothing!
