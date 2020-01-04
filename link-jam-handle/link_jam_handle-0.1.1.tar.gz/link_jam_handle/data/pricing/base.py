""" 
# BasePriceHandler

BasePriceHandler is an extension of DataHandler
"""


import copy
from typing import List, Dict, Any

# TODO: Rethink design here and come back to this.

from link_jam_handle.data import PriceSet


class PriceBaseSet(PriceSet):
    def __init__(self, limit=500, **kwargs):
        super().__init__(limit=limit, **kwargs)
        self.entity = "pricing"
        self.required = {
            "episode": str,
            "exchange": str,
            "live": bool
        }
        self.asset_bars = {}
    
    
    @property
    def assets(self) -> list:
        """ Get all of the assets that we're watching for the exchange """
        return self.latest_asset().get("assets", [])
    
    
    def latest_price(self, symbol):
        alt = {"asset": symbol}
        price_bar = self.last(alt=alt)
        return price_bar
    
    
    def latest_asset(self):
        alt = {"detail": "assets"}
        asset = self.last(alt=alt)
        return asset
    
    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Counting Functions -------------------------------
        ----------------------------------------------------------------------------------
    """
    
    
    def asset_count(self) -> int:
        """ Get the count of the asset adds we have. Not the number of assets. """
        alt = {"detail": "assets"}
        count = self.count(alt=alt)
        return count

    def price_count(self) -> int:
        count = self.count()
        return count
    
    
    """ 
        --------------------------------------------------------------------------------
        ------------------------------- Saving Functions -------------------------------
        --------------------------------------------------------------------------------
    """



    def add_assets(self, assets:List[str]):
        """ Add a list of assets to monitor. Used for tracking multiple assets inside of a portfolio. """
        if len(assets) == 0:
            return
        asset_list = self.assets
        for asset in assets:
            if asset not in asset_list:
                asset_list.append(asset)
        self.save_monitored_assets(asset_list)

    def add_asset(self, asset_name:str):
        """ Add an asset that will be monitored in an exchange"""
        if asset_name == "":
            return

        asset_list = self.assets
        asset_list.append(asset_name)
        asset_list = list(set(asset_list))
        self.save_monitored_assets(asset_list)
        
    
    def save_monitored_assets(self, assets:list):
        """ Save monitored assets """
        alt = {"detail": "assets"}
        monitored = {
            "assets": assets
        }
        self.save(monitored, alt=alt)
    
    
    
    def save_bar_multi_bar(self, name:str, bars:List[Dict]):
        """ Save multiple points of data """
        alt = {"asset": name}
        if len(bars) == 0:
            return
        
        query = copy.copy(self._query)
        episode = query.get("episode")
        exchange = query.get("exchange")
        print(f"Saving bars for {name}-{episode}-{exchange}")
        self.add_asset(name)
        self.save_many(bars, alt=alt) # This will yield a flag, because why not?

    def save_bar(self, name, bar:Dict[str, Any]) -> None:
        alt = {"asset": name}
        if len(bar.keys()) == 0:
            return
        
        self.add_asset(name)
        self.save(bar, alt=alt)
    
    def _reset_assets(self):
        """ Set the first asset """
        count = self.asset_count()
        if count == 0:
            # Save that we have no new assets
            self.save_monitored_assets([])
    
    
    
    """ ---------------------------------------------------------------------------
        ---------------------------- RL-Like Functions ---------------------------- 
        ---------------------------------------------------------------------------
    """

    def step(self):
        """
            # Step through the data set
            ---
            Step through the price dataset. The rules change based on the scenario.
        """
        
    
    def get_step(self):
        """
            # GET STEP
            ---
            Get all of the data for the latest step without pushing it forward.

            Only works when live is set to false. Should only use it when live is set to false. 
        """

    def reset(self):
        """ Resets the way of interacting with the price. """
        self._reset_assets()