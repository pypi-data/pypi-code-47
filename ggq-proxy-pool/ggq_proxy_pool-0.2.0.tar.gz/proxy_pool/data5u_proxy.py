import json
import logging
from random import choice
from time import sleep
import requests
from proxy_pool import IpPool
import threading


class Data5UProxy(IpPool):
    def __init__(self, api_url):
        super().__init__(api_url)
        self.refresh_thread = GetIpThread(self.api_url, self.ip_pool, self.cond)

    def start(self):
        self.refresh_thread.start()

    def _request_ip(self):
        logging.debug("请求新的ip")
        res = self.sess.get(self.api_url).content.decode()
        res = json.loads(res)
        if res['success']:
            all_data = res['data']
            for dd in all_data:
                self.ip_pool.add(f"{dd['ip']}:{dd['port']}")
                with self.cond:
                    self.cond.notify_all()
                logging.debug("请求成功")

    def get_ip(self):
        with self.cond:
            self.cond.wait_for(self._has_ip)
            return choice(list(self.ip_pool))

    def report_baned_ip(self, ip):
        logging.debug(f"remove {ip} from pool!")
        self.ip_pool.discard(ip)
        logging.debug(f"now the pool is {self.ip_pool}")

    def report_bad_net_ip(self, ip):
        pass

    def close(self):
        self.refresh_thread.terminate()

    def is_active(self):
        """
        判断当前拉取ip的线程是否存活
        :return:
        """
        return self.refresh_thread.keep_run

    def restart(self):
        """
        重启拉去ip的线程
        :return:
        """
        del self.refresh_thread
        self.refresh_thread = GetIpThread(self.api_url, self.ip_pool, self.cond)
        self.refresh_thread.start()


class GetIpThread(threading.Thread):
    def __init__(self, api_url, ip_pool: set, cond: threading.Condition):
        super().__init__(daemon=True)
        self.url = api_url
        self.ip_pool = ip_pool
        self.cond = cond
        self.keep_run = True
        self.sess = requests.Session()  # 构建 connections pool
        adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
        self.sess.mount("https://", adapter)
        self.sess.mount("http://", adapter)

    def run(self) -> None:
        while self.keep_run:
            if len(list(self.ip_pool)) < 5:
                logging.debug("刷新新的ip")
                response: requests.Response = self.sess.get(self.url)
                content = response.content.decode()
                res = json.loads(content)
                if res['success']:
                    all_data = res['data']
                    for dd in all_data:
                        self.ip_pool.add(f"{dd['ip']}:{dd['port']}")
                        logging.debug("请求成功")
                        with self.cond:
                            self.cond.notify_all()
                response.close()
            sleep(5)

    def terminate(self):
        self.keep_run = False
        logging.debug("关闭刷新ip线程")
