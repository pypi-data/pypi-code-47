import json

import os
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class DataLoader(object):
    #def __init__(self, market):
    def __init__(self):
        pass

    def setStock(self, path):
        print('DataLoader : ')
        self.path = '{}/{}'.format(dir_path,path)

    def loadAll(self):
        with open(self.path) as json_file:
            self.data = json.load(json_file)

    def getSequence(self, position, length):
        return self.data[position:position+length]

    def getLength(self):
        return len(self.data) 
