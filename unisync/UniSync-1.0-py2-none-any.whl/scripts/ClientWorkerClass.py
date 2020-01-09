import threading
import time
import os
import select
import socket
import Utilities as ut
import ClientDatabase as db


# from importlib.machinery import SourceFileLoader
# utilities = SourceFileLoader("Utilities.py", "../Client/Utilities.py").load_module()


class ClientWorkerClass:
    def __init__(self, conn, user):
        self.conn = conn
        self.user = user

    def getFileContent(self, filepath):
        content = b''
        f = None
        try:
            f = open(filepath, "rb")
        except OSError:
            print("Error opening file!")
            return

        l = f.read(1024)  # reads file content
        while l:
            content += l
            l = f.read(1024)

        f.close()
        return content

    def addFiletoServer(self, filepath):

        try:
            fullpath = os.path.abspath(filepath)
            mtime = os.path.getmtime(fullpath)
        except OSError:
            print("File does not exist!")
            return
        folder = "nothing"
        content = self.getFileContent(filepath)
        message = ("AddFile!end!" + ut.username + "!end!" + fullpath + "!end!" + str(
            mtime) + "!end!" + folder + "!end!").encode() + content
        db.insertIntoTable(fullpath, mtime)
        ut.HighPriorityQueue.append(message)

    def removeFile(self, filepath):
        try:
            fullpath = os.path.abspath(filepath)
            message = ("RemoveFile!end!" + ut.username + "!end!" + fullpath + "!end!").encode()
            ut.HighPriorityQueue.append(message)
            print("File ", filepath, " will be removed!")
            db.removeEntry(fullpath)  # removes entry from database
        except OSError as err:
            print("An error has occurred", err)

    def listSyncFiles(self):
        message = "List!end!" + ut.username + "!end!"
        ut.HighPriorityQueue.append(message.encode())

    def writeMessage(self, message):
        if self.conn.fileno() == -1:
            return
        size = (str(len(message)) + "!end!").encode()
        message = size + message.encode()
        list = [self.conn]
        readable, writable, exceptional = select.select(list, list, list)
        for fds in writable:
            if fds is self.conn:
                try:
                    self.conn.send(message)
                except socket.error as error:
                    print("Error ", error)
                    self.conn.close()

    def Login(self):
        message = "Login!end!" + ut.username + "!end!" + ut.password + "!end!"
        self.writeMessage(message)
