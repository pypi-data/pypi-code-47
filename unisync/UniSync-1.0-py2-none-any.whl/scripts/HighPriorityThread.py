import threading
import socket
import select
import Utilities as ut
import ClientDatabase as database


class HighPriorityThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def writeMessage(self, message):
        if self.conn.fileno() == -1:
            return
        size = (str(len(message)) + "!end!").encode()
        message = size + message
        list = [self.conn]
        readable, writable, exceptional = select.select(list, list, list)
        for fds in writable:
            if fds is self.conn:
                try:
                    self.conn.send(message)
                except socket.error as error:
                    print("Error ", error)
                    self.conn.close()
        database.removeRecords()

    def run(self):
        while True:
            for message in ut.HighPriorityQueue:
                self.writeMessage(message)
                try:
                    ut.HighPriorityQueue.remove(message)
                except ValueError:
                    pass
