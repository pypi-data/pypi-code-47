import requests
from bs4 import BeautifulSoup
import re

# To requests proxies to the website
def request_proxies():
    source = 'https://free-proxy-list.net/'
    headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive','Content-Encoding': 'gzip',
                'Content-Type': 'text/html; charset=utf-8'}

    free_proxy = requests.get(source, headers=headers).content
    soup = BeautifulSoup(free_proxy, 'lxml').find('table', {'id':"proxylisttable"})
    proxy_list = []
    for proxies in soup.find_all('tr'):
        if '</th>' not in str(proxies):
            drill = proxies.find_all('td')
            host = drill[0].text
            port = drill[1].text
            if re.match('Yes', drill[6].text, flags=re.I):
                protocol = 'https'
            else:
                protocol = 'http'
            proxy_list.append('''{}://{}:{}'''.format(protocol, host, port))
    return proxy_list

def get_one():
    return request_proxies()[0]

def get_many():
    return request_proxies()
