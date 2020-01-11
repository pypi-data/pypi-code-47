from aiovkrmq.api import API
from aiovkrmq.session import AMQPVKSession

__version__ = '1.0.2'


async def create_api(rmq_host='localhost', rmq_port=5672, rmq_virtual_host='/',
                     rmq_username='guest', rmq_password='guest',
                     rmq_exchange='vk_requests', rmq_routing_key='api.request',
                     api_version='5.95'):
    s = await AMQPVKSession.create(conn_params=dict(host=rmq_host,
                                                    port=rmq_port,
                                                    virtualhost=rmq_virtual_host,
                                                    login=rmq_username,
                                                    password=rmq_password),
                                   rmq_exchange=rmq_exchange,
                                   rmq_routing_key=rmq_routing_key,
                                   api_version=api_version
                                   )

    return API(session=s)
