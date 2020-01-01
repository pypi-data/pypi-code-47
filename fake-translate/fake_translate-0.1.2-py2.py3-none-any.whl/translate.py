# -*- encoding: utf-8 -*-
"""
@File           : faketranslate.py
@Time           : 2019/12/30 19:31
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : faketranslate
@description    : 描述
"""
import os
import time
import sys
import requests
from fake_useragent import UserAgent
from setting import *


class Translate(object):
    def __init__(self):
        self.session = requests.session()
        self.ua = UserAgent()

    def trans_youdao(self, keyword):
        salt = int(time.time() * 10000)
        ts = int(salt / 10)

        form_data = {
            "i": keyword,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": "abf857d70c24cb55263b1f624193b38b",
            "ts": ts,
            # "bv": "bbb3ed55971873051bc2ff740579bb49",
            "bv": "316dd52438d41a1d675c1d848edf4877",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        headers = {
            "User-Agent": self.ua.random,
        }

        try:
            with self.session.post(url=YOUDAO_URL, params=form_data, headers=headers) as resp:
                resp.raise_for_status()
                if resp.status_code == 200:
                    json_data = resp.json()
                    if json_data['errorCode'] == 0:
                        res = json_data['translateResult'][0][0]['tgt']
                        print('[有道]翻译结果：{}'.format(res))
                    else:
                        print('[有道]翻译结果：未找到翻译内容！')
                else:
                    print(resp.status_code)
        except Exception as ex:
            print(ex)

    def trans_baidu(self, keyword):
        print('[百度]翻译结果：{}'.format('暂无'))

    def trans_google(self, keyword):
        print('[谷歌]翻译结果：{}'.format('暂无'))

    def trans_powerword(self, keyword):
        print('[词霸]翻译结果：{}'.format('暂无'))

    def get_result(self, keyword, trans_args):
        print('输入要翻译的词：{}'.format(keyword))
        if trans_args:
            if trans_args == '-y':
                self.trans_youdao(keyword)
                return

            if trans_args == '-b':
                self.trans_baidu(keyword)
                return

            if trans_args == '-g':
                self.trans_google(keyword)
                return

            if trans_args == '-p':
                self.trans_powerword(keyword)
                return

        else:
            self.trans_youdao(keyword)
            self.trans_baidu(keyword)
            self.trans_google(keyword)
            self.trans_powerword(keyword)

    def run(self, keywords: list = None, trans_args: str=None):
        if keywords:
            print('*' * 100)
            for word in keywords:
                self.get_result(word, trans_args)
            print('*' * 100)
        else:
            print('请输入要翻译的词')


def exec():
    if len(sys.argv) < 2:
        print('docstring and usage')
        return

    # words = [sys.argv[1]] if len(sys.argv) > 1 else None
    if sys.argv[1].startswith('--'):
        option = sys.argv[1][1:]
        if option == 'help':
            print('help')

        return
    else:
        for arg in sys.argv[1:]:
            if arg.startswith('-'):
                option = arg[1:]
                if option == 'v':
                    print('{} version {}'.format(os.path.basename(__file__).split('.')[0], VERSION))
                    return

                if option == 'a':
                    pass

                if option == 'y':
                    pass

                trans_args = option
            else:
                trans_args = None

        t = Translate()
        t.run(["apple"], trans_args)


if __name__ == '__main__':
    exec()
