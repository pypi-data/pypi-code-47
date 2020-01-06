# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

# set version
version = (0, 1, 0)

import json
from . import config
from . import api_lego as lego
from . import api_users as users
from .objects import Element, Color, Part, Collection, Theme, Category
from .rebrick import Rebrick


def init(*args):
    """
    Sets API_KEY and USER_TOKEN to be used automatically as defaults for the
    whole rebrick module. The API KEY must be available for all the rebrick
    functions to work. The USER TOKEN is needed for user-specific functions.
    
    In case a single argument is provided it is considered as API_KEY. If two
    arguments are provided they are considered as API_KEY and USER_TOKEN.
    Finally, if three arguments are provided they are considered as API_KEY,
    username and password to retrieve USER_TOKEN from the server.
    """
    
    # show help
    if not args:
        message = "Missing arguments: (API_KEY) or (API_KEY, USER_TOKEN) or (API_KEY, username, password)."
        raise ValueError(message)
    
    # set API KEY
    if len(args) == 1:
        config.API_KEY = str(args[0])
    
    # set API KEY and USER TOKEN
    elif len(args) == 2:
        config.API_KEY = str(args[0])
        config.USER_TOKEN = str(args[1])
    
    # set API KEY and retrieve USER TOKEN
    elif len(args) == 3:
        config.API_KEY = str(args[0])
        response = users.get_token(args[1], args[2])
        data = json.loads(response.read())
        config.USER_TOKEN = data.get('user_token', None)
