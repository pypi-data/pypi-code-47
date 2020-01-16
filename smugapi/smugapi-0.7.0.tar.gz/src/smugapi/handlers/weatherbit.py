
import json
import re
from datetime import datetime

import requests
import tornado
from tornado.web import HTTPError, authenticated
from tornado.util import ObjectDict


from .base import route, ApiHandler, make_block
from ..lib.sparkline import text_sparkline, png_sparkline, png_colors
from ..lib.chartmoji import chartmoji




ERR_MISSING_APIKEY = """
You are missing an API key for weatherbit.io.

This means you don't have one or have not set it while starting the smug api
server.

## getting a key

You can get a free key at https://www.weatherbit.io

## setting the key

When starting the server, you have two options.

```
smugapi run --weatherbit APIKEY
```

Or you can set it via an environment variable.

```
SMUG_WEATHERBIT_KEY=APIKEY
smugapi run
```
"""


ERR_MISSING_PARAMS = """
You are missing one of `city` or `postal` when calling the weather endpoint.

For `city`, values of `city,state` are valid:  `city=Austin,TX`.

For `postal, numeric values are valid: `postal=78614`.
"""

class MissingApiKey(Exception):
    pass


def _fetch_weather(api_key, wtype, loc, country="US"):
    baseurl = (
        "http://api.weatherbit.io/v2.0/current"
        "?key={}"
        "&units=I&country={}&" ).format(
                api_key,
                country)
    u = baseurl + "{}=".format(wtype) + loc
    res = requests.get(u).json()
    if 'data' in res and len(res['data']) > 0:
        return res['data'][0]
    return None


@route('/weather')
class WeatherHandler(ApiHandler):

    @property
    def api_key(self):
        apikey = self.application.configuration('weatherbit_key')
        if not apikey: raise MissingApiKey()
        return apikey

    def get(self):
        loc = self.get_argument('city', None)
        postal = self.get_argument('postal', None)
        self.do_weather(loc, postal)

    def post(self):
        if not self.args: self.api_fail("bogus request")
        loc = self.args.get('city')
        postal = self.args.get('postal')
        self.do_weather(loc, postal)

    def do_weather(self,loc,postal):
        try:
            if loc:
                dat = _fetch_weather(self.api_key, 'city', loc)
            elif postal:
                dat = self._fetch_weather(self.api_key,'postal_code', postal)
            else: return self.api_fail(msg=ERR_MISSING_PARAMS, status=400)
        except MissingApiKey:
            return self.api_fail(msg=ERR_MISSING_APIKEY, status=500)
        accimg="https://www.weatherbit.io/static/img/icons/{}.png"
        wmoji = ":wthr_{}:"
        if dat:
            snow = float(dat['snow'])
            w = "weather for {} {}: {}. {}F. feels like {}F. wind {}mph {}.  rain {}in".format(
                dat.get('city_name'), dat.get('state_code'),
                dat.get('weather',{}).get('description'),
                dat.get('temp'), dat.get('app_temp'), dat['wind_spd'], dat['wind_cdir'],
                dat['precip'])
            icon = wmoji.format(dat.get('weather',{}).get('icon'))
            rt = (
                "*weather for {}, {}* {}"
                " {}. {}F. "
                "\nfeels like {}F. wind {}mph {}. rain {}in"
            ).format(
                dat.get('city_name'), dat.get('state_code'), icon,
                dat.get('weather',{}).get('description'),
                dat.get('temp'), dat.get('app_temp'),
                dat['wind_spd'], dat['wind_cdir'], dat['precip']
            )
            if snow > 0:
                tsnow = " snow {}in".format(snow)
                w += tsnow
                rt += tsnow
            blocks = [make_block(text=rt)]
            self.api_ok(w, blocks)
        else:
            self.out("weather location not found")


