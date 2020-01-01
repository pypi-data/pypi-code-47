"""
Base package for implementation of POD platform APIs
"""
from .exceptions import *
from .base import PodBase


def calc_offset(page=1, size=50):
    if page > 1:
        return (page - 1) * size
    return 0
