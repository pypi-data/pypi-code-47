import pypandoc
from magnet.snowflake import magnetSnowflake
from magnet.parser import magnetParser
from magnet.replacer import magnetReplacer


def hello():
    return "Hello Magnet"


class magnetEngine:
    def __init__(self):
        self.tempFolder = 'temps'
        self._Snowflake = magnetSnowflake(1, 2)
        self._Parser = magnetParser()

    def shutdown(self):
        pass

    def importFile(self, filePath):
        taskID = self._Snowflake.next()
        taskPath = self.tempFolder + '/' + str(taskID) + '.json'
        pypandoc.convert(
            filePath,
            'json',
            format='docx',
            outputfile=taskPath,
            extra_args=[
                '--extract-media=temps/'+str(taskID)
            ])
        return taskID

    def getCorporas(self, taskID):
        taskPath = self.tempFolder + '/' + str(taskID) + '.json'
        with open(taskPath, encoding='utf-8') as OJson:
            return self._Parser.parseJson(OJson.read())

    def setParallelCorporas(self, taskID, ParallelCorporas):
        corporas = self.getCorporas(taskID)
        if type(ParallelCorporas) != list or \
                len(ParallelCorporas) != len(corporas):
            raise Exception()
        taskPath = self.tempFolder + '/' + str(taskID) + '.json'
        jsonStr = ''
        with open(taskPath, encoding='utf-8') as OJson:
            jsonStr = magnetReplacer().replaceJson(OJson.read(), corporas, ParallelCorporas)
        with open(taskPath, 'w', encoding='utf-8') as OJson:
            OJson.write(jsonStr)

    def exportFile(self, filePath, taskID):
        taskPath = self.tempFolder + '/' + str(taskID) + '.json'
        pypandoc.convert(
            taskPath,
            'docx',
            format='json',
            outputfile=filePath)


def createEngine():
    return magnetEngine()
