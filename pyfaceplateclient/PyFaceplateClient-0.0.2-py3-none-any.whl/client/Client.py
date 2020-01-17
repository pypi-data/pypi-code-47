#!/usr/bin/env python3

import json
import asyncio
from websockets import connect
import pandas as pd

class _EchoWebsocket():

    def __init__(self, url):
        self.url=url
    async def __aenter__(self):
        self._conn = connect(self.url)
        self.websocket = await self._conn.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()


class EcometClient:
    def __init__(self, host, port, login="", password="", id_count=1):
        self.host=host
        self.port=port
        url = "ws://{host}:{port}/websocket".format(host=self.host, port=self.port)
        self.wws = _EchoWebsocket(url)
        self.loop = asyncio.get_event_loop()

        self.login_query = '{{"id":{id_count},' \
                           '"action":"login",' \
                           '"params":{{"login":{login},"pass":{password}}}' \
                           '}}'.format(id_count=id_count,
                                       login=json.dumps(login),
                                       password=json.dumps(password))
        self.query = ""

    def get_names(self, id_count=1):
        path='.PATH:/root/PROJECT/ARCHIVES'
        path_root='.PATH:/root/.patterns/ARCHIVE'

        self.query = '{{"id":{id_count},' \
                     '"action":"query",' \
                     '"params":{{"query_string":"GET .name WHERE AND(.folder=\'{path}\', ' \
                     '.pattern=\'{path_root}\')"}}}}'.format(id_count=id_count,
                                                             path=path,
                                                             path_root=path_root)

        resp = self.loop.run_until_complete(self.__async__get_data())
        a = self._parsing_names(resp)

        return a

    def get_data(self, id_count=1, archives=None, start_date="2020-01-13T08:41:16Z", step_count=1, step_size=1):

        ID= id_count
        FUNC = 'read_archives'
        arg = 'mean'
        path = '/root/PROJECT/ARCHIVES/'
        STR_DATE=start_date #"2020-01-13T08:41:16Z"
        SIZE = step_size
        STEP = step_count

        archives_as_list = []

        for item, archive in enumerate(archives):
            item_lst = []
            item_arc = path+archive
            item_lst.append(item_arc)
            item_lst.append(arg)
            archives_as_list.append(item_lst)


        ARCHIVES =archives_as_list

        query='{{"id":{ID},' \
              '"action":"application",' \
              '"params":{{"module":"fp_json","function":{FUNC},' \
              '"function_params":{{"archives":{ARCHIVES},' \
              '"periods":{{"start":{STR_DATE},"step_size":{SIZE},"step_count":{STEP},"step_unit":"second"}} }} }} }}'.format(ID=ID,
                                                                                                                         FUNC=json.dumps(FUNC),
                                                                                                                         ARCHIVES=json.dumps(ARCHIVES),
                                                                                                                         SIZE=SIZE,
                                                                                                                         STR_DATE=json.dumps(STR_DATE),
                                                                                                                         STEP=STEP)

        self.query = query
        resp = self.loop.run_until_complete(self.__async__get_data())
        values = resp['result']
        data_time = []
        data_value = []
        data_col_names = archives

        if values == 'invalid_format':
            return 'Error when query data: {0}'.format(values)

        else:
            for row, row_item in enumerate(values):
                data_value_row = []
                for col, col_item in enumerate(row_item):
                    if col == 0:
                        data_time.append(col_item)
                    else:
                        data_value_row.append(col_item)

                data_value.append(data_value_row)

            values=data_value

            df_custom_index = pd.DataFrame(data=values, columns=data_col_names, index=data_time)

            #print("CUSTOM PANDAS DATAFRAME : \n\n", df_custom_index)

            return df_custom_index

    async def __async__get_data(self):
        async with self.wws as echo:
            await echo.send(self.login_query)
            login = json.loads(await echo.receive())
            if login['result']=='ok':
                await echo.send(self.query)
                return json.loads(await echo.receive())

    def _parsing_names(self, data):
        names = []
        for item in data['result']['set']:

            names.append(item['fields']['.name'])

        return names