def _fetch_forecast(api_key, wtype, loc, country="US"):
    baseurl = (
        "http://api.weatherbit.io/v2.0/forecast/daily"
        "?key={}"
        "&units=I&country={}&" ).format(api_key, country)
    u = baseurl + "{}=".format(wtype) + loc
    res = requests.get(u).json()
    if 'data' in res and len(res['data']) > 0:
        return res
    return None


@route('/forecast')
class ForecastHandler(ApiHandler):

    @property
    def api_key(self):
        apikey = self.application.configuration('weatherbit_key')
        if not apikey: raise MissingApiKey()
        return apikey

    def post(self):
        loc = self.args.get('city')
        postal = self.args.get('postal')
        self._do_weather(loc,postal)

    def get(self):
        loc = self.get_argument('city', None)
        postal = self.get_argument('postal', None)
        self._do_weather(loc,postal)

    def _do_weather(self, loc=None, postal=None):
        if loc:
            dat = _fetch_forecast(self.api_key, 'city', loc)
        elif postal:
            dat = _fetch_forecast(self.api_key, 'postal_code', postal)
        wthrmoji = ":wthr_{}:"
        if dat:
            today = dat['data'][0]
            tom = dat['data'][1]
            dayafter = dat['data'][2]
            day3 = dat['data'][3]
            day4 = dat['data'][4]
            txt = ''
            # header
            highs = []
            lows = []
            txt += "forecast for {} {}: ".format(
                    dat.get('city_name'),
                    dat.get('state_code') )
            rtxt = "forecast for *{}, {}*".format(
                    dat.get('city_name'),
                    dat.get('state_code') )
            txt += "today {} {}F/{}F. ".format(
                    today['weather']['description'],
                    today['low_temp'],
                    today['max_temp'] )
            highs.append(today['max_temp'])
            lows.append(today['low_temp'])
            rtxt += "\n{} today {} {}F/{}F.".format(
                    wthrmoji.format(today['weather']['icon']),
                    today['weather']['description'],
                    today['low_temp'],
                    today['max_temp'] )

            txt += "tomorrow {} {}F/{}F. ".format(
                    tom['weather']['description'],
                    tom['low_temp'],
                    tom['max_temp'] )
            rtxt += "\n{} tomorrow {} {}F/{}F. ".format(
                    wthrmoji.format(tom['weather']['icon']),
                    tom['weather']['description'],
                    tom['low_temp'],
                    tom['max_temp'] )
            highs.append(tom['max_temp'])
            lows.append(tom['low_temp'])

            txt += "then {} {}F/{}F. ".format(
                    dayafter['weather']['description'],
                    dayafter['low_temp'],
                    dayafter['max_temp'] )
            rtxt += "\n{} then {} {}F/{}F".format(
                    wthrmoji.format(tom['weather']['icon']),
                    dayafter['weather']['description'],
                    dayafter['low_temp'],
                    dayafter['max_temp'] )
            highs.append(dayafter['max_temp'])
            lows.append(dayafter['low_temp'])

            highs.append(day3['max_temp'])
            lows.append(day3['low_temp'])
            highs.append(day4['max_temp'])
            lows.append(day4['low_temp'])

            if self.application.configuration('enable_chartmoji'):
                trendmoji = (
                    "\n*5 day trend* overall " + chartmoji([
                        ((L+H)/2.0) for L,H in zip(lows,highs)] )
                    + " - lows  " + chartmoji(lows)
                    + " - highs " + chartmoji(highs)
                )
                rtxt += trendmoji

            mid_line = text_sparkline(
                [(int(float(i+j)/2)*100) for i,j in zip(lows,highs)])
            low_line = text_sparkline( [int(float(i)*100) for i in lows])
            high_line = text_sparkline( [int(float(i)*100) for i in highs])

            txt += f" 5d trend {mid_line} | lows {low_line} | highs {high_line}"
            self.api_ok(txt,[make_block(text=rtxt)])
        else:
            self.api_ok("weather location not found")


