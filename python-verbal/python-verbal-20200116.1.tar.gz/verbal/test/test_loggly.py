import logging

from testconfig import config

from ..loggly import LogglyHandler

def test_loggly():
    root = logging.getLogger(__name__)
    root.propagation = False
    root.setLevel(level=logging.DEBUG)
    root.addHandler(LogglyHandler(config['loggly_url'], level=logging.DEBUG))
    root.info("Hello From "+__file__)
    root.error("Big Problem!")

