# -*- coding:utf-8 -*-
class _dev_api:
    baidu = "baidu"
    huohu = "123"
    
    def __str__(self):
        return "qwe"

class _dev:
    api = _dev_api()
    username = "devname"
    

class _prod_api_func:
    fuction = "functionname"
    

class _prod_api:
    func = _prod_api_func()
    

class _prod:
    api = _prod_api()
    username = "prodname"
    

class _api:
    api = "apiname"
    

class _conf:
    dev = _dev()
    prod = _prod()
    api = _api()
    
