from datetime import datetime

import requests

from .base import make_block, route, ApiHandler
from ..lib.sparkline import text_sparkline
from ..lib.chartmoji import chartmoji


ERR_MISSING_APIKEY = '''
You are missing an API key for worldtradingdata.com.

## getting a key

You can get a free key at https://worldtradingdata.com

## setting the key

You can set it via command line or environment variable.

```
smugapi run --worldtradingdata APIKEY

SMUG_WORLDTRADINGDAT_KEY=APIKEY smugapi run
```
'''


@route(r'/sq/(?P<sym>\w+)/?$')
class StockGetQuotes(ApiHandler):

    def get(self, sym=None):
        apikey = self.application.configuration('worldtradingdata_key')
        print("APIKEY", apikey)
        if apikey is None:
            return self.api_fail(msg=ERR_MISSING_APIKEY, status=500)
        txt, blocks = sq(apikey, sym)
        self.api_ok(txt,blocks)


@route('/sq/?$')
class StockPostQuotes(ApiHandler):

    def post(self):
        sym = self.args.get('sym')
        apikey = self.application.configuration('worldtradingdata_key')
        if apikey is None:
            return self.api_fail(msg=ERR_MISSING_APIKEY, status=500)
        txt, blocks = sq(apikey, sym)
        self.api_ok(txt,blocks)

def _fetch_stock_data(apikey, sym):
    u = (
        'https://api.worldtradingdata.com/api/v1/stock?'
        'symbol={}&api_token={}'
        ).format(sym, apikey)
    return requests.get(u).json()


def sq(apikey, sym):
    res = _fetch_stock_data(apikey, sym)
    print(res)
    q = res['data'][0]
    sym = q['symbol']
    nm = q['name']
    op = q['price_open']
    hi = float(q['day_high'])
    lo = float(q['day_low'])
    prc = q['price']
    pct = q['change_pct']
    prev = q['close_yesterday']
    day = q['day_change']
    pe = q['pe']
    eps = q['eps']
    last_trade = q['last_trade_time'].split(' ')[1] + " ET"
    h = datetime.now().hour
    sline = text_sparkline(
        [int(float(i)*100) for i in [prev, op, (lo+hi)/2, prc]])
    cmoji = chartmoji([prev,op,(lo+hi)/2,prc])
    print("CHARTMOJI", cmoji)
    txt = (
        f"{sym} {prc} | recent {sline} | {nm} "
        f"| open {op} | range {lo} {hi} "
        f"|  prev cls {prev} | chg {day} ({pct}%)"
        )
    if prc > op: emoji = ":arrow_upper_right:"
    else: emoji = ":arrow_lower_right:"
    ftxt = (
        f"*{sym} {prc}* {cmoji} | {nm} "
        f"| open {op} | range {lo} {hi} "
        f"| prev cls {prev} | chg {day} ({pct}%)"
        )
    return txt, [make_block(ftxt)]

    # TOO SLOW FOR THE INTRADAY

    if h > 14: interval = '30'
    else: interval = '15'
    uu = (
    'https://intraday.worldtradingdata.com/api/v1/intraday?'
    'symbol={}&range=1&interval={}&api_token={}'
        ).format(sym, interval, apikey)
    res = requests.get(uu).json()
    items = sorted(res['intraday'].items(), key=lambda x:x[0])[:-9]
    prices = [ int(float(v['close']) * 10) for _,v in items ]
    print("PRICES", prices)
    sline = text_sparkline(prices)
    txt = f"{sym} {prc} - {nm} - lo {lo} - hi {hi} - pe {pe} - eps {eps} - today {sline}"
    if prc > op: emoji = ":chart_with_upwards_trend:"
    else: emoji = ":chart_with_downwards_trend:"
    ftxt = f"*{sym}* {prc} _(lo {lo} / hi {hi})_ {emoji}"
    blocks = [make_block(ftxt)]
    self.api_ok(txt, blocks)


