from pika.exceptions import AMQPChannelError, StreamLostError, ConnectionClosed
from json import dumps
from rabbit_connection import RabbitConnection


class Publisher(RabbitConnection):
    __slots__ = ['__name']

    def __init__(self, host=None, port=None, name=None):
        super().__init__(host, port)
        self.__name = self._check_queue(queue=name)
        self._make_connection()
        self.__set_queue()

    def __set_queue(self):
        try:
            self._channel.queue_declare(queue=self.__name, durable=True)
            self.__set_exchange()

        except StreamLostError or ConnectionClosed or AMQPChannelError:
            self.reconnect()
            self.__set_queue()

    def __set_exchange(self):
        self._channel.exchange_declare(exchange=self.__name, exchange_type=self.exchange_type)

    @staticmethod
    def __dump_body(body):
        return dumps(body)

    def __publish(self, body):
        self._channel.basic_publish(exchange=self.__name,
                                    routing_key=self.__name,
                                    body=self.__dump_body(body),
                                    properties=self.properties)

    def send(self, body):
        try:
            self.__publish(body)

        except StreamLostError or AMQPChannelError or ConnectionClosed:
            self.__set_queue()
            self.__publish(body)
