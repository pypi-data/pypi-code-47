# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/10 18:22                       *
# @Author  : Bob He                                |
# @FileName: get_ip.py                              *
# @Software: PyCharm                               |
# @Project : ddcmaker                                *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+

# !/usr/bin/env python
# encoding: utf-8
# description: get local ip address

import time  # line:1
import requests  # line:2
import json  # line:3
from ddcmaker.linux.armv7l import constant, getip_address as gp  # line:4


def poststatus():  # line:7
    OOO0O0O0OO00OOOOO = constant.url0 + constant.type_link + constant.maker_dict[2]  # line:8
    OO000O00O0000O000 = gp.get_mac_address()  # line:9
    while True:  # line:10
        O00OO0OO0OO0O00O0 = json.dumps({'macAddr': OO000O00O0000O000, 'onlineStatus': 1})  # line:11
        OO0OO000O0OOOOOO0 = {'content-type': 'application/json;charset=UTF-8'}  # line:12
        try:  # line:13
            O0OOOO0OOOOOO0O00 = requests.post(OOO0O0O0OO00OOOOO, O00OO0OO0OO0O00O0,
                                              headers=OO0OO000O0OOOOOO0)  # line:14
            print(O0OOOO0OOOOOO0O00)  # line:15
        except:  # line:16
            time.sleep(3)  # line:17
            return poststatus  # line:18
        time.sleep(10)  # line:19


def poststatus_online():  # line:22
    OOOO0O0OOOO0O0000 = constant.url + constant.type_link + constant.maker_dict[2]  # line:23
    O0O00OOO0O000OOOO = gp.get_mac_address()  # line:24
    while True:  # line:25
        OOOOOO000O0O0O0OO = json.dumps({'macAddr': O0O00OOO0O000OOOO, 'onlineStatus': 1})  # line:26
        OOOOOO00O0O0OO0OO = {'content-type': 'application/json;charset=UTF-8'}  # line:27
        try:  # line:28
            OOO0OO000O00O0O0O = requests.post(OOOO0O0OOOO0O0000, OOOOOO000O0O0O0OO,
                                              headers=OOOOOO00O0O0OO0OO)  # line:29
            print(OOO0OO000O00O0O0O)  # line:30
        except:  # line:31
            time.sleep(3)  # line:32
            return poststatus_online  # line:33
        time.sleep(10)  # line:34
