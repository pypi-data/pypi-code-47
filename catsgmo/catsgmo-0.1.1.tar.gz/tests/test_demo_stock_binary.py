import unittest
import sys

from catsgmo.demo_stock_binary import DemoGMOStockBinary
from catscore.logger import CatsLogging as logging
import time
import catsgmo
import pandas as pd

class TestDemoGMOStockBinary(unittest.TestCase):
    logging.init("TestDemoGMOStockBinary", "/tmp", "info")
    logging.info("TestDemoGMOStockBinary test start")
    
    binary_location="/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
    executable_path="/Users/rv/workspace/docker/finance_db/tools/chromedriver"
    headless=True

    def test_basic(self):
        demo = DemoGMOStockBinary(binary_location=self.binary_location, executable_path=self.executable_path, headless=self.headless)

        # transition_trading
        ## transtion to 日本225 → 米国30
        demo.transition_trading("米国30")
        self.assertEqual(demo.trading_name, "米国30")

        ## transtion to 米国30 → 日本225
        demo.transition_trading("日本225")
        self.assertEqual(demo.trading_name, "日本225")
        
        ## transtion to 日本225 → 日本225
        demo.transition_trading("日本225")
        self.assertEqual(demo.trading_name, "日本225")
        
        # get_round_list
        demo.transition_trading("日本225")
        demo.round_list
        demo.transition_trading("米国30")
        demo.round_list
        
        # get_accept_round_list
        demo.transition_trading("日本225")
        demo.round_list
        demo.transition_trading("米国30")
        demo.round_list
        
        # transtion_accept_round
        demo.transition_trading("日本225")
        demo.round
        ## round first to first
        demo.transtion_accept_round("first")
        ## round first to second
        #demo.transtion_accept_round("second")
        
        # get_stock_price
        demo.transition_trading("米国30")
        demo.stock_price
        
        #get_order_info
        demo.transition_trading("日本225")
        demo.order_info
        
        #get_condition_list
        demo.transition_trading("米国30")
        demo.condition_list
        demo.condition
        demo.transion_condition("1")
        
        # round_info
        demo.round_info

        # close
        demo.close()

    def test_performance(self):
        demo = DemoGMOStockBinary(binary_location=self.binary_location, executable_path=self.executable_path, headless=self.headless)
        def _check(tag, fun):
            result = []
            round = 10
            error = 0
            print(tag)
            for i in range(round):
                start = time.time()
                try:
                    fun()
                except catsgmo.demo_stock_binary.DataConsistencyError:
                    error = error + 1
                    #print(sys.exc_info())
                result.append(time.time() - start)
            df = pd.DataFrame({'time':result})
            print(f"round: {round}")
            print(f"error: {error}")
            print(df.describe())
        #_check("order_info", lambda : demo.order_info)
        _check("round_info", lambda : demo.round_info("米国30","first"))
        # close
        demo.close()
        
if __name__ == "__main__":
    unittest.main()