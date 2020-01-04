from uuid import uuid4
from jamboree import DBHandler, Jamboree

from abc import ABCMeta
from pebble.pool import ThreadPool
class DataHandler(DBHandler, metaclass=ABCMeta):
    def __init__(self, _limit=500) -> None:
        super().__init__()
        self.limit = _limit
        self.pool = ThreadPool()
    
    
    def get_latest(self, symbol:str, alt={}):
        raise NotImplementedError
    

    def _save_step(self):
        alt = {"details": "step"}
        data = {"count": "count"}
        self.save(data, alt=alt)


    def _step_count(self):
        alt = {"details": "step"}
        count = self.count(alt=alt)
        return count


    def _test_load(self, limit=10000):
        """ 
            We're going to test the swap idea here
            NOTE: Test Load 
        """
        

    def step(self, _limit=1, first_limit=500, alt={}):
        """ 
            STEP THROUGH DATA
            ---
            Get all the data related to what we'd deem as a step
            Parameters:
                - _limit: 
                    - The number of steps we're swapping over.
                - alt: 
                    - The specifics to the query
        """
        
        raise NotImplementedError


    def step_data(self):
        """ Get the most recent stepped through data"""
        raise NotImplementedError

    

if __name__ == "__main__":
    # We'll this swap works pretty damn well.
    jam = Jamboree()
    data_handle = DataHandler()
    data_handle.entity = "test_commands"
    data_handle.required = {"test": str, "episode": str}
    data_handle.event = jam
    data_handle['test'] = "test"
    data_handle['episode'] = uuid4().hex
    multiplier = 60