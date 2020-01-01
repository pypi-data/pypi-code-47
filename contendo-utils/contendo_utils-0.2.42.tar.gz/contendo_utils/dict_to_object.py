#
# objectview class enables to access a dict as a class
class DictToObject(object):
    def __init__(self, inDict: dict) -> None:
        self.__dict__ = inDict

