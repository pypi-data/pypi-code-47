import asyncio
import sys
from rifbot.JsonHelpers import options_to_json
from rifbot.gql_queries import QUERIES, SUBSCRIPTIONS, MUTATIONS
from .GqlClient import GqlClient
from .Okta import Okta
from shortid import ShortId

sid = ShortId()


class Rifbot:
    def __init__(self, rifbot_server: str,
                 okta_domain: str,
                 okta_client_id: str,
                 okta_client_secret: str,
                 text1: str = None,
                 text2: str = None):

        self.rifbot_server = rifbot_server
        self.okta_domain = okta_domain
        self.okta_client_id = okta_client_id
        self.okta_client_secret = okta_client_secret
        self.connected = False
        self.dbg = 0
        self.nodes = {}
        self._custom_init = {
            'node': {
                'name': 'python-client',
                'id': sid.generate(),
                'text1': text1,
                'text2': text2
            }
        }

    async def listen(self, next_callback=None):
        # if self.connected is False: raise Exception('Use connect() first')
        await self.connect()
        if (next_callback is not None):
            await asyncio.gather(
                asyncio.create_task(self.apollo.listen()),
                asyncio.create_task(next_callback())
            )
        else:
            await self.apollo.listen()

    async def pingQuery(self):
        if self.connected is False: raise Exception('Use listen() first')
        return await self.apollo.query(QUERIES['PING'], variables={})

    async def pingSubscribe(self, callback):
        if self.connected is False: raise Exception('Use listen() first')
        subscribe_id = await self.apollo.subscribe(SUBSCRIPTIONS['PING'], callback=callback)
        return subscribe_id

    def close(self):
        if self.connected is False: raise Exception('Cannot close: not listening')
        self.apollo.close()

    async def push_backtest(self, strategy, options, result_callback=None, update_callback=None):
        if self.connected is False: raise Exception('Use listen() first')
        options_json = options_to_json(options)

        node = await self._action_node_backtest(options_json)
        node_id = node['id']
        self.nodes[node_id] = {
            'result': {}
        }

        def subscribe_cb(raw, id):
            topic = raw['topic']
            data = raw['data']
            node = raw['node']

            if topic == 'result':
                self.nodes[node_id]['result'].update(data)
                is_complete = data.get('complete') is not None
                # print('is_complete:', is_complete)
                # print('is_complete', is_complete, data.get('complete'))
                if is_complete is True and result_callback is not None:
                    result_callback(self.nodes[node_id]['result'], node_id)
                    del self.nodes[node_id]

            elif topic == 'update' and update_callback is not None:
                update_callback(raw, node_id)

        await self._subscribe_node(node_id, subscribe_cb)
        return node

    async def connect(self):
        self.okta = Okta(self.okta_domain)
        self.auth = self.okta.get_client_credentialflow_token(self.okta_client_id, self.okta_client_secret)
        self.authToken = self.auth['access_token']
        self.apollo = GqlClient(self.rifbot_server, self.authToken, self._custom_init)
        try:
            await self.apollo.connect()
            self.connected = True
        except BaseException as e:
            print ('Cannot connect to Rifbot server ')
            raise e

    async def get_backtest(self, id):
        if self.connected is False: raise Exception('Use connect() first')
        node = await self._query_node(id)

        if node is None or node['id'] is None:
            raise Exception('Backtest id "' + str(id) + '" Not Found on the server')

        updates = []
        results = []
        result = {}

        for message in node['messages']:
            topic = message['topic']
            data = message['data']
            # print('topic:', message['topic'])
            if topic == 'update':
                updates.append(data)
            elif topic == 'result':
                results.append(data)
                result.update(data)

        node['updates'] = updates
        node['results'] = results
        node['result'] = result if len(result) > 0 else None

        return node

    async def _query_nodes(self):
        return await self.apollo.query(QUERIES['LIST_NODES'])

    async def _query_node(self, node_id):
        return await self.apollo.query(QUERIES['GET_NODE_FULL'], {
            'id': node_id
        })

    async def _subscribe_node(self, node_id, callback):
        return await self.apollo.subscribe(SUBSCRIPTIONS['NODE'], {
            'id': node_id
        }, callback)

    async def _action_node_backtest(self, options):
        return await self.apollo.mutate(MUTATIONS['ACTION_NODE'], {
            'nodeId': 'server-beast', #FIXME
            'action': 'Backtest',
            'options': options
        })
