import pika

from vkapi.api import API
from vkapi.session import VKRabbitMQSession

__version__ = '0.9.0'


def create_api(rmq_host='localhost', rmq_port=5672, rmq_virtual_host='/',
               rmq_username='guest', rmq_password='guest',
               rmq_exchange='', rmq_routing_key='api.request',
               api_version='5.92'):
    s = VKRabbitMQSession(
        pika.ConnectionParameters(host=rmq_host,
                                  port=rmq_port,
                                  virtual_host=rmq_virtual_host,
                                  credentials=pika.PlainCredentials(username=rmq_username,
                                                                    password=rmq_password),
                                  blocked_connection_timeout=10),
        rmq_exchange=rmq_exchange,
        rmq_routing_key=rmq_routing_key,
        api_version=api_version
    )

    return API(session=s)
