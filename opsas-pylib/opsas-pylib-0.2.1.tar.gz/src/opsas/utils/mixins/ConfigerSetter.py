class ConfigerSetter:
    def setConfigger(self, configger):
        if configger is None:
            raise NotImplementedError
        self.configer = configger
