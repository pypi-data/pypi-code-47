import maya
import copy
from maya import MayaDT
from abc import ABC
from link_jam_handle.data.base_handlers import DataSet

class RunnableSet(DataSet, ABC):
    """ Create a setup to run through code as if it were real (backtest/simulations). Might migrate that code to the portfolio. """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._parameters = {}
        self._start_time_maya = maya.now()
        self._current_time = None
    

    @property
    def current_time(self):
        """ Get the timestamp of the price indicator. """
        step = self.current_step
        shift = 1
        
        return (self._start_time_maya.add(
            seconds=(self._seconds * (step+self._first_limit-shift)), 
            minutes=(self._minutes * (step+self._first_limit-shift)), 
            hours=(self._hours * (step+self._first_limit-shift)), 
            days=(self._days * (step+self._first_limit-shift)), 
            months=(self._months * (step+self._first_limit-shift)), 
            years=(self._years * (step+self._first_limit-shift))
        )._epoch)
        """ 
            return (self._start_time_maya.add(
                seconds=(self._seconds * (step+self._first_limit-shift)), 
                minutes=(self._minutes * (step+self._first_limit-shift)), 
                hours=(self._hours * (step+self._first_limit-shift)), 
                days=(self._days * (step+self._first_limit-shift)), 
                months=(self._months * (step+self._first_limit-shift)), 
                years=(self._years * (step+self._first_limit-shift))
            )._epoch)
        """

    @property
    def start_time(self):
        return self._start_time_maya._epoch
    

    @property
    def current_step(self):
        return self._step_count()

    @property
    def parameters(self):
        """ Parameters to we use to generate the data. """
        return self._parameters


    def update_step(self):
        """ Update the step of the program """
        self._save_step()


    @start_time.setter
    def start_time(self, _t:MayaDT):
        self.start_time = _t
    



    def _save_step(self):
        alt = {"details": "step"}
        data = {"count": "count"}
        self.save(data, alt=alt)


    def _step_count(self):
        alt = {"details": "step"}
        count = self.count(alt=alt)
        return count


    @parameters.setter
    def parameters(self, param:dict):
        """ Add items to the parameter dict. """
        keys = param.keys()
        for key in keys:
            self._parameters[key] = param[key]
    
    

    def step(self):
        """ Step through simulated data """
        raise NotImplementedError

    def reset(self):
        """ Run reset command to signify that we're loading information and"""
        raise NotImplementedError

    def close(self):
        raise NotImplementedError