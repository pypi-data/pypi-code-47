# from shinehope.utils.definitions import ROOT_DIR
from shinehope.utils.definitions import EAACCESS_DIR
from shinehope.eaaccess.marketdata import OrderData, TradeData, TradeType
import  os
import sqlite3
from datetime import datetime
import json

class   DBAccess(object):
    tradeDBFile = None
    
    def __init__(self):
        super().__init__()

    ## 2019.11.30 返回值改為表示原 db file 是否存在
    # def initTradeDB(self, accountID, reinit=False) -> str:
    def initTradeDB(self, accountID, reinit=False) -> bool:
        """
            :return 2019.11.30 返回值改為表示原 db file 是否存在        
        """
        isExisted = True

        dbDir = os.path.join(EAACCESS_DIR, 'files')
        if not os.path.exists(dbDir):
            os.makedirs(dbDir)

        # accountID = configs['accountID']
        dbFile = os.path.join(EAACCESS_DIR, 'files', f"eaaccess_{accountID}.db")
        if reinit:
            if os.path.exists(dbFile):
                os.unlink(dbFile)

        if not os.path.exists(dbFile):
            isExisted = False

            conn = sqlite3.connect(dbFile)
            cursor = conn.cursor()
    #         sql = ('CREATE TABLE order'
    # '(id INT PRIMARY KEY NOT NULL,'
    # 'order_id TEXT NOT NULL,'
    # 'timestamp INT NOT NULL,'
    # 'remaining REAL);')
    #         c.execute(sql)
            cursor.execute('''CREATE TABLE ea_order(
sid INTEGER PRIMARY KEY AUTOINCREMENT,
order_id char(30) NOT NULL,
timestamp int NOT NULL,
status char(12) NOT NULL,
symbol char(12) NOT NULL,
type   char(12) NOT NULL,
side    char(12) NOT NULL,
price   decimal(16,8) NOT NULL,
amount  decimal(14,6) NOT NULL,
filled  decimal(14,6) NOT NULL,
remaining decimal(14,6) NOT NULL,
trans_dtime TEXT);''')
            conn.commit()
            print("Table ea_order created successfully")

            sql = ('CREATE UNIQUE INDEX if not exists uidx_ea_order on ea_order(order_id)')
            cursor.execute(sql)
            conn.commit()

            cursor.execute('''CREATE TABLE ea_trade(
sid INTEGER PRIMARY KEY AUTOINCREMENT,
trade_id char(30) NOT NULL,
timestamp int NOT NULL,
symbol char(12) NOT NULL,
order_id char(30)  NOT NULL,
type   char(12) NOT NULL,
side    char(12) NOT NULL,
taker_or_maker char(12) NOT NULL,
price   decimal(16,8) NOT NULL,
amount  decimal(14,6) NOT NULL,
cost    decimal(16,8) NOT NULL,
fee     varchar(128),
trans_dtime TEXT
);''')
            conn.commit()
            print("Table ea_trade created successfully")

            sql = ('CREATE UNIQUE INDEX if not exists uidx_ea_trade on ea_trade(trade_id)')
            cursor.execute(sql)
            conn.commit()

            cursor.execute('''CREATE TABLE acc_balance(
sid INTEGER PRIMARY KEY AUTOINCREMENT,
asset  char(6) NOT NULL,
free   decimal(16,8) NOT NULL,
used   decimal(16,8) NOT NULL,
total  decimal(16,8) NOT NULL,
trans_dtime TEXT
);''')
            conn.commit()
            print("Table acc_balance created successfully")

            sql = ('CREATE UNIQUE INDEX if not exists uidx_acc_balance on acc_balance(asset)')
            cursor.execute(sql)
            conn.commit()

            cursor.close()
            conn.close()

        self.tradeDBFile = dbFile
        # return dbFile
        return isExisted

    def initHistDB(self, exchange, symbol, reinit=False) -> str:
        dbDir = os.path.join(EAACCESS_DIR, 'history')
        if not os.path.exists(dbDir):
            os.makedirs(dbDir)

        # accountID = configs['accountID']
        dbFile = os.path.join(EAACCESS_DIR, 'history', f"{exchange}_{symbol}.db")
        if reinit:
            if os.path.exists(dbFile):
                os.unlink(dbFile)

        conn = sqlite3.connect(dbFile)
        cursor = conn.cursor()
        sql = (f'CREATE TABLE if not exists candles_{symbol}(id INTEGER PRIMARY KEY AUTOINCREMENT, ' 
                'start INTEGER NOT NULL,'
                'open REAL NOT NULL,'
                'high REAL NOT NULL,'
                'low REAL NOT NULL,'
                'close REAL NOT NULL,'
                'vwp REAL,'
                'volume REAL NOT NULL,'
                'trades INTEGER, '
                'trans_dtime TEXT);'
        )
        cursor.execute(sql)      
        conn.commit()
        print(f"Table candles_{symbol} created successfully")

        sql = (f'CREATE UNIQUE INDEX if not exists uidx_{symbol}_start on candles_{symbol}(start)')
        cursor.execute(sql)
        conn.commit()
        
        sql = ('CREATE TABLE if not exists candles_sequence(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'symbol TEXT NOT NULL, '
            'seq_start INTEGER NOT NULL, '
            'seq_end INTEGER NOT NULL, '
            'trans_dtime TEXT);'
        )
        cursor.execute(sql)
        sql = ('CREATE UNIQUE INDEX if not exists uidx_candles_seq_symbol on candles_sequence(symbol, seq_start)')
        cursor.execute(sql)
        conn.commit()

        # conn.commit()
        # print("Table ea_trade created successfully")
        cursor.close()
        conn.close()

        return dbFile

    # def loadBalance(dbFileName, balance) -> bool:
    def loadBalance(self, balance) -> bool:
        isOK = False
        if balance:
            try:
                conn = sqlite3.connect(self.tradeDBFile)
                cursor = conn.cursor()
                for idx, bal in enumerate(balance, start=0):
                    asset = bal['asset'].strip()
                    free = bal['amount']
                    used = 0.0
                    total = free + used
                    sql = ("insert into acc_balance(asset, free, used, total, trans_dtime) values("
                        f"'{asset}', {free}, {used}, {total}, datetime('now', 'localtime'))")
                    cursor.execute(sql)
                conn.commit()
                isOK = True
            except:
                conn.rollback()
                raise
            finally:
                cursor.close()
                conn.close()

        return isOK    

    # def fetchBalance(dbFileName) -> {}:
    def fetchBalance(self) -> {}:
        balance = {}

        if self.tradeDBFile:
            try:
                conn = sqlite3.connect(self.tradeDBFile)
                cursor = conn.cursor()
                sql = "select asset, free, used, total from acc_balance"
                cursor.execute(sql)
                rows = cursor.fetchall()
                free = {}
                used = {}
                total = {}
                for row in rows:
                    element = {}
                    asset = row[0]
                    element['free'] = round(row[1], 8)
                    free[asset]= round(row[1], 8)
                    element['used'] = round(row[2], 8)
                    used[asset] = round(row[2], 8)
                    element['total'] = round(row[3], 8)
                    total[asset] = round(row[3], 8)
                    balance[asset] = element
                balance['free'] = free
                balance['used'] = used
                balance['total'] = total
            finally:
                cursor.close()
                conn.close()
        
        return balance

    def orderNew(self, order:OrderData, fee={}) -> bool:
        isOK = False
        if not fee:
            return isOK

        if order:
            try:
                conn = sqlite3.connect(self.tradeDBFile)
                cursor = conn.cursor()
                sql = ("INSERT INTO ea_order(order_id, timestamp, status, symbol, type, side, price, amount, "
                    f"filled, remaining, trans_dtime) values('{order.order_id}', {order.timestamp}, '{order.status}', "
                    f"'{order.symbol}', '{order.order_type}', '{order.side}', {order.price}, {order.amount}, {order.filled}, "
                    f"{order.remaining}, datetime('now', 'localtime'))")
                cursor.execute(sql)

                ## update balance
                # buy: 記錄 quota currency 的 used ((by cost))
                # sell: 記錄 base currency 的 used ((by amount))
                pos = order.symbol.find("/")
                asset = None
                if order.side == "buy":
                    asset = order.symbol[pos + 1:]
                    sql = f"select free, used, total from acc_balance where asset = '{asset}'"                    
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    balFree = row[0]
                    balUsed = row[1]
                    cost = round(order.amount * order.price, 8)
                    if order.order_type == TradeType.TYPE_MARKET.value:
                        feeRate = fee['taker']
                    else:
                        feeRate = fee['maker']                        
                    feeCost = round(cost * feeRate, 8)
                    balFree = round(balFree - cost - feeCost, 8)
                    balUsed = round(balUsed + cost + feeCost, 8)
                    balTotal = round(balFree + balUsed, 8)
                else:
                    asset = order.symbol[:pos]
                    sql = f"select free, used, total from acc_balance where asset = '{asset}'"                    
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    balFree = row[0]
                    balUsed = row[1]
                    balFree = round(balFree - order.amount, 8)
                    balUsed = round(balUsed + order.amount, 8)
                    balTotal = round(balFree + balUsed, 8)

                updSql = (f"UPDATE acc_balance set free = {balFree}, used = {balUsed}, total = {balTotal} WHERE "
                    f"asset = '{asset}'")
                cursor.execute(updSql)

                conn.commit()
                isOK = True
            except:                 ## 發生無法 insert 時也不發出 exception, 只 return False
                isOK = False
            finally:
                cursor.close()
                conn.close()

        return isOK    

    def orderFetch(self, orderID:str) -> OrderData:        
        order: OrderData = None
        if orderID:
            try:
                conn = sqlite3.connect(self.tradeDBFile)
                cursor = conn.cursor()
                sql = ("select order_id, timestamp, status, symbol, type, side, price, amount, "
                    f"filled, remaining from ea_order WHERE order_id = '{orderID}'")
                cursor.execute(sql)
                row = cursor.fetchone()
                order = OrderData()
                order.order_id = row[0]
                order.timestamp = row[1]        
                order.status = row[2]
                order.symbol = row[3]
                order.order_type = row[4]
                order.side = row[5]
                order.price = round(row[6], 8)
                order.amount = round(row[7], 8)
                order.filled = round(row[8], 8)
                order.remaining = round(row[9], 8)
            finally:
                cursor.close()
                conn.close()

        return order

    def orderFilled(self, order:OrderData, fee={}, partialVol:float=None) -> bool:
        isOK = False

        if not order:
            return isOK
        
        if not fee:
            return isOK

        if partialVol is not None:
            if partialVol > order.remaining:
                raise ValueError("has insufficient order.remaining !!!")

        try:
            conn = sqlite3.connect(self.tradeDBFile)
            cursor = conn.cursor()

            # newTrade = TradeData()
            dtNow = datetime.now()
            tstamp = dtNow.timestamp()
            trade_id = str(tstamp)
            # timestamp = int(tstamp * 1000)       # timestamp 不可使用 記錄當時的時間... 否則 backtest 時, 時間就出問題了
            timestamp = order.timestamp
            symbol = order.symbol
            order_id = order.order_id
            trade_type = order.order_type          # ???
            side = order.side                      # ???

            price = order.price                    # ???

            if partialVol is None or partialVol == order.remaining:
                # amount = order.amount
                amount = order.remaining
                delSql = f"delete from ea_order WHERE order_id = '{order.order_id}'"
                cursor.execute(delSql)
            else:
                remaining = order.remaining
                filled = order.filled
                amount = partialVol
                filled = round(filled + amount, 8)
                remaining = round(remaining - amount, 8)
                updSql = (f"update ea_order set filled = {filled}, remaining = {remaining}, "
                    f"trans_dtime = datetime('now', 'localtime') where order_id = '{order.order_id}'")
                cursor.execute(updSql)

            cost = round(price * amount, 8)
            if trade_type == TradeType.TYPE_MARKET.value:
                takerOrMaker = 'taker'                 # ???
                feeRate = fee['taker']
            else:
                takerOrMaker = 'maker'                 # ???
                feeRate = fee['maker']
            feeCost = round(cost * feeRate, 8)
            feeTaker = {
                'cost': feeCost,
                'currency': fee['currency'],
                'rate': feeRate
            }
            jsonFee = json.dumps(feeTaker)
            insSql = ("INSERT INTO ea_trade(trade_id, timestamp, symbol, order_id, type, side, taker_or_maker, "
                f"price, amount, cost, fee, trans_dtime) values('{trade_id}', {timestamp}, '{symbol}', '{order_id}', "
                f"'{trade_type}', '{side}', '{takerOrMaker}', {price}, {amount}, {cost}, '{jsonFee}', "
                f"datetime('now', 'localtime'))")
            cursor.execute(insSql)

            # delSql = f"delete from ea_order WHERE order_id = '{order.order_id}'"
            # cursor.execute(delSql)

            ## update balance
            # buy: 扣除 quota currency 的 used (by cost)
            # sell: 扣除 base currency 的 used (by amount)
            pos = symbol.find("/")
            asset = None
            if order.side == "buy":
                asset = symbol[pos + 1:]
                sql = f"select free, used, total from acc_balance where asset = '{asset}'"
                cursor.execute(sql)
                row = cursor.fetchone()
                balFree = row[0]
                balUsed = row[1]
                balUsed = round(balUsed - cost - feeCost, 8)
                balTotal = round(balFree + balUsed, 8)
            else:
                asset = symbol[:pos]
                sql = f"select free, used, total from acc_balance where asset = '{asset}'"
                cursor.execute(sql)
                row = cursor.fetchone()
                balFree = row[0]
                balUsed = row[1]
                balUsed = round(balUsed - amount, 8)
                balTotal = round(balFree + balUsed, 8)
            updSql = (f"UPDATE acc_balance set used = {balUsed}, total = {balTotal}, trans_dtime = datetime('now', 'localtime') "
                f"WHERE asset = '{asset}'")
            cursor.execute(updSql)

            ## update balance
            # buy: 加入 base currency 的 free (by amount)
            # sell: 加入 quota currency 的 free (by cost)
            if order.side == "buy":
                asset = symbol[:pos]
                sql = f"select free, used, total from acc_balance where asset = '{asset}'"
                cursor.execute(sql)
                row = cursor.fetchone()
                if row:
                    balFree = row[0]
                    balUsed = row[1]
                    balFree = round(balFree + amount, 8)
                    balTotal = round(balFree + balUsed, 8)
                    updSql = (f"UPDATE acc_balance set free = {balFree}, total = {balTotal}, "
                        f"trans_dtime = datetime('now', 'localtime') WHERE asset = '{asset}'")
                    cursor.execute(updSql)
                else:
                    balFree = 0.0
                    balUsed = 0.0
                    balFree = round(balFree + amount, 8)
                    balTotal = round(balFree + balUsed, 8)
                    insSql = (f"INSERT INTO acc_balance(asset, free, used, total, trans_dtime) values( "
                        f"'{asset}', {balFree}, {balUsed}, {balTotal}, datetime('now', 'localtime'))")
                    cursor.execute(insSql)
            else:
                asset = symbol[pos + 1:]
                sql = f"select free, used, total from acc_balance where asset = '{asset}'"
                cursor.execute(sql)
                row = cursor.fetchone()
                balFree = row[0]
                balUsed = row[1]
                balFree = round(balFree + cost - feeCost, 8)
                balTotal = round(balFree + balUsed, 8)

                updSql = (f"UPDATE acc_balance set free = {balFree}, total = {balTotal}, "
                        f"trans_dtime = datetime('now', 'localtime') WHERE asset = '{asset}'")
                cursor.execute(updSql)


            conn.commit()
        finally:
            cursor.close()
            conn.close()        

    def tradeSummary(self) -> {}:
        tradeSum = {}
        try:
            conn = sqlite3.connect(self.tradeDBFile)
            cursor = conn.cursor()
            sql = "select count(*), sum(amount) from ea_trade"
            cursor.execute(sql)
            row = cursor.fetchone()
            tradeSum['trades'] = row[0]
            tradeSum['amounts'] = round(row[1], 8)
        finally:
            cursor.close()
            conn.close()

        return tradeSum

    def fetchBackTestTrades(self) -> {}:
        trades = {}
        try:
            conn = sqlite3.connect(self.tradeDBFile)
            cursor = conn.cursor()
            sql = "select trade_id, timestamp, side, price from ea_trade order by trade_id"
            cursor.execute(sql)
            # row = cursor.fetchone()
            trades = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

        return trades

    def fetchMyTrades(self, since:int = None) -> []:
        trades = []
        try:
            conn = sqlite3.connect(self.tradeDBFile)
            cursor = conn.cursor()
            if since is None:
                sql = ("select trade_id, timestamp, symbol, order_id, type, side, taker_or_maker, price, "
                    "amount, cost, fee from ea_trade order by trade_id")
            else:
                sql = ("select trade_id, timestamp, symbol, order_id, type, side, taker_or_maker, price, "
                    f"amount, cost, fee from ea_trade where timestamp >= {since} order by trade_id")
            cursor.execute(sql)
            # row = cursor.fetchone()
            rows = cursor.fetchall()
            for trade in rows:
                item = {}
                item['id'] = trade[0]
                item['timestamp'] = trade[1]
                item['symbol'] = trade[2]
                item['order'] = trade[3]
                item['type'] = trade[4]
                item['side'] = trade[5]
                item['takerOrMaker'] = trade[6]
                item['price'] = round(trade[7], 8)
                item['amount'] = round(trade[8], 8)
                item['cost'] = round(trade[9], 8)
                jsonStr = trade[10]
                jsonFee = json.loads(jsonStr)
                item['fee'] = jsonFee
                trades.append(item)
        finally:
            cursor.close()
            conn.close()

        return trades

    def fetchPendingOrders(self, since:int = None) -> []:
        pendingOrders = []
        try:
            conn = sqlite3.connect(self.tradeDBFile)
            cursor = conn.cursor()
            if since is None:
                sql = ("select order_id, timestamp, status, symbol, type, side, price, amount, filled, remaining "
                    "from ea_order order by order_id")
            else:
                sql = ("select order_id, timestamp, status, symbol, type, side, price, amount, filled, remaining "
                    f"from ea_order where timestamp >= {since} order by order_id")
            cursor.execute(sql)
            # row = cursor.fetchone()
            rows = cursor.fetchall()
            for order in rows:
                item = {}
                item['id'] = order[0]
                item['timestamp'] = order[1]
                item['status'] = order[2]
                item['symbol'] = order[3]
                item['type'] = order[4]
                item['side'] = order[5]
                item['price'] = round(order[6], 8)
                item['amount'] = round(order[7], 8)
                item['filled'] = round(order[8], 8)
                item['remaining'] = round(order[9], 8)
                pendingOrders.append(item)
        finally:
            cursor.close()
            conn.close()

        return pendingOrders
