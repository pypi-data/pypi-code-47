#! /usr/bin/env python3
#! coding='utf-8' 

import requests
import json
from enum import Enum

class requestMode(Enum):
    post = requests.post
    get = requests.get
    put = requests.put
    delete = requests.delete

def sendRequest(url, header, params = "", content = "", 
                rMode = requestMode.post):
    status = True
    try:
        response = rMode(
            url=url,
            headers=header,
            params=params,
            data=json.dumps(content)
        )
        if response.status_code < 300 and response.status_code >= 200:
            status = True
        else:
            status = False
        content = response.content
    
    except requests.exceptions.RequestException:
        status = False
        content = '%s Request failed'%url
    
    return(status, content)