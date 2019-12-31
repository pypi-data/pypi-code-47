# auto generated by update_py.py

import ctypes
import os
import signal
import sys
import threading
import time

from tlclient.trader.client import Client
from tlclient.trader.constant import Direction, ExchangeID, MsgType, OffsetFlag, OrderType

config_file_template = '''
Format ({} for required, [] for optional):
    client_name     {CLIENT_FIST_NAME}
    environment     {ENVIRONMENT_NAME}
    master_address  {MASTER_ADDRESS}
    trade_router    {TRADE_ROUTER_FIST_NAME}
    market_router   {MARKET_ROUTER_FIST_NAME}
Example:
    client_name     client1
    environment     local
    master_address  tcp://localhost:9000
    trade_router    trade1
    market_router   market1
'''

trade_command_description = '''
Format ({} for required, [] for optional):
    1. insert plain orders:             {DIRECTION} {VOLUMN} [{OFFSET_FLAG}] of {TICKER}.{EXCHANGE} [at {PRICE}] [{fak/fok}] on {TRADE_GATEWAY} [silently]
    2. insert twap orders:              {DIRECTION} {VOLUMN} [{OFFSET_FLAG}] of {TICKER}.{EXCHANGE}
                                            from {START_TIME} to {END_TIME} gap {INTERVAL_SECONDS} seconds on {TRADE_GATEWAY} [silently]
    3. cancel orders:                   cancel order {ORDER_ID} on {TRADE_GATEWAY} [silently]
    4. request position:                req pos on {TRADE_GATEWAY}
    5. request account:                 req acc on {TRADE_GATEWAY}
    6. request active orders:           req orders on {TRADE_GATEWAY}
    7. reqest cancel active orders      req cancel orders [REQUEST_ACTIVE_ORDERS_ID] on {TRADE_GATEWAY}
Arguments:
    1. DIRECTION: [buy, sell]
    2. OFFSET_FLAG: [open, close, force_close, close_today, close_yesterday]
    3. EXCHANGE: [sse, sze, hk, cffex, dce, shfe, czce]
Examples:
    [plain order - limit/market price]
        buy 1000 of 000001.sze on tora_trade                           # market price order
        sell 500 of 000001.sze on tora_trade silently                  # market price order without double confirm
        buy 100 of 000001.sze at 13.5 on tora_trade silently           # limit price order without double confirm
        sell 100 of 000001.sze at 1024.16 on tora_trade                # limit price order
        buy 100 open of rb1906.shfe on ctp_trade silently              # market price order without double confirm
        buy 1000 close_yesterday of rb1906.shfe on ctp_trade           # market price order
        buy 500 close_today of rb1906.shfe on ctp_trade silently       # market price order without double confirm
        buy 100 close of rb1906.shfe at 13.5 on ctp_trade              # limit price order
        buy 100 open of rb1906.shfe at 13.5 fok on ctp_trade           # fok order
        sell 100 close of rb1906.shfe at 1024.16 fak on ctp_trade      # fak order
    [algo order - twap]
        buy 1000 of 000001.sze from 20190417-093000 to 20190417-103000 gap 10 seconds on tora_trade silently  # twap order without double confirm
        sell 800 of 000001.sze from 20190418-101800 to 20190418-104500 gap 10 seconds on tora_trade           # twap order
        buy 1000 open of rb1906.shfe from 20190417-093000 to 20190417-103000 gap 10 seconds on ctp_trade      # twap order
        sell 800 close of rb1906.shfe from 20190418-101800 to 20190418-104500 gap 10 seconds on ctp_trade     # twap order
    [cancel orders]
        cancel order 37 on tora_trade silently                         # cancel order (id: 37) in stock market without double confirm
        cancel order 25 on ctp_trade                                   # cancel order (id: 25) in future market
    [request infomation]
        req pos on tora_trade                                          # request position in stock market
        req acc on tora_trade                                          # request account infomation in stock market
        req orders on tora_trade                                       # request active orders in stock market
        req pos on ctp_trade                                           # request position in future market
        req acc on ctp_trade                                           # request account infomation in future market
        req orders on ctp_trade                                        # request active orders in future market
        req cancel orders on ctp_trade                                 # request cancel active orders in future market
        req cancel orders 1001 on ctp_trade                            # request cancel active orders in future market
'''

