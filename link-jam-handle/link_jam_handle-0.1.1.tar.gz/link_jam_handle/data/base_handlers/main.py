import maya
from abc import ABC
from jamboree import DBHandler
from pebble.pool import ThreadPool

class DataSet(DBHandler, ABC):
    """ Abstracted way of handling variations of datasets. """
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self._name = ""
        self._metadata = {}
        self.pool = ThreadPool()
        self._start_time_maya = maya.now()
        self._current_time = None

        self._seconds = kwargs.get("seconds", 0)
        self._minutes = kwargs.get("minutes", 0)
        self._hours = kwargs.get("hours", 1)
        self._days = kwargs.get("days", 0)
        self._months = kwargs.get("months", 0)
        self._years = kwargs.get("years", 0)
        self._first_limit = kwargs.get("first_limit", 500)

    @property
    def current_time(self):
        """ Get the timestamp of the price indicator. """
        raise NotImplementedError
        

    def get_latest(self, symbol:str, alt={}):
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name:str):
        self.name = name

    def latest(self, alt:dict={}):
        raise NotImplementedError
