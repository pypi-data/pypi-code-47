# -*- coding:utf-8 -*-
# author:Pntehan


import socks
from urllib.parse import urlparse
import Zpider.config as C
from lxml import etree

class zpider():
    """
    Zpider基本类，实现get，post以及其他方法
    """
    def __init__(self):
        pass

    def get(self, url, user_agent=False, proxy_ip=False, timeout=3, retry=3, cookies=False):
        # 通过socket请求网页
        if url == "why is Zpider":
            print("Because I love ZJ.")
            return
        # 分析url
        host, path = self.__parse_url(url)
        if path == "":
            path = "/"
        # 连接请求
        if isinstance(retry, int):
            r = 0
            while r < retry:
                flag, data = self.__connect_server(host, path, user_agent, proxy_ip, timeout, cookies)
                if flag:
                    break
                print(">>>服务器未响应，第{}次重试...".format(r+1))
                r += 1
            assert flag, data
        else:
            raise Exception("retry必须是整型或者浮点型...")
        # 请求成功，分析返回的数据
        html_headers = data.decode().split('\r\n\r\n')[0]
        html_data = data.decode().split('\r\n\r\n')[1]
        html_status = html_headers.split(" ")[1]
        return {"status": html_status, "header": html_headers, "text": html_data, "etree": etree.HTML(html_data), "content": data}

    def __connect_server(self, host, path, user_agent, proxy_ip, timeout, cookies, data=None, method="GET", up_type="form"):
        # 通过socket连接服务器
        client = socks.socksocket()
        # 设置报文
        if method == "POST":
            mess = "POST {} HTTP/1.1\r\nHost: {}\r\n".format(path, host)
            if up_type == "form":
                mess = mess + "Content-Type: application/x-www-form-urlencoded;charset=utf-8\r\n"
            elif up_type == "file":
                mess = mess + "Content-Type: multipart/form-data\r\n"
        else:
            mess = "GET {} HTTP/1.1\r\nHost: {}\r\n".format(path, host)
        # 检查是否有代理头
        if user_agent == "default":
            # 使用自带的代理头
            from random import randint
            user_agent = C.USER_AGENT[randint(0, len(C.USER_AGENT) - 1)]
            mess = mess + "User-Agent: {}\r\n".format(user_agent)
        # 检查是否含有cookies
        if cookies:
            if isinstance(cookies, dict):
                cookies_str = ""
                for key, value in cookies.items():
                    cookies_str = cookies_str + key + "=\"" + value + "\";"
            else:
                raise Exception("cookies的设置必须是字典类型...")
            mess = mess + "Cookie: {}\r\n".format(cookies_str)
        # 报文头部结束
        mess = mess + "Connection: close\r\n\r\n"
        # 判断是否有正文内容需要发送
        if data:
            if isinstance(data, dict):
                for key, value in data.items():
                    mess = mess + "{}={}&".format(key, value)
                mess = mess[:-1]
            else:
                raise Exception("正文的格式必须是字典类型...")
        # 设置代理IP
        if proxy_ip:
            # 使用自带的代理ip地址
            proxy_ip = C.IP[randint(0, len(C.IP) - 1)]
            client.setproxy(socks.HTTP, proxy_ip.split(":")[0], int(proxy_ip.split(":")[1]))
        # 设置超时时间
        if isinstance(timeout, int):
            client.settimeout(timeout)
        try:
            # 连接主机
            client.connect((host, 80))
            # 发送报文
            client.sendall(mess.encode())
            # 接受数据
            rec = b""
            while True:
                d = client.recv(1024)
                if d:
                    rec += d
                else:
                    break
            client.close()
            return True, rec
        except Exception as e:
            client.close()
            return False, Exception("连接错误，可能是连接超时，可能是主机拒绝您的请求，可以更换请求头或者代理ip重新尝试...")

    def post(self, url, data, user_agent=False, proxy_ip=False, timeout=3, retry=3, cookies=False):
        # 向网站发送post请求
        if url == "my name is ZJ":
            print("I love you.")
            return
        # 分析url
        host, path = self.__parse_url(url)
        if path == "":
            path = "/"
        # 连接请求
        if isinstance(retry, int):
            r = 0
            while r < retry:
                flag, rec = self.__connect_server(host, path, user_agent, proxy_ip, timeout, cookies, data, method="POST")
                if flag:
                    break
                print(">>>服务器未响应，第{}次重试...".format(r + 1))
                r += 1
            assert flag, rec
        else:
            raise Exception("retry必须是整型或者浮点型...")
        # 请求成功，分析返回的数据
        html_headers = rec.decode().split('\r\n\r\n')[0]
        html_data = rec.decode().split('\r\n\r\n')[1]
        html_status = html_headers.split(" ")[1]
        return {"status": html_status, "header": html_headers, "text": html_data, "etree": etree.HTML(html_data),
                "content": rec}

    def __parse_url(self, url):
        # 分析网页地址，返回域名和路径
        url = urlparse(url)
        return url.netloc, url.path

if __name__ == '__main__':
    z = zpider()
    info = z.get("https://www.baidu.com")
    print(info["status"])
    print(info["text"])
