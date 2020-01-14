import os
import pika
from pika.exceptions import AMQPConnectionError
from time import sleep


class RabbitConnection:
    __slots__ = ['__connection', '_channel', '__host', '__port', '__properties', '__credentials']

    __default_user = 'guest'
    __default_password = 'guest'
    __default_port = os.getenv('RABBIT_PORT') or 5672
    __default_host = os.getenv('RABBIT_HOST') or 'localhost'
    __default_queue = 'receiver'
    __default_exchange_type = 'direct'

    def __init__(self, host=None, port=None, persistent=True):
        self.__host = host
        self.__port = port
        self.__connection = None
        self.__credentials = self.__make_credentials()
        self._channel = None
        self.__properties = self.__set_properties(persistent)

    def _make_connection(self):
        try:
            self.__connection = pika.BlockingConnection(self.__get_connection_parameters(self.__host, self.__port))
            self.__get_channel()

        except AMQPConnectionError:
            sleep(10)
            self._make_connection()

    def __get_channel(self):
        self._channel = self.__connection.channel()

    def __make_credentials(self):
        user = os.getenv('RABBIT_USERNAME') or self.__default_user
        password = os.getenv('RABBIT_PASSWORD') or self.__default_password

        return pika.PlainCredentials(username=user, password=password)

    @property
    def queue(self):
        return self.__default_queue

    @property
    def properties(self):
        return self.__properties

    @property
    def exchange_type(self):
        return self.__default_exchange_type

    def __check_host(self, host):
        if not host:
            return self.__default_host

        return host

    def __check_port(self, port):
        if not port:
            return self.__default_port

        return port

    def _check_queue(self, queue):
        if not queue:
            return self.__default_queue

        return queue

    def __get_connection_parameters(self, host, port):
        return pika.ConnectionParameters(host=self.__check_host(host), port=self.__check_port(port),
                                         credentials=self.__credentials)

    @staticmethod
    def __set_properties(persistent):
        if persistent:
            return pika.BasicProperties(delivery_mode=2)  # delivery_mode = 2 | Make message persistent

        return None

    def reconnect(self):
        if self.__connection.is_closed:
            self._make_connection()

    def close_connection(self):
        if not self.__connection.is_closed:
            self.__connection.close()
