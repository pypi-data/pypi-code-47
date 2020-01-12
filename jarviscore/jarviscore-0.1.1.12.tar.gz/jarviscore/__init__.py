# -*- coding: utf-8 -*-

"""
Twitch IRC & API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Twitch IRC channels and 
partial coverage of the Twitch API.
:copyright: (c) 2016-2019 Cubbei
:license: Restricted, direct inquiries to Cubbei.
"""

__title__ = 'jarvis on twitch'
__author__ = 'cubbei'
__license__ = 'Restricted'
__copyright__ = 'Copyright 2016-2019 Cubbei'
__version__ = '0.3.0a'

from collections import namedtuple

from .client import Client
from .command import Command, CommandResponse
from .errors import *
from .helpers import Helpers
from .httpclient import HTTPClient, WebResponse
from .log import Log
from .message import *
from .model import Model
from .settings import Settings
from .socket import SendSocket, ReadSocket
from .user import User
from .commands import *







VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=3, micro=0, releaselevel='alpha', serial=0)