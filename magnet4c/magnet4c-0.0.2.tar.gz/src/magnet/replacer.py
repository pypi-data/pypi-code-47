import json


class magnetReplacer:
    def replaceJson(self, jsonStr, corporas, parallelCorporas):
        jsonObj = json.loads(jsonStr)
        for i in range(len(corporas)):
            self.replaceElement(
                corporas[i][1].Pos, parallelCorporas[i], jsonObj)
        return json.dumps(jsonObj)

    def replaceElement(self, index: list, replacement, obj):
        if len(index) == 1:
            if type(replacement) == type(obj[index[0][1]]):
                obj[index[0][1]] = replacement
        else:
            self.replaceElement(index[1:], replacement, obj[index[0][1]])
