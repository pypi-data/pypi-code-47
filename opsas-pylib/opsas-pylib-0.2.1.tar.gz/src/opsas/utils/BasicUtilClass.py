from .mixins.LoggerSetter import LoggerSetter


class BaseUtilClass(LoggerSetter):
    def __init__(self, Logger=None):
        """
        All function class should mixin or inherit from thisyou
        :param Logger:
        """
        self.setLogger(Logger)
