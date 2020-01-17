import os
from envyaml import EnvYAML
class Config():
    def __init__(self):
        envConfig = os.getenv('APP_SETTINGS', 'default')
        mode = "MODE : %s" % str(envConfig)
        print(mode)
        path ="config/%s.yaml"%(str(envConfig))
        self.fileConfig = EnvYAML(path)

    def yamlToDict(self):
        return self.fileConfig
        
    def getValueToYaml(self,key,default):
        return self.fileConfig.get(key,default)