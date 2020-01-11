import json
import uuid
import time
import logging
import functools

import pika
import pika.exceptions

from vkapi.exceptions import VkAPIError
from vkapi.utils import stringify_values

logger = logging.getLogger('vkapi')


class VKRabbitMQSession:
    def __init__(self, connection_parameters, rmq_exchange, rmq_routing_key, api_version):
        """
        Establish connection with RabbitMQ and get ready to send requests

        :param connection_parameters: pika.ConnectionParameters: parameters to connect with
        :param rmq_exchange: str: RabbitMQ exchange to publish requests to
        :param rmq_routing_key: str: RabbitMQ routing key
        :param api_version: str: VK API version to make request with
        """
        self.api_version = api_version

        self._exchange = rmq_exchange
        self._routing_key = rmq_routing_key

        self._conn_params = connection_parameters

        self._connection = None
        self._channel = None

        self._reply_timeout_id = None

        self.open_connection()
        logger.debug('Connected to RabbitMQ with params: %r', self._conn_params)

        self.open_channel()

        logger.info('Created rmq session. params: %r, exchange: %s, routing_key: %s',
                    self._conn_params, self._exchange, self._routing_key)

    def make_request(self, request, retries=0):
        try:
            method_kwargs = {'v': self.api_version}
            method_kwargs.update(request.method_args)

            reply = {}
            # Set up reply consumer
            self._channel.basic_consume('amq.rabbitmq.reply-to',
                                        functools.partial(self.on_reply, reply),
                                        auto_ack=True)

            # Publish the request
            self._channel.basic_publish(
                exchange=self._exchange,
                routing_key=self._routing_key,
                properties=pika.BasicProperties(content_type='application/json',
                                                delivery_mode=1,
                                                reply_to='amq.rabbitmq.reply-to',
                                                priority=request.priority or 3),
                body=json.dumps({
                    "id": uuid.uuid4().hex,
                    "method_name": request.method_name,
                    "method_args": stringify_values(method_kwargs),
                })
            )
            logger.debug('Published request: %r', request)

            # Add timeout for reply
            self._reply_timeout_id = self._connection.call_later(10, self.on_timeout)
            # Get reply
            self._channel.start_consuming()

            logger.debug('Got reply: %s', reply)

            if reply == {}:
                raise TimeoutError('Request %r timed out' % request)

            if reply['error']:
                raise VkAPIError(reply['error'])

            return reply['response']

        except (pika.exceptions.StreamLostError, pika.exceptions.ChannelWrongStateError):
            if retries > 10:
                logger.exception('Connection was not reestablished after 10 retries')
                raise
            logger.debug('Lost connection with RabbitMQ, reconnecting')
            self.open_connection()
            self.open_channel()
            return self.make_request(request, retries + 1)

    def on_reply(self, reply, channel, method, properties, body):
        self._connection.remove_timeout(self._reply_timeout_id)
        reply.update(json.loads(body))
        self._channel.stop_consuming()

    def on_timeout(self):
        self._channel.stop_consuming()

    def open_connection(self, retries=0):
        if (self._connection is None) or self._connection.is_closed:
            try:
                self._connection = pika.BlockingConnection(parameters=self._conn_params)
                logger.info("Connection with RabbitMQ successfully established")
            except pika.exceptions.AMQPConnectionError:
                if retries > 10:
                    raise TimeoutError('Could not connect to RabbitMQ after 10 retries') from None
                logger.debug('Connection to RabbitMQ failed, reconnecting (%i/%i)...', retries, 10)
                time.sleep(2)
                return self.open_connection(retries + 1)

    def open_channel(self):
        if (self._channel is not None) and self._channel.is_open:
            self._channel.close()
        self._channel = self._connection.channel()
