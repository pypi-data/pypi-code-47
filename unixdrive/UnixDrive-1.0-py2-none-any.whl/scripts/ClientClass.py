import os
import ntpath
import sys
import Utilities as u


class ClientClass:

    def __init__(self, mysock):
        self.mysock = mysock

    def RegisterClient(self, username, password):
        message = "Register#"
        message += username + "#" + password + "#"
        self.mysock.send(message.encode())

    def send_File(self, filename):
        if not os.path.exists(filename):
            print("File does not exist!")
            return
        size = str(os.path.getsize(filename))
        message = "Content#"
        message += (filename + "#") + u.clientusername + "#" + u.clientpassword + "#" + size + "#"
        f = open(filename, 'rb')

        l = f.read(2048)
        while l:
            message += l.decode()
            l = f.read(2048)
        f.close()
        self.mysock.send(message.encode())
        print(message)
        print("Send to server file %s" % filename)

    def LogInClient(self, username, password):
        message = "LogIn#"
        message += username + "#" + password + "#"
        self.mysock.send(message.encode())

    def downloadFile(self, filename, usr, passw):
        msg = "Download#" + usr + "#" + passw + "#" + filename + "#"
        self.mysock.send(msg.encode())

    def list_uploads(self, usr, password):
        message = "List#"
        message += usr + "#" + password + "#"
        self.mysock.send(message.encode())

    def CountFiles(self, start_path):
        count = 0
        try:
            path, dirs, files = next(os.walk(start_path))
            count = len(files)
        except OSError:
            print("Failed to open directory!")

        return count

    def uploadFolder(self, folderPath):
        fullpath = os.path.abspath(folderPath)
        message = "Folder#" + u.clientusername + "#"
        nrfiles = self.CountFiles(fullpath)
        dirsize = self.get_size(fullpath)
        if nrfiles == 0:
            print("Wrong path!")
            return
        message += fullpath + "#" + str(nrfiles) + "#"
        message += str(dirsize) + "#"
        try:
            for dirpath, dirnames, filenames in os.walk(folderPath):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    message = message + f + "#"
                    file = open(fp, 'rb')
                    l = file.read(2048)
                    while l:
                        message += l.decode()
                        l = file.read(2048)
                    file.close()
                    message += "#"
        except OSError:
            print("Failed to open directory!")

        self.mysock.send(message.encode())

    def downloadFolder(self, folder):
        message = "FolderDownload#"
        message = message + folder + "#" + u.clientusername + "#"
        self.mysock.send(message.encode())

    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def removeFile(self, filepath):  # removes file from drive
        filename = filepath
        message = "RemoveFile#" + u.clientusername + "#" + filename + "#"
        self.mysock.send(message.encode())

    def removeDir(self, dirName):
        message = "RemoveDir#" + u.clientusername + "#" + dirName + "#"
        self.mysock.send(message.encode())

    def get_size(self, start_path):  # gets size of directory
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(start_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
        except OSError:
            print("Failed to open directory!")

        return total_size