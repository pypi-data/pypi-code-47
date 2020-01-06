import datetime
import sys
import requests
import re
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium
from catscore.session import CatsRequestSession, CatsWebDriverSession
from catscore.logger import CatsLogging as logging
from catscore.time import get_today_date, get_current_time

class InitPageError(RuntimeError):
    pass

class TransitionFailedError(RuntimeError):
    pass

class DataConsistencyError(RuntimeError):
    pass

class DemoGMOStockBinary:
    order_url = "https://demo.click-sec.com/ixop/order.do"
    
    def __init__(self, binary_location, executable_path, headless, proxy=None):
        """[summary]
        
        Arguments:
            binary_location {[type]} -- [description]
            executable_path {[type]} -- [description]
            headless {[type]} -- [description]
        
        Keyword Arguments:
            proxy {[type]} -- [description] (default: {None})
        """
        self.binary_location = binary_location
        self.executable_path = executable_path
        self.headless =  headless
        self.proxy = proxy
        self.request = CatsRequestSession()
        self.session = CatsWebDriverSession(binary_location=self.binary_location, executable_path=self.executable_path, proxy=self.proxy, headless=self.headless)
        
    def init(self):
        self._init_page(click_skip=True)

    def _init_page(self, click_skip, timeout=1):
        """[ページの初期化]
        
        Arguments:
            click_skip {[type]} -- [description]
        """
        self.session.driver.get(self.order_url)
        if click_skip:
            # check
            error_count = 0
            skipped = 4
            while True:
                try:
                    self.session.wait_rendering_by_class('joyride-tooltip__button')
                    self.session.wait_rendering_by_class('round-list')
                    for i in range(skipped):
                        logging.info(f"_init_page skip {i}")
                        button = self.session.driver.find_elements_by_css_selector(".joyride-tooltip__button.joyride-tooltip__button--primary")[0]
                        button.click()
                        time.sleep(1)
                        skipped = skipped -1
                    logging.info("_init_page success")
                    return True
                except:
                    if error_count < 3:
                        logging.info(f"__init_page error count is {error_count}")
                        error_count = error_count + 1
                        time.sleep(timeout)
                    else:
                        logging.info(f"__init_page is failed: {sys.exc_info()}")
                        self.reload()
                        raise InitPageError(f"__init_page is failed: {sys.exc_info()}")
    
    def close(self):
        """[close DemoGMOStockBinary]
        """
        self.session.close()
        self.request.close()

    def restart(self):
        """[Restart browser]
        """
        logging.info("GMOStockBinaryDemoWebSession restart")
        self.session.close()
        self.session = CatsWebDriverSession(binary_location=self.binary_location, executable_path=self.executable_path, proxy=self.proxy, headless=self.headless)
        self._init_page(click_skip=True)
        
    def reload(self):
        logging.info("DemoGMOStockBinary reload")
        self.session.reload()

    def is_open(self):
        """[ToDo: check market is open or close]
        """
        pass

    @property
    def trading_name(self):
        """[ 現在の銘柄を取得]
        
        Returns:
            [type] -- [description]
        """
        name = self.session.html().find('button', {'class': 'currency-list-button on'}).text
        logging.info(f"trading_name is {name}")
        return name

    def transition_trading(self, trading_name):
        """[銘柄を変更]
        
        Arguments:
            id {[trading_name]} -- [日本225 or 米国30]
        """
        current_trading_name = self.trading_name
        if current_trading_name != trading_name: # 遷移が必要ない場合は遷移しない
            logging.info(f"transition_trading transition {current_trading_name} to {trading_name}")
            if trading_name == "米国30":
                id = 1
            else:
                id = 0
            button = self.session.driver.find_elements_by_css_selector(".currency-list-button")[id]
            button.click()

            # check
            error_count = 0
            while True:
                current_trading_name = self.trading_name
                logging.info(f"transition_trading transitioned {current_trading_name}")
                if trading_name == current_trading_name:
                    return True
                elif error_count == 4:
                    raise TransitionFailedError("transition_trading is failed")
                else:
                    error_count = error_count + 1
                    logging.info(f"transition_trading error count is : {error_count}")

    @property
    def round_list(self):
        """[ラウンド一覧を取得]
        
        Returns:
            [type] -- [description]
        """
        round_list = self.session.html().find('div', {'class': 'round-list'})
        buttons = round_list.findAll('button')
        round_list = list(filter(lambda x: x[0][0] == 'round-list-button', map(lambda x: (x.get("class"), x), buttons)))
        logging.info(f"round_list: {round_list}")
        return round_list

    @property
    def accept_round_list(self):
        """[Acceptステータスのラウンド一覧を取得]
        
        Returns:
            [type] -- [description]
        """
        accept_round_list = list(filter(lambda x: (x[0][1] == 'ACCEPT'), self.round_list))
        logging.info(f"accept_round_list is {accept_round_list}")
        return accept_round_list

    def transtion_accept_round(self, round):
        """[acceptステータスのラウンドを移動]
        
        Arguments:
            round {[type]} -- [first or second]
        """
        if round == "first":
            round_id = 0
        elif round == "second":
            round_id = 1
        else:
            round_id = 0
        accept_round_list = self.accept_round_list
        if len(accept_round_list) < 1:
            raise TransitionFailedError("transtion_accept_round round is not open")
        elif len(accept_round_list) == 1 and round == "second":
            raise TransitionFailedError("transtion_accept_round round second is not open")
        transition_round = accept_round_list[round_id][1]
        current_round = self.round
        logging.info(f"transtion_accept_round: current_round is {current_round.text}, transition_round is {transition_round.text}")
        if current_round.text != transition_round.text:
            logging.info("transtion_accept_round: transition round")
            buttons = self.session.driver.find_elements_by_css_selector(".round-list-button.ACCEPT")[round_id]
            buttons.click()
        # check
        for i in range(4):
            transitioned_round = self.round
            if transition_round.text == transitioned_round.text:
                logging.info(f"transtion_accept_round: {current_round.text} to {transitioned_round.text}")
                return True
            else:
                logging.info(f"transtion_accept_round: error count is {i}")
        raise TransitionFailedError("transtion_accept_round is failed")

    @property
    def round(self):
        """[現在のラウンドを取得]
        """
        round = list(filter(lambda x: (x[0][-1] == 'on'), self.round_list))
        if len(round) != 1:
            raise RuntimeError(f"round: current round len are {round}")
        else:
            logging.info(f"round: {round[0][1]}")
            return round[0][1]

    @property
    def stock_price(self):
        """[現在の株価情報を取得]

        Returns:
            [type] -- [description]
        """
        trading_name = self.trading_name
        if trading_name == "日本225":
            stock_price_url = "https://demo.click-sec.com/boquote/api/v3/chart?underlierCd=000001&count=1&type=MIN_1"
        elif trading_name == "米国30":
            stock_price_url = "https://demo.click-sec.com/boquote/api/v3/chart?underlierCd=000002&count=1&type=MIN_1"
        json = self.request.get(stock_price_url, response_content_type="json")[1][0]
        logging.info(f"stock_price: {json}")
        return json

    @property
    def order_info(self):
        """[オーダ情報を取得]
        
        Returns:
            [type] -- [description]
        """
        def __parse_oder_panel(order_panel):
            buy = order_panel.find('span', {'class': 'order-buy-price'}).text
            sell = order_panel.find('span', {'class': 'order-sell-price'}).text
            payout_price = order_panel.find('span', {'class': 'order-payout-price'}).text
            return {"buy": buy, "sell": sell, "payout_price": payout_price}

        trade_panel = self.session.html().find('div', {'class': 'trade-panel'})
        panel_put = __parse_oder_panel(trade_panel.find('div', {'class': 'panel-put'}))
        panel_call = __parse_oder_panel(trade_panel.find('div', {'class': 'panel-call'}))
        r = {"put": panel_put, "call": panel_call}
        logging.info(f"order_info: {r}")
        return r

    @property
    def condition_list(self):
        """[権利行使価格一覧を取得]
        """
        target_selector = self.session.html().find('select', {'class': 'select-strike-price'})
        result = list(map(lambda selector: {"target_price": selector.text, "selector_value": selector["value"]}, target_selector))
        logging.info(f"condition_list: {result}")
        return result

    @property
    def condition(self):
        selectable_selector = Select(self.session.driver.find_element_by_class_name('select-strike-price'))
        result = {"target_price": selectable_selector.first_selected_option.text, "selector_value": selectable_selector.first_selected_option.get_property("value")}
        logging.info(f"condition: {result}")
        return result

    def transion_condition(self, value: str):
        """[summary]
        
        Arguments:
            value {[str]} -- [From 1 to 7]
        """
        before_value = self.condition["selector_value"]
        if before_value != value:
            logging.info("transion_condition")
            selectable_selector = Select(self.session.driver.find_element_by_class_name('select-strike-price'))
            selectable_selector.select_by_value(value) # select pulldown
        # check
        for i in range(4):
            current_value = self.condition["selector_value"]
            if value == current_value:
                logging.info(f"transion_condition: {before_value} to {current_value}")
                return True
            else:
                logging.info(f"transion_condition: error count is {i}")
        raise TransitionFailedError("transion_condition is failed")

    @property
    def condition_info(self):
        r =  {"trading_name": self.trading_name, "timestamp": get_current_time(), "round_date": get_today_date(), "round_name": self.round.text, "condition": self.condition, "order_info": self.order_info, "stock_price": self.stock_price}
        logging.info(f"condition_info result: {r}")
        return r

    def round_info(self, round):
        self.transtion_accept_round(round)
        condition_info = []
        timestamp = get_current_time()
        stock_info = self.stock_price
        for c in self.condition_list:
            self.transion_condition(c["selector_value"])
            condition_info.append({"condition": self.condition, "order_info": self.order_info})
        r =  {"trading_name": self.trading_name, "timestamp": get_current_time(), "round_date": get_today_date(), "round_name": self.round.text, "condition_info": condition_info, "stock_price": self.stock_price}
        logging.info(f"round_info: {r}")
        return r
    
    def all_round_info(self, trading_name):
        self.transition_trading(trading_name)
        accept_round_list = self.accept_round_list
        result = []
        if len(accept_round_list) == 1:
            result.append(self.round_info("first"))
        elif len(accept_round_list) == 2:
            result.append(self.round_info("first"))
            result.append(self.round_info("second"))
        return result