subscribe_market_data_command_description = '''
Format ({} for required, [] for optional):
    1. subsribe market data snap:       sub {TICKER}.{EXCHANGE} [snap]
    2. subsribe market data bar:        sub {TICKER}.{EXCHANGE} bar
    3. subsribe market data index:      sub {TICKER}.{EXCHANGE} index
    4. subsribe market data order:      sub {TICKER}.{EXCHANGE} order
    5. subsribe market data trade:      sub {TICKER}.{EXCHANGE} trade
Arguments:
    1. EXCHANGE: [sse, sze, hk, cffex, dce, shfe, czce]
Examples:
    sub rb1906.shfe snap                                               # subsribe market data snap of rb1906.shfe
    sub rb1906.shfe                                                    # same as above, "snap" is optional
    sub 000001.sze bar                                                 # subsribe market data bar of 000001.sze
    sub 000001.sze index                                               # subsribe market data index of 000001.sze
    sub rb1906.shfe order                                              # subsribe market data order of rb1906.shfe
    sub 000001.sze trade                                               # subsribe market data trade of 000001.sze
'''

insert_order_confirm_template = '''
Trade Gateway:      {}
Direction:          {}
Ticker:             {}
Exchange:           {}
Volumn              {}
Price:              {}
Order Type:         {}
Offset Flag:        {}
'''

cancel_order_confirm_template = '''
Trade Gateway:      {}
Order Id:           {}
'''

command_prompt = 'Please type in command. Type in "H"/"h" for help.\n> '
input_prompt = 'Type "Q"/"q" to exit, or type "I"/"i" to insert command.'
confirm_prompt = 'Please type in "Y"/"y" for confirmation, and any other key for cancellation.\n'

all_command_description = '''
1. Trade
{}
2. Subscribe Market Data
{}'''.format(trade_command_description, subscribe_market_data_command_description)

valid_commands =        ['buy', 'sell', 'cancel', 'req', 'sub']
valid_exchange =        {'sse': ExchangeID.SSE, 'sze': ExchangeID.SZE, 'hk': ExchangeID.HK,
                         'cffex': ExchangeID.CFFEX, 'dce': ExchangeID.DCE, 'shfe': ExchangeID.SHFE, 'czce': ExchangeID.CZCE}
valid_message_types =   {'snap': MsgType.MKT_SNAP, 'bar': MsgType.MKT_BAR, 'index': MsgType.MKT_INDEX,
                         'order': MsgType.MKT_ORDER, 'trade': MsgType.MKT_TRADE}
valid_offset_flags =    {'open': OffsetFlag.OPEN, 'close': OffsetFlag.CLOSE, 'force_close': OffsetFlag.FORCE_CLOSE,
                         'close_today': OffsetFlag.CLOSE_TODAY, 'close_yesterday': OffsetFlag.CLOSE_YESTERDAY}
valid_requests =        ['pos', 'acc', 'orders', 'cancel']

# use print lock to avoid terrible content format when interacting with multi-threads application in console
print_lock = threading.Lock()

def sprint(content):
    with print_lock:
        print(content)

