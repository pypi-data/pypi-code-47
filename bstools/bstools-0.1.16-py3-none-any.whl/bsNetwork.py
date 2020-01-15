#! /usr/bin/env python3
#! coding='utf-8' 

import requests
import json
from .bsPrint import dPrint
from enum import Enum

class requestMode(Enum):
    post = requests.post
    get = requests.get
    put = requests.put
    delete = requests.delete

def sendRequest(url, header, params = "", content = "", 
                rMode = requestMode.post, debugMode = dPrint(True)):
    try:
        response = rMode(
            url=url,
            headers=header,
            params=params,
            data=json.dumps(content)
        )
        debugMode.debug(url + "-----" +str(response.content))
        return response.content
    
    except requests.exceptions.RequestException:
        print('HTTP Request failed')