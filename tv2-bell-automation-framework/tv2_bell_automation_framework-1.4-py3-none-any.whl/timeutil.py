'''
Module with time related functions
'''
from datetime import datetime

def date_diff_in_seconds(dt2, dt1):
    '''
    Calculate the difference between two timestamps in seconds.
    '''
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds + (timedelta.microseconds/1000000)
