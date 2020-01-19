import datetime
now = datetime.datetime.now().strftime('%Y%m%d%H%M')

__version__ = '0.5.%s' % now
