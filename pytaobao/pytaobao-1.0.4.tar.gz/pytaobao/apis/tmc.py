# -*- coding: utf8 -*-

import aiohttp
from pytaobao.apis.base import TaobaoClient


class TMCClient(TaobaoClient):

    def __init__(self,
                 app_key: str,
                 app_secret: str,
                 session: str,
                 sign_method: str = 'md5',
                 endpoint: str = 'http://gw.api.taobao.com/router/rest'):
        """Init.

        :param str app_key: App id
        :param str app_secret: App secret
        :param str session:
        :param str endpoint: Api hostname
        :param str sign_method:
        """
        super().__init__(app_key,
                         app_secret,
                         session,
                         sign_method,
                         endpoint)
        self.url = 'ws://mc.api.taobao.com/'
        self.session = aiohttp.ClientSession()

    async def start(self):
        async with self.session.ws_connect(self.url) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == 'close cmd':
                        await ws.close()
                        break
                    else:
                        await ws.send_str(msg.data + '/answer')
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break
