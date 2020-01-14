# coding: utf-8
'''
This file is part of the `cn_workday` Python package.
It provides the function `is_workday(dt)` which takes a `datetime` object,
and return True if the date it represents is considered a workday in PRC.
'''
from datetime import datetime
import io
import os.path

import csv
import enum
import pytz

DATA_FIELDS = [
    'name', 'date', 'description', 'observed', 'isholiday', 'isworkday',
]

CACHE = {}
TZ = pytz.timezone('Asia/Shanghai')


@enum.unique
class DAY_TYPES(enum.Enum):
    '''
    Day types enum. Members:
      - WORKDAY
      - WEEKEND
      - HOLIDAY
      - HOLIDAY_TRADEOFF
    '''
    WORKDAY = 0
    WEEKEND = 1
    HOLIDAY = 2
    HOLIDAY_TRADEOFF = 3


def cleanup_dict(d):
    '''Strip key and value for dict `d`'''
    return {
        (k.strip() if isinstance(k, str) else k): (v.strip() if isinstance(v, str) else v)
        for k, v in d.items()
    }


def decomment(rf):
    '''Remove comment content from CSV line.
    `rf` should be a file opened for reading.
    '''
    for line in rf:
        content = line.split('#')[0].strip()
        if content:
            yield content


def load_data(year):
    '''Load data into memory cache'''
    year = str(year)
    if year in CACHE:
        return True

    data_file = os.path.join(
        os.path.dirname(__file__), 'data', '{}.csv'.format(year),
    )
    if not os.path.isfile(data_file):
        return False

    CACHE[year] = {}
    with io.open(data_file, encoding='utf-8') as rf:
        # Detect CSV header line
        has_header = csv.Sniffer().has_header(rf.read(1024))
        rf.seek(0)  # Reset file offset

        reader = csv.DictReader(decomment(rf), DATA_FIELDS)
        if has_header:
            next(reader)

        for data_line in reader:
            day = cleanup_dict(data_line)

            # Convert to `int` type so we don't need to parse it afterwards
            dt = datetime.strptime(day['date'], '%Y-%m-%d')
            day.update({
                'year': dt.year,
                'month': dt.month,
                'day': dt.day,
                'isholiday': bool(int(day['isholiday'])),
                'isworkday': bool(int(day['isworkday'])),
            })
            CACHE[year][day.pop('date')] = day

    return True


def get_day_type(dt):
    '''Get type of given datetime object'''
    # Naive time => localized time
    if dt.tzinfo is None:
        dt = TZ.localize(dt)
    else:
        # Normalize timezone to GMT+8
        dt = TZ.normalize(dt)

    year = str(dt.year)
    load_data(year)

    matched_days = list(filter(
        lambda x: all([
            x['year'] == dt.year,
            x['month'] == dt.month,
            x['day'] == dt.day,
        ]),
        CACHE[year].values(),
    ))

    if list(filter(lambda x: x['isholiday'] is True, matched_days)):
        return DAY_TYPES.HOLIDAY

    if list(filter(lambda x: x['isworkday'] is True, matched_days)):
        return DAY_TYPES.HOLIDAY_TRADEOFF

    if dt.weekday() > 4:
        return DAY_TYPES.WEEKEND

    return DAY_TYPES.WORKDAY


def is_workday(dt):
    '''Detect if the day given datetime object represents is a workday in PRC.
    These are not workdays:
      - Weekends;
      - Holidays;
    If given date is defined as a holiday tradeoff, it is indeed a workday.
    '''
    day_type = get_day_type(dt)
    return day_type is DAY_TYPES.WORKDAY \
        or day_type is DAY_TYPES.HOLIDAY_TRADEOFF

