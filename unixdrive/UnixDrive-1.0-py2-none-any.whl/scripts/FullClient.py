import socket
from ServerThread import ServerThread
from ClientClass import *
import Utilities as ut

port = 10001


# Multithreaded Python client : TCP Client Socket Program Stub


class FullClient:
    def __init__(self):
        self.host = ""
        self.mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = None
        if len(sys.argv) == 2:
            self.host = sys.argv[1]
        try:
            self.mysock.connect((self.host, port))
            ut.ConnectionEstabilished = True
        except ConnectionError:
            print("Failed to connect!")
            ut.ConnectionEstabilished = False
        if ut.ConnectionEstabilished is True:
            self.mysock.setblocking(0)
            self.newThread = ServerThread(self.mysock)  # thread for processing messages from server
            self.newThread.start()
            self.client = ClientClass(self.mysock)  # client instance

    def GetClientInstance(self):
        return self.client
