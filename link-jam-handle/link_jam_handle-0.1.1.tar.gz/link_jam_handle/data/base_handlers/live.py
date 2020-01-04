import maya
import copy
from maya import MayaDT
from abc import ABC
from loguru import logger
from link_jam_handle.data.base_handlers import DataSet

class LiveSet(DataSet, ABC):
    """ Load and save live data. Should have a set of  """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._parameters = {}
        self['opt_type'] = "live"
    

    @property
    def current_time(self):
        """ Get the timestamp of the price indicator. """
        return maya.now()._epoch

    
    

    def step(self):
        """ Step through simulated data """
        logger.error("Live data doesn't use the `step` paradigm")

    def reset(self):
        """ Run reset command to signify that we're loading information and"""
        logger.error("Live data doesn't use the `reset` paradigm")

    def close(self):
        logger.error("Live data doesn't use the `error` paradigm")