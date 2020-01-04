from abc import ABC
from link_jam_handle.data.base_handlers import DataSet
class PriceSet(DataSet, ABC):
    """ A price dataset abstract. Use with all price related sets """
    def __init__(self, **kwargs) -> None:
        print(kwargs)
        super().__init__(**kwargs)
    

    def latest_price(self, symbol:str):
        """ Get the latest price """
        return 0.0
    
    def step(self):
        return {}