# -*- coding:utf-8 -*-
# author:Pntehan


from Zpider.zpider import zpider

def get(url, user_agent=False, proxy_ip=False, timeout=3, retry=3, cookies=False):
    new = zpider()
    return new.get(url, user_agent, proxy_ip, timeout, retry, cookies)

def post(url, data=None, user_agent=False, proxy_ip=False, timeout=3, retry=3, cookies=False):
    new = zpider()
    return new.post(url, data, user_agent, proxy_ip, timeout, retry, cookies)


