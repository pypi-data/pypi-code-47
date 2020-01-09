import socket
import sys
import ServerThread as s
# from importlib.machinery import SourceFileLoader
# utilities = SourceFileLoader("Utilities.py", "../Client/Utilities.py").load_module()
# module where client username and password are stored
import ClientDatabase as db
import DataExchangeThread as data
import ClientWorkerClass as cw
import ClientClass as client
import MessageSender as sender
from threading import Lock
import HighPriorityThread
import Utilities as ut

port = 10002


class SyncClient:

    def createSocket(self):  # method that creates a new socket
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        if len(sys.argv) == 2:
            host = sys.argv[1]  # server ip
        try:
            mysock.connect((host, port))
        except ConnectionError:
            return None
        mysock.setblocking(False)
        return mysock

    def __init__(self):
        self.conn = self.createSocket()  # connection for sending normal messages
        self.connData = self.createSocket()  # connection for exchanging files data
        self.clientworker = None
        if self.conn is not None and self.connData is not None:
            ut.ConnectionEstabilished = True
        else:
            ut.ConnectionEstabilished = False
            return
        user = client.ClientClass(ut.username, ut.password)  # class that stores client info
        self.clientworker = cw.ClientWorkerClass(self.conn, user)  # main client class
        db.make_database()  # creates database
        self.thread = s.ServerThread(self.conn, self.connData)  # Thread that processes messages from server
        self.thread.start()
        self.dataThread = data.DataExchangeThread(self.connData)  # thread that gets file info
        self.highPriority = HighPriorityThread.HighPriorityThread(self.conn)  # thread that send important messages
        # to server

    def GetClientInstance(self):
        return self.clientworker

    def StartSyncThreads(self):
        if ut.LoggedIn is True:
            self.dataThread.start()
            self.highPriority.start()
