#! /usr/bin/env python3
#! coding='utf-8' 

import requests
import json
from .bsPrint import dPrint

class requestMode(object):
    post = requests.post
    get = requests.get
    put = requests.put
    delete = requests.delete

def sendRequest(url, header, params = "", content = "", 
                requestMode = requestMode.post, debugMode = dPrint(True)):
    try:
        response = requestMode(
            url=url,
            headers=header,
            params=params,
            data=json.dumps(content)
        )
        debugMode.debug(url + response.content)
        return response.content
    
    except requests.exceptions.RequestException:
        print('HTTP Request failed')