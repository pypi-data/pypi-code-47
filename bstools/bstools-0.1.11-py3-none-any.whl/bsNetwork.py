#! /usr/bin/env python3
#! coding='utf-8' 

import requests
import json

class requestMode(object):
    post = requests.post
    get = requests.get
    put = requests.put
    delete = requests.delete

def sendRequest(self, url, header, params = "", 
                content = "", requestMode = requestMode.post):
    try:
        response = requestMode(
            url=url,
            headers=header,
            params=params,
            data=json.dumps(content)
        )
        self.dPrint(url + response.content)
        return response.content
    
    except requests.exceptions.RequestException:
        print('HTTP Request failed')