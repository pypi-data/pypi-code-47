""" Get Aggregate Information """
from abc import ABC
from crayons import blue
from typing import Any, Dict
from link_jam_handle.data.base_handlers import RunnableSet
# Come back to work on this. It'll take a little while to finish this. It's classified as overbuilt unti lnecessary to do better. 

class BacktestDataset(RunnableSet, ABC):
    """ Backtest A Dataset"""
    def __init__(self, limit=500, seconds=0, minutes=0, hours=1, days=0, months=0, years=0) -> None:
        super().__init__(limit=limit, seconds=seconds, minutes=minutes, hours=hours, days=days, months=months, years=years)
        self._name = ""
        self._metadata = {}


    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name:str):
        self.name = name

    @property
    def metadata(self) -> dict:
        return self._metadata

    @metadata.setter
    def metadata(self, meta):
        self._metadata = meta

    def check(self):
        """ Check to see if a certain kind of dataset exists. """
        pass

    def load(self):
        """ Loads a dataset from the database and implants it into a backtest-able location if it's not already there. """
        print(blue(f"Load the dataset with the parameters ... {self._metadata}")) # would use the metadata to load from main dataset. 


    def latest(self) -> Dict[str, Any]:
        return {}

    def reset(self):
        """ Pull the data we need to pull """
        self.load()