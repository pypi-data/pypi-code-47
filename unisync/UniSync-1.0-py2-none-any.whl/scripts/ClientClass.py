import os

class ClientClass:
    def __init__(self, username, password):
        self.user = username
        self.password = password
        self.files = []


    def createFileList(self, DB):
        f = None
        try:
            f = open("Files", "r")
        except OSError:
            print("Failed to open file!")
        l = f.readline()
        while l:
            words = l.split()
            self.files.append(words[0]) #adds file path from DB

        f.close()

    def getUser(self):
        return self.user

    def getPass(self):
        return self.password

    def getSyncFiles(self):
        return self.files
