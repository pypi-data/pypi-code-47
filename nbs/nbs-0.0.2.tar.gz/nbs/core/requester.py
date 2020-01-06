#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : requester.py
# Author            : JCHRYS <jchrys@me.com>
# Date              : 04.01.2020
# Last Modified Date: 04.01.2020
# Last Modified By  : JCHRYS <jchrys@me.com>
import requests

class Singletone():
    __instance = None
    
    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


class BaseClass():

    def __init__(self, default_headers, default_params, default_url):
        self.headers = default_headers
        self.params = default_params
        self.url = default_url

    
    def search(self, string):
        if string is None or string == '':
            raise Exception("keyword is empty")
            return None # ERROR NO SEARCH TEXT
        context = {
                "query": string
                }
        return requests.get(self.url, headers = self.headers, params = dict(self.params, **context))

    def search_title(self, string):
        pass

    def search_author(self, string):
        pass

    def search_text(self, string):
        pass

class Request(BaseClass, Singletone):
    pass


if __name__ == '__main__':
    from NBCrawler import settings
    requester = Request(settings.default_headers, 
                      settings.default_params, 
                      settings.default_url
                      )
    res = requester.search("자바")
    print(res.content.decode('utf-8'))
