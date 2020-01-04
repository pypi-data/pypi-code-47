""" 
# BasePriceHandler

BasePriceHandler is an extension of DataHandler
"""



from jamboree import Jamboree
from loguru import logger
from crayons import yellow
from link_jam_handle.data import LiveSet
from link_jam_handle.data.pricing import PriceBaseSet
# TODO: Rethink design here and come back to this.

def is_acceptable_units(unit):
    units = ["seconds", "minutes", "hours", "days", "months", "years"]
    if unit not in units:
        return "minutes"
    return unit

class LivePriceHandler(LiveSet, PriceBaseSet):
    def __init__(self, limit=500, **kwargs):
        super().__init__(limit=limit, **kwargs)
        _units = kwargs.get("units", "minutes")
        _units = is_acceptable_units(_units)
        self.entity = "pricing"
        self['opt_type'] = "live"
        self['spacing'] = 1
        self['unit'] = _units
        self.asset_bars = {}

    
    def get_latest_many(self, symbol):
        pass
    """ 
        ----------------------------------------------------------------------------------
        ------------------------------- Counting Functions -------------------------------
        ----------------------------------------------------------------------------------
    """


    

    
    # """ ---------------------------------------------------------------------------
    #     ---------------------------- RL-Like Functions ---------------------------- 
    #     ---------------------------------------------------------------------------
    # """

    def step(self, _limit=2, alt={}):
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
        """ Reset should do nothing here. """
        logger.info("Resetting price information")

def main():
    asset_list = ["BTC", "ATL", "TRX", "ETH", "BCH", "XRP", "LTC", "EOS", "ADA", "XMR", "LINK", "HT"]
    price_handler = LivePriceHandler()
    jam = Jamboree()
    # This live variable locks certain commands, and allows us to query faster. 
    price_handler['episode'] = "live" # set this to live if we're trying to use live prices.
    price_handler['exchange'] = "binance"
    price_handler['live'] = True
    price_handler['obs_num'] = 1300
    print(price_handler['obs_num'])
    price_handler.event = jam
    price_handler.add_assets(asset_list)
    price_handler.reset()
    while True:
        obs = price_handler.step()

        # # Get the observation number
        # i = obs.get("step_num", 0)
        # assets = obs.get("assets", {})
        # done = obs.get("done", False)
        # if done:
        #     print(blue("Observation Complete"))
        #     break
        # print()
        # latest_price = price_handler.latest_price("BTC")
        # logger.info(yellow(latest_price['time']))
        # logger.info(red(price_handler.current_time))
        # logger.info(blue(assets['BTC'][-1]['time']))
    


if __name__ == "__main__":
    main()