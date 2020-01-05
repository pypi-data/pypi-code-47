import calendar
import datetime
import pandas as pd

from dateutil.relativedelta import relativedelta

def isocalendar(date):
    """
    Returns the isocalendar tuple
    https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar
    """
    try: 
        return date.isocalendar()
    except: 
        return datetime.date(date.year, date.month, date.day).isocalendar()

def weekday(date):
    """
    Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    https://docs.python.org/3/library/datetime.html#datetime.date.weekday
    """
    try: 
        return date.weekday()
    except: 
        return datetime.date(date.year, date.month, date.day).weekday()

def semester(date, *, base=1):
    """
    Returns the semester index of the given date
    """
    return (date.month - 1)//6 + base

def trimester(date, *, base=1):
    """
    returns the trimester index of the given date
    """
    return (date.month - 1)//4 + base

def quarter(date, *, base=1):
    """
    Returns the quarter index of the given date
    """
    return (date.month - 1)//3 + base

def sow(date, offset=0, weekday="SUN"):
    """
    returns the start of the week, i.e. the first date preceeding the given date 
    (not strict), whose weekday is equal to the the weekday argument, and 
    offset by a given number of weeks. Weekday must be one of MON...SUN.
    """
    weekday = ["MON","TUE","WED","THU","FRI","SAT","SUN"].index(weekday)
    return date + datetime.timedelta(offset * 7 - ((date.weekday() - weekday) % 7))

def eow(date, offset=0, weekday="SUN"):
    """
    returns the end of the week, i.e. the first date following the given date 
    (not strict), whose weekday is equal to the the weekday argument, and 
    offset by a given number of weeks. Weekday must be one of MON...SUN.
    """
    weekday = ["MON","TUE","WED","THU","FRI","SAT","SUN"].index(weekday)
    return date + datetime.timedelta((weekday - date.weekday()) % 7 + offset * 7)

def som(date, offset=0):
    """
    Returns start of month at a given offset for a given date
    """
    return date.replace(
        year=(date.year + (date.month + offset - 1) // 12),
        month=((date.month - 1 + 12 * date.year + offset) % 12 + 1), 
        day=1)

def eom(date, offset=0):
    """
    Returns the end of month at a given offset for a given date
    """
    if offset == 0:
        return date.replace(day=calendar.monthrange(year=date.year, month=date.month)[1])
    return eom(som(date, offset))

def soq(date, offset=0):
    """
    Returns the first date of the quarter
    1 January, 1 April, 1 July or 1 October
    """
    return (eoq(date, offset) - datetime.timedelta(2 * 31 + 1)).replace(day=1)

def eoq(date, offset=0):
    """
    Returns the end of the calendar quarter
    31 March, 30 June, 30 September or 31 December
    """
    return eom(date.replace(
        year=((date.month - 1) + date.year * 12 + 3 * offset) // 12, 
        month=3*(((date.month - 1)//3 + offset) % 4 + 1),
        day=1))

def eos(date, offset=0):
    """
    Returns the end of the calendar semester
    30 June or 31 December
    """
    return eom(date.replace(
        year=((date.month - 1) + date.year * 12 + 6 * offset) // 12, 
        month=6*(((date.month - 1)//6 + offset) % 2 + 1),
        day=1
    ))

def sos(date, offset=0):
    """
    Returns the first date of the calendar semester
    1 January or 1 July
    """ 
    return (eos(date, offset) - datetime.timedelta(5 * 31 + 1)).replace(day=1)

def soy(date, offset=0):
    """
    Returns the end of the year at a given offset
    """
    return type(date)(date.year + offset, 1, 1)

def eoy(date, offset=0):
    """
    Returns the end of the year at a given offset
    """
    return type(date)(date.year + offset, 12, 31)

def isleap(year):
    """
    Returns whether the given year is a leap-year
    """
    if isinstance(year, datetime.date):
        return isleap(year.year)
    return calendar.isleap(year)

def parse(date, disambiguate="EU"): 
    """
    parses a string into a datetime.date format
    """
    if isinstance(date, (datetime.date, datetime.datetime)): 
        return date
    if re.match("\d{4}-\d{2}-\d{2}", date):
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()
    if re.match("\d{2}/\d{2}/\d{2}", date):
        return datetime.datetime.strptime(date, "%d/%m/%y" if disambiguate == "EU" else "%m/%d/%y").date()
    if re.match("\d{2}/\d{2}/\d{4}", date):
        return datetime.datetime.strptime(date, "%d/%m/%Y" if disambiguate == "EU" else "%m/%d/%Y").date()
    raise ValueError("unrecognized date format")