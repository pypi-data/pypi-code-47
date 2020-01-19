class LoggerSetter:
    def setLogger(self, logger):
        if logger is None:
            raise NotImplementedError
        self.logger = logger
