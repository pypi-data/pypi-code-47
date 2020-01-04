""" Abstract for all things related to simulations. Using OpenAI format to handle. """
from abc import ABC
from crayons import yellow
# from linkkt_hand.data.base import DataSet
from link_jam_handle.data.base_handlers import RunnableSet

class SimulatedData(RunnableSet, ABC):
    """ Simulated data has creation processes """
    def __init__(self, limit=500, **kwargs) -> None:
        super().__init__(limit=limit, **kwargs)
        self._parameters = {}
        self._is_generate = False

    @property
    def parameters(self):
        """ Parameters to we use to generate the data. """
        return self._parameters
    
    @parameters.setter
    def parameters(self, param:dict):
        """ Add items to the parameter dict. """
        keys = param.keys()
        for key in keys:
            self._parameters[key] = param[key]
    
    def _can_generate(self):
        """ Given the conditions we set, determine if we should generate data and sets a bool for the is_generate property to return. """
        print(yellow("Determining", bold=True))
    
    @property
    def is_generate(self) -> bool:
        """ Determine if we can generate"""
        self._can_generate()
        return self._is_generate

    def step(self):
        """ Step through runnable data """
        raise NotImplementedError

    def reset(self):
        """ Run reset command to signify that we're loading information and"""
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