class SampleClient(Client):
    def __init__(self, config_file):
        # step 1: load config file
        config_dict = {}
        fields = ['client_name', 'environment', 'master_address', 'trade_router', 'market_router']
        with open(config_file, 'r') as fconfig:
            for line in fconfig:
                if not line.strip():
                    continue
                parts = line.split()
                if len(parts) != 2:
                    sprint('Error in config file. Please refer to below.\n{}'.format(config_file_template))
                    raise Exception('Line "{}" is invalid in config file.'.format(line))
                if parts[0] in fields:
                    config_dict[parts[0]] = parts[1]

        for field in fields:
            if field not in config_dict:
                sprint('Error in config file. Please refer to below.\n{}'.format(config_file_template))
                raise Exception('{} is not found in config file'.format(field))

        # step 2: client fist initialization
        client_name = config_dict['client_name']
        environment = config_dict['environment']
        master_address = config_dict['master_address']
        Client.__init__(self, name=client_name, env_name=environment, addr=master_address)

        # step 3: set trade router and market router
        trade_router = config_dict['trade_router']
        market_router = config_dict['market_router']
        self.init_trade(trade_router)
        self.init_market(market_router)

    # overrided trade functions
    def on_rsp_order_insert(self, obj, frame_nano):
        sprint('[rsp_order_insert] ' + str(obj))

    def on_rsp_order_cancel(self, obj, frame_nano):
        sprint('[rsp_order_cancel] ' + str(obj))

    def on_rtn_order(self, obj, frame_nano):
        sprint('[rtn_order] ' + str(obj))

    def on_rtn_trade(self, obj, frame_nano):
        sprint('[rtn_trade] ' + str(obj))

    def on_rsp_position(self, obj, frame_nano):
        sprint('[rsp_position] ' + str(obj))

    def on_rsp_account(self, obj, frame_nano):
        sprint('[rsp_account] ' + str(obj))

    def on_rsp_active_orders(self, obj, frame_nano):
        sprint('[rsp_active_orders] ' + str(obj))

    def on_rsp_cancel_active_orders(self, obj, frame_nano):
        sprint('[rsp_cancel_active_orders] ' + str(obj))

    # overrided market data functions
    def on_mkt_snap(self, obj, msg_type, frame_nano):
        with print_lock:
            print(obj, msg_type)
            print(obj.ticker, ExchangeID.read(obj.exchange), obj.mkt_time,
                  'b: {}'.format(obj.bid_price[0]), 'a: {}'.format(obj.ask_price[0]))
            for i in range(0, 10):
                print('\tb: {}@{} \ta: {}@{}'.format(obj.bid_volume[i], obj.bid_price[i],
                    obj.ask_volume[i], obj.ask_price[i]))

    def on_mkt_bar(self, obj, msg_type, frame_nano):
        sprint('[market_data_bar] ' + str(obj))

    def on_mkt_index(self, obj, msg_type, frame_nano):
        sprint('[market_data_index] ' + str(obj))

    def on_mkt_order(self, obj, msg_type, frame_nano):
        sprint('[market_data_order] ' + str(obj))

    def on_mkt_trade(self, obj, msg_type, frame_nano):
        sprint('[market_data_trade] ' + str(obj))

class TimeoutException(Exception):
    pass

