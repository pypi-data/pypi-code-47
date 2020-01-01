import logging
try:
    import flask,jinja2
    from .web import *
    from . import bps
except:
    logging.warning('web module requires flask, jinja2 ,which are not found.')
# from . import bluepoints,examples