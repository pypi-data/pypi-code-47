""" 
# BasePriceHandler

BasePriceHandler is an extension of DataHandler
"""


import uuid
import dask
import random
import numpy as np
from jamboree import Jamboree
from loguru import logger
from crayons import (magenta, yellow, red, blue)

from link_jam_handle.utils import generate_super_price
from link_jam_handle.data import SimulatedData
from link_jam_handle.data.pricing import PriceBaseSet

class SimulatedPriceHandler(SimulatedData, PriceBaseSet):
    def __init__(self, limit=500, **kwargs):
        super().__init__(limit=limit, **kwargs)
        self.entity = "pricing"
        self['opt_type'] = "simulated"
        self.asset_bars = {}

    

    def latest_price(self, symbol:str):
        alt = {"asset": symbol}
        all_prices = self.last(alt=alt)
        return all_prices.get("close", 0.0)
    
    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Counting Functions -------------------------------
        ----------------------------------------------------------------------------------
    """


    def _generate_price_bars(self, name, _type, _len, base_price):
        price = generate_super_price(base_price, _type, _len)
        ps = len(price)
        vol_multiplier = random.uniform(2, 20)
        open_multiplier = np.absolute(np.random.normal(1, 0.05, size=ps))
        high_multiplier = np.absolute(np.random.normal(1.12, 0.05, size=ps))
        low_multiplier =  np.absolute(np.random.normal(0.92, 0.05, size=ps))
        noise = np.absolute(
            np.random.normal(1, 0.2, size=ps)
        )


        volume = (noise * price) * vol_multiplier
        _open = price * open_multiplier
        high = high_multiplier * price
        _low = low_multiplier * price

        bars = []
        current_time = self._start_time_maya
        
        time_list = list(range(ps))
        time_list_sorted = sorted(time_list, reverse=True)
        for _ in time_list_sorted:
            
            bar = {
                "open": float(_open[_]),
                "close": float(price[_]),
                "high": float(high[_]),
                "volume": float(volume[_]),
                "low": float(_low[_]),
                "time": float((current_time.add(
                                seconds=(self._seconds * _), minutes=(self._minutes * _), 
                                hours=(self._hours * _), days=(self._days * _), 
                                months=(self._months * _), years=(self._years * _))._epoch))
            }
            bars.append(bar)
        # # Create a bunch of bars here
        self.asset_bars[name] = bars

    


    def generate(self, starting_min=50, starting_max=2000, is_varied=True, excluded_assets=[], _len=4000):
        """ Generate price bars for assets """
        assets = self.assets
        if len(assets) == 0:
            logger.error(red("No assets found"))
            return
        
        for excluded in excluded_assets:
            assets.remove(excluded)
        
        # Generate bars
        mid_point = ((starting_min + starting_max)/2)
        std = (mid_point/4)

        
        dask_tasks = []
        for asset in assets:
            base_price = random.normalvariate(mid_point, std)
            # price_quote = f"Create prices for {asset}, {base_price}"
            _type = random.choice(["GBM", "HESTON"])
            dask_task = dask.delayed(self._generate_price_bars)(asset, _type, _len, base_price)
            dask_tasks.append(dask_task) 
        dask.compute(*dask_tasks)

        for asset in assets:
            logger.info("Saving Bar")
            self.save_bar_multi_bar(asset, self.asset_bars[asset])
        
    

    

    def _reset_generate_price(self):
        count = self.price_count()
        logger.info("Change the conditions here. The conditions should allow for dynamically adding assets")
        if count == 0:
            logger.info(magenta("Generating price points", bold=True))
            starting_min = self.data.get("starting_min", 50)
            starting_max = self.data.get("starting_max", 2000)
            is_varied = self.data.get("is_varied", True)
            excluded_assets = self.data.get("excluded_assets", [])
            obs_num = self.data.get("obs_num", 4000) # number of observations
            self.generate(starting_min=starting_min, starting_max=starting_max, is_varied=is_varied, excluded_assets=excluded_assets, _len=obs_num)
            self.save({"data": "blank"})


    @property
    def is_next_observation(self) -> bool:
        """ Check to see if there's a next observation for all coins. """
        assets = self.assets
        if len(assets) == 0: False
        confirmations = list(map(self._is_next_observation_single, assets))
        # logger.info(confirmations)
        return (not all(confirmations))


    def _is_next_observation_single(self, name:str):
        alt = {"asset": name}
        count = self.count(alt=alt)
        if count == 0: return False
        return True
    # """ ---------------------------------------------------------------------------
    #     ---------------------------- RL-Like Functions ---------------------------- 
    #     ---------------------------------------------------------------------------
    # """

    def step(self, _limit=1, alt={}):
        """
            # Step through the data set

            Step through the price dataset. The rules change based on the scenario.
        """
        current_step = self._step_count()
        if current_step == 0:
            # Use the first_limit here
            logger.info(yellow(f"Set the limit to the first limit: {self._first_limit}", bold=True))
            _limit = self._first_limit
        
        assets = self.assets
        
        swapped_assets = {
            "step_num": current_step,
            "assets": {},
            "done": self.is_next_observation
        }
        # Move the latest n assets over to the seen list

        for asset in assets:
            alt = {"asset": asset}
            self.swap_many(limit=_limit, alt=alt)
            swapped = self.query_many_swap(limit=self._first_limit, alt=alt)[::-1]
            swapped_assets["assets"][asset] = swapped
        
        swapped_assets["done"] = self.is_next_observation
        self.update_step()
        return swapped_assets
    
    def get_step(self):
        """
            # GET STEP
            ---
            Get all of the data for the latest step without pushing it forward.

            Only works when live is set to false. Should only use it when live is set to false. 
        """


    def reset(self):
        """ Resets the way of interacting with the price. """
        # super().reset()
        self._reset_generate_price()


def main():
    asset_list = ["BTC", "ATL", "TRX", "ETH", "BCH", "XRP", "LTC", "EOS", "ADA", "XMR", "LINK", "HT"]
    price_handler = SimulatedPriceHandler()
    jam = Jamboree()
    # This live variable locks certain commands, and allows us to query faster. 
    price_handler['episode'] = uuid.uuid4().hex # set this to live if we're trying to use live prices.
    price_handler['exchange'] = "binance"
    price_handler['live'] = False
    price_handler['obs_num'] = 1300
    print(price_handler['obs_num'])
    price_handler.event = jam
    price_handler.add_assets(asset_list)
    price_handler.reset()
    last_current_time = 0
    last_price_time = 0
    while True:

        obs = price_handler.step()

        # Get the observation number
        i = obs.get("step_num", 0)
        assets = obs.get("assets", {})
        done = obs.get("done", False)
        if done:
            logger.info(blue("Observation Complete"))
            break
        # print()
        latest_price = price_handler.latest_price("BTC")
        logger.info(yellow(latest_price['time']))
        logger.info(red(price_handler.current_time))
        logger.info(blue(assets['BTC'][-1]['time']))

        # print()

        # logger.info(latest_price['time'] - price_handler.current_time)
        # logger.info(assets['BTC'][-1]['time'] - price_handler.current_time)
        logger.info(price_handler.current_time - last_current_time)
        logger.info(latest_price['time'] - last_price_time)
        last_current_time = price_handler.current_time
        last_price_time = latest_price['time']


if __name__ == "__main__":
    main()