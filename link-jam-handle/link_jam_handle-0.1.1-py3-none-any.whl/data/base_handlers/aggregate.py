""" Get Aggregate Information """
from abc import ABC
from typing import Any, Dict
from link_jam_handle.data.base_handlers import DataSet, PriceSet

# Come back to work on this. It'll take a little while to finish this. It's classified as overbuilt.

class AggregateDataset(ABC):
    def __init__(self) -> None:
        self._datasets = set()

    def raise_if_no_price(self):
        if not self._is_already_price():
            raise AttributeError("You didn't add any price information to read from")

    def _is_already_price(self) -> bool:
        """ Checks to see if there's already price information. We can only allow for one piece of price information. """
        if len(self._datasets) != 0:
            for _set in self._datasets:
                if isinstance(_set, PriceSet):
                    return True 
        return False

    @property
    def datasets(self):
        return self._datasets

    @datasets.setter
    def datasets(self, dataset:DataSet):
        """ Add a dataset to pull. """
        if not self._is_already_price():
            self._datasets.add(dataset)

    def latest(self) -> Dict[str, Any]:
        # Iterates through all datasets and calls their latest parameter
        return self.preprocess({})
    

    def latest_price(self, symbol:str):
        self.raise_if_no_price()
        for _set in self._datasets:
            if isinstance(_set, PriceSet):
                return _set.latest_price(symbol)
        return 0.0

    def _preprocess_rules(self):
        """ 
            A set of preprocessing rules that need to be called for any dataset. 
            Usually to match the records so they can be processed. 
        """
        raise NotImplementedError

    def preprocess(self, data:dict) -> Dict[str, Any]:
        """ Get all of the queried data and preprocess it for a single frame. """
        return {}
    

    def reset(self):
        """ Run a reset function """
        # Run through all datasets and reset them. LIve datasets will skip extra processing
        if len(self._datasets) == 0:
            raise IndexError("Datasets can't be empty")