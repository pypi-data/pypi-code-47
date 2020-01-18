from enum import Enum
from algoz.errors import LocationError
import os

class Location(Enum):
        ALGORITHMIA_WEB   = 1
        ALGORITHMIA_LOCAL = 2
        ELSEWHERE = 99

def whereami():
    if os.environ.get("ALGORITHMIA_API_KEY") is None:
        return Location.ELSEWHERE
    else:
        return Location.ALGORITHMIA_WEB  # FIXME .. could be local

def assert_algorithmia_web(message="Cannot use outside of Algorithmia Marketplace"):
    if whereami()!=Location.ALGORITHMIA_WEB:
        raise LocationError(message)
