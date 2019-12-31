# auto generated by update_py.py

import json

import tlclient.trader.message_common as message_common
import tlclient.trader.message_market as message_market
import tlclient.trader.message_trade as message_trade

from tlclient.linker.constant import FistType
from tlclient.linker.fist import Fist
from tlclient.linker.frame import Frame
from tlclient.linker.timer import Timer
from tlclient.linker.utility import bytify
import tlclient.linker.message_comm as message_linker
from tlclient.linker.constant import MsgType as LinkerMsgType
from tlclient.trader.constant import (AssetType, BarType, ExchangeID, MsgType,
                             OffsetFlag, OrderType, TradingStyle)
from tlclient.trader.data_manager.dm_client import DMClient


class Client(Fist):

    def __init__(self, name, env_name, addr):
        Fist.__init__(self, name, FistType.CLIENT, env_name)
        self.set_master_addr(addr)
        self.create_fist()
        self.trade_router = None
        self.market_router = None
        self.oms_name = None
        self.dm_client = None
        self._msg_callbacks = {}

    def init_trade(self, router_name):
        self.reg_req(router_name)
        self.reg_sub(router_name)
        self.trade_router = router_name

    def init_market(self, router_name):
        self.reg_req(router_name)
        self.reg_sub(router_name)
        self.market_router = router_name

    def auto_init_trade(self):
        self.auto_reg_req(FistType.TRADE_ROUTER)
        self.auto_reg_sub(FistType.TRADE_ROUTER)
        self.logger.info('[auto_init] to auto reg trade router...')

    def auto_init_market(self):
        self.auto_reg_req(FistType.MARKET_ROUTER)
        self.auto_reg_sub(FistType.MARKET_ROUTER)
        self.logger.info('[auto_init] to auto reg market router...')

    def init_oms(self, oms_name):
        self.reg_req(oms_name)
        self.oms_name = oms_name

    def init_dm(self, api_key, secret_key):
        self.dm_client = DMClient(api_key, secret_key)

    #####################
    # trading functions #
    #####################

    def get_order_info(self, order_id):
        if self.oms_name is None:
            self.logger.error('[get_order_info] oms has not been inited!')
            return None
        req = message_trade.ReqOrderInfo()
        req.order_id = order_id
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.oms_name, req, MsgType.REQ_ORDER_INFO, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            order_info = ret.get_obj(message_trade.RspOrderInfo)
            return order_info
        else:
            self.logger.error('[get_order_info] error occurred (eid){}'.format(err_id))
            return None

    def get_position(self, tg_name):
        if self.oms_name is None:
            self.logger.error('[get_position] oms has not been inited!')
            return None
        req = message_trade.ReqPosition()
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.oms_name, req, MsgType.REQ_POSITION, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            pos_d = json.loads(ret.get_string())
            pos_obj = message_trade.RspPosition(pos_d)
            return pos_obj
        else:
            self.logger.error('[get_position] error occurred (eid){}'.format(err_id))
            return None

    def get_account(self, tg_name):
        if self.oms_name is None:
            self.logger.error('[get_account] oms has not been inited!')
            return None
        req = message_trade.ReqAccount()
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.oms_name, req, MsgType.REQ_ACCOUNT, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            acc_obj = ret.get_obj(message_trade.RspAccount)
            return acc_obj
        else:
            self.logger.error('[get_account] error occurred (eid){}'.format(err_id))
            return None

    # return order_id
    def insert_order(self, tg_name, exchange, ticker, price, volume, order_type, direction, source='', offset_flag=OffsetFlag.NOT_AVAILABLE, asset_type=AssetType.NOT_AVAILABLE):
        req = message_trade.ReqOrderInsert()
        req.tg_name = bytify(tg_name)
        req.exchange = exchange
        req.ticker = bytify(ticker)
        req.source = bytify(source)
        req.price = price
        req.volume = volume
        req.asset_type = asset_type
        req.order_type = order_type
        req.direction = direction
        req.offset_flag = offset_flag
        req.client_name = bytify(self.fist_name)
        req.parent_id = -1
        ret = self.req(self.trade_router, req, MsgType.REQ_ORDER_INSERT, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[order_insert] error occurred (eid){}'.format(err_id))
            return -1

    def insert_algo_order(self, tg_name, exchange, ticker, volume, direction, order_type, start_time, end_time, sec_interval, trading_style, asset_type=AssetType.NOT_AVAILABLE, **algo_args):
        req = message_trade.ReqOrderInsert()
        req.tg_name = bytify(tg_name)
        req.exchange = exchange
        req.ticker = bytify(ticker)
        req.price = 0
        req.volume = volume
        req.asset_type = asset_type
        req.order_type = order_type
        req.direction = direction
        req.offset_flag = OffsetFlag.NOT_AVAILABLE
        req.client_name = bytify(self.fist_name)
        req.parent_id = -1
        order_data = req.to_dict()
        # add necessary algo args
        order_data['start_nano'] = Timer.get_nano(start_time)
        order_data['end_nano'] = Timer.get_nano(end_time)
        order_data['sec_interval'] = sec_interval
        order_data['trading_style'] = trading_style
        # update extra algo args
        order_data.update(algo_args)
        # send order as json str
        order_str = json.dumps(order_data)
        ret = self.req(self.trade_router, order_str, MsgType.REQ_ORDER_INSERT_J, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[insert_twap_order] error occurred (eid){}'.format(err_id))
            return -1

    def insert_algo_order_twap(self, tg_name, exchange, ticker, volume, direction, start_time, end_time, sec_interval, trading_style=TradingStyle.NEUTRAL, asset_type=AssetType.NOT_AVAILABLE):
        return self.insert_algo_order(tg_name, exchange, ticker, volume, direction, OrderType.TWAP, start_time, end_time, sec_interval, trading_style, asset_type=asset_type)  # no extra args

    def insert_basket_order(self, basket_name, tg_name, basket_order, child_order_type, **algo_args):
        basket_order.basket_name = basket_name
        basket_order.tg_name = tg_name
        basket_order.order_id = -1
        basket_order.client_name = self.fist_name
        # set child order type
        # if child order type is algo type, then the algo args are necessary
        basket_order.set_child_order_type(child_order_type)
        basket_order.set_algo_info(**algo_args)
        # send out order as json str
        basket_order_str = json.dumps(basket_order.to_dict())
        ret = self.req(self.trade_router, basket_order_str, MsgType.REQ_ORDER_INSERT_BASKET, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[insert_basket_order] error occurred (eid){}'.format(err_id))
            return -1

    def insert_basket_order_w_twap(self, basket_name, tg_name, basket_order, start_time, end_time, sec_interval, trading_style):
        start_nano = Timer.get_nano(start_time)
        end_nano = Timer.get_nano(end_time)
        return self.insert_basket_order(basket_name, tg_name, basket_order, OrderType.TWAP, trading_style=trading_style, start_nano=start_nano, end_nano=end_nano, sec_interval=sec_interval)

    def cancel_order(self, order_id, tg_name):
        req = message_trade.ReqOrderCancel()
        req.order_id = order_id
        req.tg_name = bytify(tg_name)

        ret = self.req(self.trade_router, req, MsgType.REQ_ORDER_CANCEL, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[cancel_order] error occurred (eid){}'.format(err_id))
            return -1

    def req_position(self, tg_name):
        req = message_trade.ReqPosition()
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.trade_router, req, MsgType.REQ_POSITION, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[req_position] error occurred (eid){} (tg){}'.format(err_id, tg_name))
            return -1

    def req_account(self, tg_name):
        req = message_trade.ReqAccount()
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.trade_router, req, MsgType.REQ_ACCOUNT, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[req_account] error occurred (eid){} (tg){}'.format(err_id, tg_name))
            return -1

    def req_active_orders(self, tg_name):
        req = message_trade.ReqActiveOrders()
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.trade_router, req, MsgType.REQ_ACTIVE_ORDERS, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[req_active_orders] error occurred (eid){} (tg){}'.format(err_id, tg_name))
            return -1

    def req_cancel_active_orders(self, tg_name, req_active_orders_id=-1):
        req = message_trade.ReqCancelActiveOrders()
        req.req_active_orders_id = req_active_orders_id
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.trade_router, req, MsgType.REQ_CANCEL_ACTIVE_ORDERS, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[req_cancel_active_orders] error occurred (eid){} (tg){}'.format(err_id, tg_name))
            return -1

    def req_history_trades(self, tg_name):
        req = message_trade.ReqHistoryTrades()
        req.tg_name = bytify(tg_name)
        req.client_name = bytify(self.fist_name)
        ret = self.req(self.trade_router, req, MsgType.REQ_HISTORY_TRADES, 0)
        err_id = ret.get_err_id()
        if err_id == 0:
            return ret.get_req_id()
        else:
            self.logger.error('[req_hist_trades] error occurred (eid){} (tg){}'.format(err_id, tg_name))
            return -1

    # subscription
    def subscribe_snap(self, exchange, ticker):
        return self.subscribe(exchange, ticker, MsgType.MKT_SNAP)

    def subscribe_bar(self, exchange, ticker, bar_type=BarType.MIN_15):
        return self.subscribe(exchange, ticker, MsgType.MKT_BAR, bar_type=bar_type)

    def subscribe_index(self, exchange, ticker):
        return self.subscribe(exchange, ticker, MsgType.MKT_INDEX)

    def subscribe_order(self, exchange, ticker):
        return self.subscribe(exchange, ticker, MsgType.MKT_ORDER)

    def subscribe_trade(self, exchange, ticker):
        return self.subscribe(exchange, ticker, MsgType.MKT_TRADE)

    def subscribe(self, exchange, ticker, msg_type, bar_type=BarType.NOT_AVAILABLE):
        return self.subscribe_batch([exchange], [ticker], msg_type, bar_type)

    def subscribe_batch(self, exchanges, tickers, msg_type=MsgType.MKT_SNAP, bar_type=BarType.NOT_AVAILABLE):
        if not isinstance(tickers, list):
            tickers = [tickers]
        if not isinstance(exchanges, list):
            exchanges = [exchanges for i in range(0, len(tickers))]
        if len(exchanges) != len(tickers):
            self.logger.error('[subscribe] exchanges and tickers, size mismatch')
            return False
        ss = json.dumps([{'exchange': ExchangeID.read(exchanges[i]), 'ticker': tickers[i], 'msg_type': msg_type, 'bar_type': bar_type} for i in range(0, len(tickers))])
        rsp = self.req(self.market_router, ss, MsgType.MKT_SUBSCRIBE, 0)
        if rsp.get_err_id() != 0:
            self.logger.error('[subscribe] failed (err_id){} (msg){}'.format(rsp.get_err_id(), ss))
            return False
        else:
            self.logger.info('[subscribe] success')
            return True

    # to override
    # trade
    def on_rsp_order_insert(self, obj, frame_nano):
        pass

    def on_rsp_order_cancel(self, obj, frame_nano):
        pass

    def on_rtn_order(self, obj, frame_nano):
        pass

    def on_rtn_trade(self, obj, frame_nano):
        pass

    def on_rsp_position(self, obj, frame_nano):
        pass

    def on_rsp_account(self, obj, frame_nano):
        pass

    def on_rsp_active_orders(self, obj, frame_nano):
        pass

    def on_rsp_cancel_active_orders(self, obj, frame_nano):
        pass

    def on_rsp_history_trades(self, obj, frame_nano):
        pass

    # to override
    # market
    def on_mkt_snap(self, obj, msg_type, frame_nano):
        pass

    def on_mkt_bar(self, obj, msg_type, frame_nano):
        pass

    def on_mkt_vol(self, obj, msg_type, frame_nano):
        pass

    def on_mkt_index(self, obj, msg_type, frame_nano):
        pass

    def on_mkt_order(self, obj, msg_type, frame_nano):
        pass

    def on_mkt_trade(self, obj, msg_type, frame_nano):
        pass

    # to override
    # system status
    def on_gateway_connection_change(self, obj, frame_nano):
        pass

    def on_gateway_heart_beat(self, obj, frame_nano):
        pass

    ######################
    # internal functions #
    ######################

    def register_msg_callback(self, msg_type, callback):
        # callback should have the args list exactly matched (data: dict, msg_type: int, frame_nano: int)
        if msg_type in self._msg_callbacks:
            self.logger.warn('[reg_msg_callback] replacing callback (msg_type){}/{}'.format(msg_type, MsgType.read(msg_type)))
        self._msg_callbacks[msg_type] = callback

    def on_pub_frame(self, f):
        msg_type = f.get_msg_type()
        frame_nano = f.get_nano()

        msg_callback = self._msg_callbacks.get(msg_type)
        if msg_callback is not None:
            data = json.loads(f.get_string())
            msg_callback(data, msg_type, frame_nano)

        elif MsgType.is_market_data_type(msg_type):
            if msg_type == MsgType.MKT_SNAP:
                snap_obj = f.get_obj(message_market.MktSnap)
                self.on_mkt_snap(snap_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_SNAP_PLUS:
                snap_obj = f.get_obj(message_market.MktSnapPlus)
                self.on_mkt_snap(snap_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_SNAP_FUT:
                snap_obj = f.get_obj(message_market.MktSnapFut)
                self.on_mkt_snap(snap_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_SNAP_OPT:
                snap_obj = f.get_obj(message_market.MktSnapOpt)
                self.on_mkt_snap(snap_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_SNAP_AGG:
                agg_d = json.loads(f.get_string())
                snap_obj = message_market.MktSnapAgg(agg_d)
                self.on_mkt_snap(snap_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_INDEX:
                idx_obj = f.get_obj(message_market.MktIndex)
                self.on_mkt_index(idx_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_ORDER:
                order_obj = f.get_obj(message_market.MktOrder)
                self.on_mkt_order(order_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_TRADE:
                trade_obj = f.get_obj(message_market.MktTrade)
                self.on_mkt_trade(trade_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_BAR:
                bar_obj = f.get_obj(message_market.MktBar)
                self.on_mkt_bar(bar_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_BAR_GEN:
                bar_obj = f.get_obj(message_market.MktBarGen)
                self.on_mkt_bar(bar_obj, msg_type, frame_nano)

            elif msg_type == MsgType.MKT_VOL:
                vol_obj = f.get_obj(message_market.MktVol)
                self.on_mkt_vol(vol_obj, msg_type, frame_nano)

        elif MsgType.is_trading_data_type(msg_type):
            if msg_type == MsgType.RSP_ORDER_INSERT:
                rsp_ord_obj = f.get_obj(message_trade.RspOrderInsert)
                self.on_rsp_order_insert(rsp_ord_obj, frame_nano)

            elif msg_type == MsgType.RSP_ORDER_CANCEL:
                rsp_cancel_obj = f.get_obj(message_trade.RspOrderCancel)
                self.on_rsp_order_cancel(rsp_cancel_obj, frame_nano)

            elif msg_type == MsgType.RTN_ORDER:
                ord_object = f.get_obj(message_trade.RtnOrder)
                self.on_rtn_order(ord_object, frame_nano)

            elif msg_type == MsgType.RTN_TRADE:
                trd_obj = f.get_obj(message_trade.RtnTrade)
                self.on_rtn_trade(trd_obj, frame_nano)

            elif msg_type == MsgType.RSP_POSITION:
                pos_d = json.loads(f.get_string())
                pos_obj = message_trade.RspPosition(pos_d)
                self.on_rsp_position(pos_obj, frame_nano)

            elif msg_type == MsgType.RSP_ACCOUNT:
                acc_obj = f.get_obj(message_trade.RspAccount)
                self.on_rsp_account(acc_obj, frame_nano)

            elif msg_type == MsgType.RSP_ACTIVE_ORDERS:
                ods_d = json.loads(f.get_string())
                ods_obj = message_trade.RspActiveOrders(ods_d)
                self.on_rsp_active_orders(ods_obj, frame_nano)

            elif msg_type == MsgType.RSP_CANCEL_ACTIVE_ORDERS:
                rsp_obj = f.get_obj(message_trade.RspCancelActiveOrders)
                self.on_rsp_cancel_active_orders(rsp_obj, frame_nano)

            elif msg_type == MsgType.RSP_HISTORY_TRADES:
                rsp_trades = json.loads(f.get_string())
                rsp_trades = message_trade.RspHistoryTrades(rsp_trades)
                self.on_rsp_history_trades(rsp_trades, frame_nano)

        elif MsgType.is_system_status_data_type(msg_type):
            if msg_type == MsgType.GTW_CONNECTION:
                gtw_con_obj = f.get_obj(message_common.GatewayConnectionStatus)
                self.on_gateway_connection_change(gtw_con_obj, frame_nano)

        elif msg_type == LinkerMsgType.FIST_HEART_BEAT:
            gtw_hb = f.get_obj(message_linker.MsgHeartBeat)
            self.on_gateway_heart_beat(gtw_hb, frame_nano)