class ConsoleClient:
    def __init__(self, config_file):
        self.sc = SampleClient(config_file)

    def signal_handler(self, signum=None, frame=None):
        if signum == signal.SIGALRM:
            raise TimeoutException
        else:
            raise KeyboardInterrupt

    def parse_symbol(self, symbol):
        parts = symbol.split('.')
        if len(parts) != 2:
            return [False, 'symbol "{}" is not in TICKER.EXCHANGE format'.format(symbol)]
        ticker = parts[0].strip()
        if not ticker:
            return [False, 'ticker "{}" is not valid'.format(ticker)]
        if parts[1] not in valid_exchange:
            return [False, 'exchange "{}" cannot be recognized'.format(parts[1])]
        return [True, ticker, valid_exchange[parts[1]]]

    def parse_message_types(self, message_type):
        if message_type not in valid_message_types:
            return [False, 'message_type "{}" cannot be recognized'.format(message_type)]
        return [True, valid_message_types[message_type]]

    def process_subscribe_command(self, parts):
        if len(parts) != 2 and len(parts) != 3:
            return [False, 'subscribe command should have 2 or 3 parts, but {} parts are given'.format(len(parts))]

        symbol_parse_result = self.parse_symbol(parts[1])
        if not symbol_parse_result[0]:
            return symbol_parse_result
        ticker = symbol_parse_result[1]
        exchange = symbol_parse_result[2]

        if len(parts) == 2:
            message_type = MsgType.MKT_SNAP
        else:
            message_type_parse_result = self.parse_message_types(parts[2])
            if not message_type_parse_result[0]:
                return message_type_parse_result
            message_type = message_type_parse_result[1]

        if not self.sc.subscribe(exchange, ticker, message_type):
            return [False, 'subscribe failed']
        return [True]

    def parse_volumn(self, volumn_str):
        try:
            volumn = int(volumn_str)
            if volumn <= 0:
                return [False, '{} is not a valid volumn'.format(volumn_str)]
        except ValueError:
            return [False, '{} is not a valid volumn'.format(volumn_str)]
        return [True, volumn]

    def parse_id(self, id_str):
        try:
            id = int(id_str)
            if id <= 0:
                return [False, '{} is not a valid id'.format(id_str)]
        except ValueError:
            return [False, '{} is not a valid id'.format(id_str)]
        return [True, id]

    def parse_price(self, price_str):
        try:
            price = float(price_str)
            if price < 0:
                return [False, '{} is not valid price'.format(price_str)]
        except ValueError:
            return [False, '{} is not valid price'.format(price_str)]
        return [True, price]

    def parse_offset_flag(self, offset_flag_str):
        if offset_flag_str not in valid_offset_flags:
            return [False, '{} is not valid offset_flag'.format(offset_flag_str)]
        return [True, valid_offset_flags[offset_flag_str]]

    def process_trade_buy_or_sell_command(self, parts):
        # 1. parse buy/sell
        part_index = 0
        if parts[part_index] == 'buy':
            direction = Direction.BUY
        else:
            direction = Direction.SELL

        # 2. parse volumn
        part_index += 1
        if len(parts) < part_index + 1:
            return [False, 'no valid volumn found']
        volumn_parse_result = self.parse_volumn(parts[part_index])
        if not volumn_parse_result[0]:
            return volumn_parse_result
        volumn = volumn_parse_result[1]

        # 3. parse offset (if exists) and symbol
        part_index += 1
        if len(parts) < part_index + 1:
            return [False, 'missing symbol in command']
        if parts[part_index] != 'of':
            # 3.1. parse offset
            offset_flag_parse_result = self.parse_offset_flag(parts[part_index])
            if not offset_flag_parse_result[0]:
                return offset_flag_parse_result
            offset_flag = offset_flag_parse_result[1]
            part_index += 1
            if len(parts) < part_index + 1:
                return [False, 'missing "of" before symbol in command']
            if parts[part_index] != 'of':
                return [False, 'missing "of" before symbol in command']
        else:
            offset_flag = OffsetFlag.NOT_AVAILABLE
        # 3.2. parse symbol
        part_index += 1
        if len(parts) < part_index + 1:
            return [False, 'no symbol in command']
        symbol_parse_result = self.parse_symbol(parts[part_index])
        if not symbol_parse_result[0]:
            return symbol_parse_result
        ticker = symbol_parse_result[1]
        exchange = symbol_parse_result[2]

        # 4. parse price (if exists) and twap arguments (if exists)
        part_index += 1
        if len(parts) < part_index + 1:
            return [False, 'missing trade gateway in command']
        if parts[part_index] == 'at':
            # 4.1. parse price
            part_index += 1
            if len(parts) < part_index + 1:
                return [False, 'no price in limit order command']
            price_parse_result = self.parse_price(parts[part_index])
            if not price_parse_result[0]:
                return price_parse_result
            price = price_parse_result[1]
            order_type = OrderType.LIMIT
            part_index += 1
            if len(parts) < part_index + 1:
                return [False, 'missing trade gateway in command']
        elif parts[part_index] == 'from':
            # 4.2. parse twap arguments (start_time, end_time and sec_interval)
            # TODO: twap order
            return [False, 'TWAP order insert is not implemented']
            pass
        else:
            order_type = OrderType.MARKET
            price = 0.0

        # 4. parse fak/fok flag (if exists)
        if parts[part_index] == 'fak':
            order_type = OrderType.FAK
            part_index += 1
            if len(parts) < part_index + 1:
                return [False, 'missing trade gateway in command']
        elif parts[part_index] == 'fak':
            order_type = OrderType.FOK
            part_index += 1
            if len(parts) < part_index + 1:
                return [False, 'missing trade gateway in command']

        # 5. parse trade gateway
        if parts[part_index] != 'on':
            return [False, 'trade gateway name is not following "on" in command']
        part_index += 1
        if len(parts) < part_index + 1:
            return [False, 'missing trade gateway in command']
        trade_gateway = parts[part_index]

        # 6. parse silently flag (if exists)
        part_index += 1
        if len(parts) == part_index + 1:
            if (parts[part_index] == 'silently'):
                silently = True
            else:
                return [False, 'unrecognized command arguments "{}"'.format(parts[part_index])]
        elif len(parts) < part_index + 1:
            silently = False
        else:
            return [False, 'redundant command arguments "{}"'.format(parts[part_index + 1])]

        # 7. insert order
        if not silently:
            with print_lock:
                print(insert_order_confirm_template.format(trade_gateway, Direction.read(direction), ticker,
                            ExchangeID.read(exchange), volumn, price, OrderType.read(order_type), OffsetFlag.read(offset_flag)))
                confirm = self.get_user_input(confirm_prompt)
                if confirm == 'Y' or confirm == 'y':
                    order_id = self.sc.insert_order(tg_name = trade_gateway, exchange = exchange, ticker = ticker, price = price,
                            volume = volumn, order_type = order_type, direction = direction, offset_flag=offset_flag)
                    if order_id == -1:
                        print('Order insert error')
                    else:
                        print('Order with id {} has been inserted.'.format(order_id))
                else:
                    print('"{}" typed, order not sent out.'.format(confirm))
        else:
            order_id = self.sc.insert_order(tg_name = trade_gateway, exchange = exchange, ticker = ticker, price = price,
                    volume = volumn, order_type = order_type, direction = direction, offset_flag=offset_flag)
            if order_id == -1:
                sprint('Order insert error')
            else:
                sprint('Order with id {} has been inserted.'.format(order_id))

        return [True]

    def process_cancel_order_command(self, parts):
        if len(parts) != 5 and len(parts) != 6:
            return [False, 'cancel order command part number should be 5 or 6, but here is {}'.format(len(parts))]
        if parts[1] != 'order':
            return [False, '"order" keyword is supposed to be after "cancel"']

        parse_id_result = self.parse_id(parts[2])
        if not parse_id_result[0]:
            return parse_id_result
        order_id = parse_id_result[1]

        if parts[3] != 'on':
            return [False, '"on" keyword is needed before trade router name']
        trade_gateway = parts[4]
        if len(parts) == 6:
            if (parts[5] == 'silently'):
                silently = True
            else:
                return [False, 'unrecognized command argument "{}"'.format(parts[5])]
        else:
            silently = False

        if not silently:
            with print_lock:
                print(cancel_order_confirm_template.format(trade_gateway, order_id))
                confirm = self.get_user_input(confirm_prompt)
                if confirm == 'Y' or confirm == 'y':
                    request_id = self.sc.cancel_order(order_id = order_id, tg_name = trade_gateway)
                    print('Order cancel request {} has been sent.'.format(request_id))
                else:
                    print('"{}" typed, order not sent out.'.format(confirm))
        else:
            request_id = self.sc.cancel_order(order_id = order_id, tg_name = trade_gateway)
            sprint('Order cancel request {} has been sent.'.format(request_id))

        return [True]

    def process_request_command(self, parts):
        if len(parts) < 2:
            return [False, 'request command part number should be 4 or 5, but here is {}'.format(len(parts))]
        req_target = parts[1]
        if req_target not in valid_requests:
            return [False, '{} is not a valid request'.format(parts[1])]

        if req_target == 'cancel':
            # process cancel active orders request
            if len(parts) < 5:
                return [False, 'request cancel active orders command part number should be 5 or 6, but here is {}'.format(len(parts))]
            if parts[2] != 'orders':
                return [False, 'missing "orders" in request to cancel active orders']
            if parts[3] != 'on':
                if len(parts) != 6:
                    return [False, 'request cancel active orders with id command part number should be 6, but here is {}'.format(len(parts))]
                req_active_orders_id = parts[3]
                if parts[4] == 'on':
                    trade_gateway = parts[5]
                else:
                    return [False, '"on" keyword is needed before trade router name']
            else:
                if len(parts) != 5:
                    return [False, 'request cancel active orders without id command part number should be 5, but here is {}'.format(len(parts))]
                req_active_orders_id = None
                trade_gateway = parts[4]
            # send request
            if req_active_orders_id is not None:
                parse_id_result = self.parse_id(req_active_orders_id)
                if not parse_id_result[0]:
                    return parse_id_result
                req_active_orders_id = parse_id_result[1]
                request_id = self.sc.req_cancel_active_orders(tg_name = trade_gateway, req_active_orders_id = req_active_orders_id)
            else:
                request_id = self.sc.req_cancel_active_orders(tg_name = trade_gateway)
        else:
            # process request for pos/acc/active_orders
            if len(parts) != 4:
                return [False, 'request {} command part number should be 4, but here is {}'.format(req_target, len(parts))]
            if parts[2] != 'on':
                return [False, '"on" keyword is needed before trade router name']
            trade_gateway = parts[3]

            # send request
            if req_target == 'pos':
                request_id = self.sc.req_position(tg_name = trade_gateway)
            if req_target == 'acc':
                request_id = self.sc.req_account(tg_name = trade_gateway)
            if req_target == 'orders':
                request_id = self.sc.req_active_orders(tg_name = trade_gateway)

        sprint('Request for {} has been sent, with id {}.'.format(req_target, request_id))

        return [True]

    def process_trade_command(self, parts):
        if parts[0] == 'buy' or parts[0] == 'sell':
            buy_sell_process_result = self.process_trade_buy_or_sell_command(parts)
            if not buy_sell_process_result[0]:
                return buy_sell_process_result

        if parts[0] == 'cancel':
            cancel_order_result = self.process_cancel_order_command(parts)
            if not cancel_order_result[0]:
                return cancel_order_result

        if parts[0] == 'req':
            request_result = self.process_request_command(parts)
            if not request_result[0]:
                return request_result

        return [True]

    def process_command(self, line):
        if line == 'H' or line == 'h':
            time.sleep(0.5)
            sprint(all_command_description)
            return
        parts = line.split()
        if len(parts) == 0:
            sprint('Command is empty.')
            return

        if parts[0] not in valid_commands:
            sprint('Unrecognized command "{}".'.format(line))
            return

        if parts[0] == 'sub':
            subscribe_command_process_result = self.process_subscribe_command(parts)
            if not subscribe_command_process_result[0]:
                sprint('Command syntax error "{}". Detail: {}'.format(line, subscribe_command_process_result[1]))
        else:
            trade_command_process_result = self.process_trade_command(parts)
            if not trade_command_process_result[0]:
                sprint('Command syntax error "{}". Detail: {}'.format(line, trade_command_process_result[1]))

    def get_user_input(self, prompt = ''):
        if sys.version_info[0] == 2:
            line = raw_input(prompt)
        elif sys.version_info[0] == 3:
            line = input(prompt)

        return line.strip()

    def run(self):
        self.sc.start()
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGALRM, self.signal_handler)
        sprint(input_prompt)
        while True:
            try:
                signal.alarm(1)
                with print_lock:
                    line = self.get_user_input()
                signal.alarm(0)

                if line == 'Q' or line == 'q':
                    # type a single char 'Q' or 'q' to exit
                    break
                elif line == 'I' or line == 'i':
                    # type a single char 'I' or 'i' to insert command
                    with print_lock:
                        line = self.get_user_input(command_prompt)
                    # Process actual command
                    self.process_command(line)
                else:
                    sprint('Error in "{}". {}'.format(line, input_prompt))

                time.sleep(0.01)

            except TimeoutException:
                time.sleep(0.01)
                continue
            except KeyboardInterrupt:
                signal.alarm(0)
                sprint('Interative test is going to exit.')
                break

        self.sc.stop()
        self.sc.join()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        if not os.path.exists('console_client.cfg'):
            sprint('Could not find configuration file. Please create one as below.\n{}'.format(config_file_template))
        else:
            client = ConsoleClient('console_client.cfg')
    else:
        client = ConsoleClient(sys.argv[1])

    client.run()










