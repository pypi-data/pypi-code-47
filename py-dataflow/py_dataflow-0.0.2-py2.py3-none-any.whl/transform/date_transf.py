import time

import pandas as pd
from dateutil import tz
from datetime import datetime

UTC_TIMEZONE = tz.tzutc()
LOCAL_TIMEZONE = tz.tzlocal()



def now(format="%Y-%m-%d %X"):
    return time.strftime(format)


def convert_utc_datetime(datetime):
	utc = datetime.replace(tzinfo=UTC_TIMEZONE)
	local_time = utc.astimezone(LOCAL_TIMEZONE)
	return pd.to_datetime(local_time)


def convert_local_datetime(datetime):
	local_time = datetime.replace(tzinfo=LOCAL_TIMEZONE)
	return pd.to_datetime(local_time)


def get_time_now():
	time_now = datetime.today().strftime('%H:%M:%S')
	return time_now


"""
###########################################################################
                          get period week, time
###########################################################################
"""

def is_hour_trade(self, stock={}):
    """
    :return: is hour to operation broker
    """
    stock = stock or self.stock_default
    if stock.get('production'):
        hour_init = settings.broker.get('HOUR_INIT_BROKER')
        hour_final = settings.broker.get('HOUR_FINAL_BROKER')
        useful_day = datetime.today().date().weekday()
        if useful_day not in [5, 6] and hour_init < time.strftime("%H:%M") < hour_final:
            return True
        else:
            return False
    else:
        return True

def num_week_year(year=None):
    """
    return => num week total in year bissexto
    """
    year = year or datetime.today().year
    if bool(year % 4):
        if bool(year % 100):
            if bool(year % 400):
                return 53
            else:
                return 52
        else:
            return 53
    else:
        return 52

def days_month(num_month=None, year=None):
    """
    :param num_week
    :param num_month:
    :param year:
    :return: days of the month
    """
    from datetime import date
    num_month = num_month or datetime.today().month
    year = year or datetime.today().year
    first_day_month = date(year, num_month, 1)
    dayBase = first_day_month.isocalendar()[2]
    sunday = 0
    if dayBase != sunday:
        first_day_month = dif_date(-dayBase, first_day_month)
    days_month = []
    for day in range(42):
        days_month.append(dif_date(day, first_day_month))
    return days_month

def days_week(num_week=None, year=None):
    """
    :param num_month:
    :param year:
    :return: days of the week
    """
    # import operator
    # import ipdb; ipdb.set_trace()
    days = []
    num_week = num_week or num_this_week()
    year = year or datetime.today().year
    if year < datetime.today().year:
        num_week = num_week - num_week_year(year) - num_this_week()
        qtd_day = (num_week * 7 - datetime.today().weekday())
    else:
        qtd_day = (num_week - num_this_week()) * 7 - datetime.today().weekday()

    day_init_week = dif_date(qtd_day)
    for num_day in range(7):
        day_week = dif_date(num_day, day_init_week)
        days.append(day_week)
    return days

def dif_date(day=None, date=None):
    """
    :param day:
    :param date:
    :return: diferents day in date
    """
    day = day or 0
    date = date or datetime.today().date()
    day = date.toordinal() + day
    return date.fromordinal(day)

def add_minute(minute= 1):
    """
    :param tm: with defaut secs=300 iguals 5 minute
    :param secs:
    :return
    """
    import datetime
    date_time = datetime.datetime.now()
    minute = date_time.minute + minute
    hour = date_time.hour
    if minute > 59:
        hour += 1
        minute = minute % 59
    fulldate = datetime.datetime(date_time.year, date_time.month, date_time.day, hour, minute)
    return fulldate

def num_this_week(day=None):
    """
    :return:
    """
    day = day or datetime.today()
    num_week = day.isocalendar()[1]
    return num_week

def get_week_before(num_week=None, year=None):
    """
    :param num_week:
    :return:
    """
    week_before = {}
    num_week = num_week or num_this_week()
    year = year or datetime.today().year
    num_before_week = None
    # first_day_week = days_week(num_week)[0]
    # num_before_week = dif_date(-1, first_day_week).isocalendar()[1]
    if num_week == 1:
        year = year -1
        num_before_week = num_week_year(year)
    else:
        num_before_week = num_week -1

    week_before['num_week'] = num_before_week
    week_before['year'] = year
    return week_before

"""
###########################################################################
                         munipulation date e hour
###########################################################################
"""
def name_day(date=None, time=None):
    """
    :param date:
    :return:
    """
    date = date or datetime.today().date()
    name_day = "%s %s %s" %(date.strftime("%A"), str(date.day), date.strftime("%B"))
    if time:
        name_day += ' as %02d:%02d' %(time.hour, time.minute)
    return name_day

def to_date(date=None):
    """
    :return: convert date
    """
    # import ipdb; ipdb.set_trace()
    if not date:
        return datetime.today().date()
    else:
        date = date.replace('/','-')
        year = date.split('-')[2]
        if len(year) == 2:
            date = date[:-2] + '20' + year
        date = datetime.strptime(date, '%d-%m-%Y').date()
        return date

def to_datetime(date=None, time=None):
    """
    :return: convert date_time
    """
    # import ipdb; ipdb.set_trace()
    import datetime
    date = date or datetime.datetime.today()
    if not time:
        date_time = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
    else:
        date = '%s-%s-%s' %(date.day, date.month, date.year)
        date_time = datetime.datetime.strptime(date + 'T' + time + 'Z', '%d-%m-%YT%H:%M:%SZ')
    return date_time