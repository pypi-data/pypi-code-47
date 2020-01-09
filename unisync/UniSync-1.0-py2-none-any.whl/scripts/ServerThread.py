import threading
from threading import Thread
import ClientDatabase as db
# from importlib.machinery import SourceFileLoader
import select
import Utilities as ut

# utilities = SourceFileLoader("Utilities.py", "../Client/Utilities.py").load_module()
import os


class ServerThread(Thread):  # thread that processes info sent from server
    def __init__(self, conn, conn2):
        threading.Thread.__init__(self)
        self.conn = conn
        self.conn2 = conn2
        self.messageQueue = []

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
            l = f.read(1)

        f.close()
        return content

    def sendUpdate(self, tokkens):
        path = tokkens[1].decode()
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            print("Failed to send update to server!")
            return
        content = self.getFileContent(path)
        message = ("UpdateData!end!" + ut.username + "!end!" + path + "!end!" + str(
            mtime) + "!end!").encode()
        message += content
        ut.HighPriorityQueue.append(message)

    def UpdateFile(self, tokkens):
        path = tokkens[1].decode()
        mtime = tokkens[2].decode()
        try:
            currentmtime = os.path.getmtime(path)
        except OSError as er:
            currentmtime = 0
        content = tokkens[3]
        try:
            if not os.path.exists(os.path.dirname(path)):  # creates directory hierarchy
                os.makedirs(os.path.dirname(path))
            if float(mtime) > float(currentmtime):
                f = open(path, "wb")
                f.write(content)
                f.close()
        except OSError:
            return
        try:
            os.utime(path, (float(mtime), float(mtime)))  # sets mtime to server mtime
        except OSError as err:
            return

    def AddDatabase(self, tokkens):
        count = int(tokkens[1])
        index = 2
        while count:
            db.insertIntoTable(tokkens[index].decode(), 0)
            index = index + 1
            count = count - 1

    def displayList(self, tokkens):
        ut.filelist.clear()
        for files in tokkens[1:]:
            ut.filelist.append(files.decode())

    def processPacket(self):
        for message in self.messageQueue:
            tokkens = message.split(b'!end!')
            messageType = tokkens[0]
            if messageType == b'RequestData':
                self.sendUpdate(tokkens)
            if messageType == b'FileUpdate':
                self.UpdateFile(tokkens)
            if messageType == b'Database':
                self.AddDatabase(tokkens)
            if messageType == b'List':
                self.displayList(tokkens)
                ut.AnswerReceived = True
            if messageType == b'Ack':
                ut.AnswerReceived = True
                ut.LoggedIn = True
            if messageType == b'Reject':
                ut.AnswerReceived = True
                ut.LoggedIn = False
            self.messageQueue.clear()  # refreshes messageQueue

    def receiveMessage(self):  # Method that receives messages
        if self.conn.fileno() == -1:
            self.IsActive = False
            return
        list = [self.conn]
        readable, writable, exceptional = select.select(list, list, list)
        for fds in readable:
            if fds is self.conn:
                message = b''  # reads all message
                data = b''
                while True:
                    unavailable = 0
                    try:
                        data = self.conn.recv(1)
                    except:
                        unavailable = 1
                    if message[-5:] == b'!end!':
                        try:
                            size = int(message[:-5])
                            data += self.conn.recv(size - 1)
                            message = data
                        except:
                            print("Failed to get size of message")
                            return
                        finally:
                            break

                    if data:
                        message += data
                        data = None
                    else:
                        break
                self.messageQueue.append(message)
                if len(self.messageQueue) == 10:
                    break

    def receiveMessageData(self):  # Method that receives messages
        if self.conn2.fileno() == -1:
            self.IsActive = False
            return
        list = [self.conn2]
        readable, writable, exceptional = select.select(list, list, list)
        for fds in readable:
            if fds is self.conn2:
                message = b''  # reads all message
                data = b''
                while True:
                    unavailable = 0
                    try:
                        data = self.conn2.recv(1)
                    except:
                        unavailable = 1
                    if message[-5:] == b'!end!':
                        try:
                            size = int(message[:-5])
                            data += self.conn2.recv(size - 1)
                            message = data
                        except:
                            print("Failed to get size of message")
                            return
                        finally:
                            break

                    if data:
                        message += data
                        data = None
                    else:
                        break
                self.messageQueue.append(message)
                if len(self.messageQueue) == 10:
                    break

    def run(self):
        while True:
            self.receiveMessage()
            self.receiveMessageData()
            self.processPacket()
