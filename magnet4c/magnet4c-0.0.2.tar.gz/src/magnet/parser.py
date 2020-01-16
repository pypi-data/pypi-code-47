import json
from magnet.datastructs import jsonPos
import copy

class magnetParser:
    def parseJson(self, jsonStr):
        obj = json.loads(jsonStr)
        corporas = []
        pos = jsonPos()
        pos.add(dict, 'blocks')
        for i in range(len(obj['blocks'])):
            b = obj['blocks'][i]
            np = copy.deepcopy(pos)
            np.add(list, i)
            self.parseElement(b, corporas, np)
        return corporas


    def parseElement(self, eleObj, corporas, pos: jsonPos):
        if type(eleObj) != dict:
            if type(eleObj) == list:
                for i in range(len(eleObj)):
                    l = eleObj[i]
                    np = copy.deepcopy(pos)
                    np.add(list, i)
                    self.parseElement(l, corporas, np)
            else:
                corporas.append((eleObj, pos))
        else:
            if 'c' not in eleObj.keys():
                return
            if 't' in eleObj.keys():
                if eleObj['t'] == 'Image':
                    return
                if eleObj['t'] == 'Link':
                    return
            if type(eleObj['c']) == list:
                pos.add(dict, 'c')
                for i in range(len(eleObj['c'])):
                    c = eleObj['c'][i]
                    np = copy.deepcopy(pos)
                    np.add(list, i)
                    self.parseElement(c, corporas, np)
            else:
                np = copy.deepcopy(pos)
                np.add(dict, 'c')
                self.parseElement(eleObj['c'], corporas, np)
