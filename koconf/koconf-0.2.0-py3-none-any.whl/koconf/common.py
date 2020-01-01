import requests

from datetime import datetime as dt
from humanfriendly import format_timespan

date_format = '%Y-%m-%d %H:%M'


def now():
    return dt.now().strftime(date_format)


def difftime(before, after):
    diff = dt.strptime(after, date_format) - dt.strptime(before, date_format)
    return format_timespan(diff.total_seconds())


def request():
    url = 'https://raw.githubusercontent.com/lntuition/koconf/master/data/conference.json'

    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'

    return response.json()