# Appendix
# obsolete, just for reference of available commands
obsolete_commands = '''
----------------------
<command> [<args>]
The supported commands are:
    insert          insert order. Return value: order id
        -g              trade gateway name, e.g. tora1
        -e              exchange (SSE/SZE/HK/CFFEX/DCE/SHFE/CZCE), e.g. SZE
        -s              stock ticker, e.g. 000001
        -v              volumn, integer e.g. 100
        -d              direction (BUY/SELL), e.g. BUY
        -t              type, plain/twap, e.g. plain
        -of             [FUTURE ONLY] offset_flag (OPEN/CLOSE/FORCE_CLOSE/CLOSE_TODAY/CLOSE_YESTERDAY), e.g. OPEN
        -ot             [PLAIN ORDER ONLY] order type (LIMIT/MARKET/FAK/FOK), e.g. LIMIT
        -p              [PLAIN ORDER ONLY] [LIMIT ORDER ONLY] price, float, e.g. 13.0
        -st             [TWAP ORDER ONLY] start time, e.g. 20190417-093000
        -et             [TWAP ORDER ONLY] end time, e.g.20190417-103000
        -ivl            [TWAP ORDER ONLY] interval (in seconds) between two child orders, e.g. 10
    cancel          cancel order
        -g              trade gateway name, e.g. tora1
        -i              order id
    req             request position/account/active orders
        -t              type, pos(for position)/acc(for account)/orders(for active orders), e.g. pos
        -g              trade gateway name, e.g. tora1
    sub             subscribe market data
        -g              market gateway name, e.g. tora_market
        -t              type, snap/bar/index/order/trade
----------------------
'''
