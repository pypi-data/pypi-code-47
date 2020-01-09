from threading import Thread
import ntpath
import os
import Utilities as u


class ServerThread(Thread):

    def __init__(self, mysock):
        Thread.__init__(self)
        self.mysock = mysock

    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def addFolder(self, tokkens):

        try:
            os.mkdir(tokkens[1])
        except OSError:
            print("Creation of directory  failed!")
        nrFiles = int(tokkens[2])
        index = 3
        while nrFiles != 0:
            file = os.path.join(tokkens[1], tokkens[index])
            f = open(file, 'wb')  # writes to file
            f.write(tokkens[index + 2].encode())
            f.close()
            index = index + 2
            nrFiles -= 1

    def processPacket(self, sock):
        Unavailable = 0
        message = ''  # reads all message
        data = ""
        while True:
            try:
                data = self.mysock.recv(2048).decode()
            except:
                Unavailable = 1

            if data:
                message += data
                data = None
            else:
                break
        tokkens = message.split('#')

        if tokkens[0] == "Message":
            if tokkens[1] == "You must register first!":
                u.ReceivedAnswer = True
            print(tokkens[1])  # prints message to terminal
        if tokkens[0] == "AccountAck":
            u.ReceivedAnswer = True
            u.LoggedIn = True

        if tokkens[0] == "Content":
            if os.path.exists(tokkens[1]):
                print("File already exits!")
                return
            if not os.path.exists(os.path.dirname(tokkens[1])):  # creates directory for file
                try:
                    os.makedirs(os.path.dirname(tokkens[1]))
                except OSError as exc:  # Guard against race condition
                    print("Failed to create directory")
            f = open(tokkens[1], 'wb')
            f.write(tokkens[2].encode())
        if tokkens[0] == "List":
            u.filelist.clear()
            for f in tokkens:
                if f != "List":
                    u.filelist.append(f)
            u.ReceivedAnswer = True
        if tokkens[0] == "FolderDownload":
            self.addFolder(tokkens)

    def run(self):
        while True:
            self.processPacket(self.mysock)
