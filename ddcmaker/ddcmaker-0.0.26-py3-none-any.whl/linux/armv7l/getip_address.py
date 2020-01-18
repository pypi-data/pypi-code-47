# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/12 10:31                      *
# @Author  : Bob He                                |
# @FileName: getip_address.py                      *
# @Software: PyCharm                               |
# @Project : ddcmaker                              *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
import socket  # line:1
import requests  # line:2
import re  # line:3
import time  # line:4
import json  # line:5


def get_mac_address():  # line:7
    import uuid  # line:8
    O000O00O00OOO00O0 = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()  # line:9
    return '%s:%s:%s:%s:%s:%s' % (
    O000O00O00OOO00O0[0:2], O000O00O00OOO00O0[2:4], O000O00O00OOO00O0[4:6], O000O00O00OOO00O0[6:8],
    O000O00O00OOO00O0[8:10], O000O00O00OOO00O0[10:])  # line:10


def get_ip():  # line:13
    try:  # line:14
        O00OOOOOOOO0O0OOO = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # line:15
        try:  # line:16
            O00OOOOOOOO0O0OOO.connect(('www.baidu.com', 0))  # line:17
        except:  # line:18
            print("无法连接到外网！")  # line:19
        OOO00O000OOOO0000 = O00OOOOOOOO0O0OOO.getsockname()[0]  # line:20
    except:  # line:21
        OOO00O000OOOO0000 = "x.x.x.x"  # line:22
    finally:  # line:23
        O00OOOOOOOO0O0OOO.close()  # line:24
    return OOO00O000OOOO0000  # line:25


def get_extranetip():  # line:28
    try:  # line:35
        O0000O0OO0OO0O0O0 = requests.get("http://members.3322.org/dyndns/getip", timeout=3).text.strip()  # line:36
        if len(str(O0000O0OO0OO0O0O0)) > 7:  # line:38
            return O0000O0OO0OO0O0O0  # line:39
    except Exception as OO0O0000O000OOO00:  # line:40
        O0O00O00O00OO0OO0 = requests.get("http://txt.go.sohu.com/ip/soip", timeout=2).text  # line:41
        O0000O0OO0OO0O0O0 = re.findall(r'\d+.\d+.\d+.\d+', O0O00O00O00OO0OO0)[0]  # line:42
        if len(str(O0000O0OO0OO0O0O0)) > 7:  # line:43
            return O0000O0OO0OO0O0O0  # line:44
        print("暂时无法发出外网请求！")  # line:45


def getipadress():  # line:48
    OO000O00O0OO0000O = get_ip()  # line:49
    O0OOOO000O000OOOO = get_mac_address()  # line:50
    OO0000O000OO0OOO0 = get_extranetip()  # line:51
    return OO000O00O0OO0000O, O0OOOO000O000OOOO, OO0000O000OO0OOO0  # line:52


def postaddress(O0OO0OOO0OO0OOO00, O00OO000OOO000OO0, OOO0O0OO00O000000, O0OOOOO0OO0OO0000,
                OO0000OOO00000000):  # line:55
    OO0OO00O0O00OO00O = json.dumps({'inIp': O0OO0OOO0OO0OOO00, 'macAddr': O00OO000OOO000OO0, 'exIp': OOO0O0OO00O000000,
                                    'type': OO0000OOO00000000})  # line:57
    OOO000OOOOO00O0OO = {'content-type': 'application/json;charset=UTF-8'}  # line:58
    print(OO0OO00O0O00OO00O)  # line:59
    OO0OOOOO0OOO0O000 = requests.post(O0OOOOO0OO0OO0000, OO0OO00O0O00OO00O, headers=OOO000OOOOO00O0OO)  # line:60
    print(OO0OOOOO0OOO0O000)  # line:61
    if OO0OOOOO0OOO0O000.status_code == 200:  # line:62
        return O0OO0OOO0OO0OOO00  # line:63
    elif OO0OOOOO0OOO0O000.status_code == 504:  # line:64
        print("当前服务器接口不通")  # line:65
        time.sleep(15)  # line:66
    else:  # line:67
        time.sleep(15)  # line:68
        return postaddress(O0OO0OOO0OO0OOO00, O00OO000OOO000OO0, OOO0O0OO00O000000, O0OOOOO0OO0OO0000,
                           OO0000OOO00000000)  # line:69
