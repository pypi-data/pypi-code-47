from pika.exceptions import ChannelClosed, StreamLostError
from json import dumps
from rabbit_connection import RabbitConnection


class Publisher(RabbitConnection):
    __slots__ = []

    def __init__(self, host=None, port=None):
        super().__init__(host, port)
        self._make_connection()

    def __set_queue(self, queue=None):
        try:
            self._channel.queue_declare(queue=queue, durable=True)

        except StreamLostError or ChannelClosed:
            self.reconnect()
            self.__set_queue(queue)

    def __set_exchange(self, exchange):
        self._channel.exchange_declare(exchange=exchange, exchange_type=self.exchange_type)

    @staticmethod
    def __dump_body(body):
        return dumps(body)

    def send(self, body, queue=None):
        name = self._check_queue(queue)

        self.__set_queue(queue=name)
        self.__set_exchange(exchange=name)
        self._channel.basic_publish(exchange=name,
                                    routing_key=name,
                                    body=self.__dump_body(body),
                                    properties=self.properties)
