# -*- coding: utf-8 -*-
from pkg_resources import DistributionNotFound, get_distribution

from .servo import Servo
from .servoDevice import ServoDevice

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
