__author__ = "Unai Saralegui"
__copyright__ = "Copyright 2019, Unai Saralegui"
__credits__ = ["Unai Saralegui", "Josu Gomez"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Unai Saralegui"
__email__ = "usaralegui@gmail.com"
__status__ = "Development"

import requests


class RedCapError(requests.RequestException):
    """Default Error Type for the redcapy package"""
    pass
