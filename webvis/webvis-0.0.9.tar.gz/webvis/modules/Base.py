from webvis import VisVars
import json

class BaseModule(VisVars):
    def serial(self):
        return json.dumps(self.__dict__)



