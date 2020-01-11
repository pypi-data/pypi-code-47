import json
import uuid
import asyncio
import logging

import aioamqp

from aiovkrmq.exceptions import VkAPIError
from aiovkrmq.utils import stringify_values

logger = logging.getLogger('vkapi')


class AMQPVKSession:
    def __init__(self, rmq_exchange, rmq_routing_key, api_version, conn_params=None):
        """
        :param rmq_exchange: str: RabbitMQ exchange to publish requests to
        :param rmq_routing_key: str: RabbitMQ routing key
        :param api_version: str: VK API version to make request with
        :param conn_params: dict: Connection parameters for aioamqp.connect()
        """
        self.api_version = api_version

        self._exchange = rmq_exchange
        self._routing_key = rmq_routing_key

        self._conn_params = conn_params or {}
        self._conn_params['login_method'] = 'PLAIN'

        self._connection = None

        self._consumers = {}

    @classmethod
    async def create(cls, *args, **kwargs):
        """
        Async factory method for AMQPVKSession.
        Instantiates AMQPVKSession, opens AMQP connection and channel

        :return: AMQPVKSession instance
        """
        s = cls(*args, **kwargs)

        await s._open_connection()
        logger.info('Created rmq session. params: %r, exchange: %s, routing_key: %s',
                    s._conn_params, s._exchange, s._routing_key)

        return s

    async def make_request(self, request, retries=0):
        """
        Publish request, wait for response, recursively retry on failure up to 10 times

        :param request: dict: vkapi.api.Request
        :param retries: number of retries already made
        :raises: VkAPIError: if VK API responded with an error
        :return: VK API response
        """
        consumer_tag = channel = None
        try:
            method_kwargs = {'v': self.api_version}
            method_kwargs.update(request.method_args)

            channel = await self._open_channel()

            # Set up reply consumer
            consumer_tag = (await channel.basic_consume(
                callback=self._on_reply,
                queue_name='amq.rabbitmq.reply-to',
                no_ack=True
            ))['consumer_tag']

            self._consumers[consumer_tag] = asyncio.Future()

            # Publish the request
            await channel.basic_publish(
                exchange_name=self._exchange,
                routing_key=self._routing_key,
                properties=dict(content_type='application/json',
                                delivery_mode=1,
                                reply_to='amq.rabbitmq.reply-to',
                                priority=request.priority or 3),
                payload=json.dumps({
                    "id": uuid.uuid4().hex,
                    "method_name": request.method_name,
                    "method_args": stringify_values(method_kwargs),
                }).encode()
            )
            logger.debug('Published request: %r', request)

            # Wait for reply at most 10 seconds
            await asyncio.wait_for(self._consumers[consumer_tag], 10)
            reply = self._consumers[consumer_tag].result()

            await channel.basic_cancel(consumer_tag)
            del self._consumers[consumer_tag]
            await channel.close()

            logger.debug('Got reply: %s', reply)

            if reply['error']:
                raise VkAPIError(reply['error'])

            return reply['response']

        except (aioamqp.exceptions.AmqpClosedConnection, aioamqp.exceptions.ChannelClosed):
            if retries > 10:
                logger.exception('Connection was not reestablished after 10 retries')
                raise
            logger.debug('Lost AMQP connection, reconnecting')
            await self._open_connection()
            await self._open_channel()
            return await self.make_request(request, retries + 1)

        except asyncio.TimeoutError:
            if consumer_tag:
                await channel.basic_cancel(consumer_tag)
            raise TimeoutError('Request %r timed out' % request) from None

    async def _on_reply(self, channel, body, envelope, properties):
        if not self._consumers[envelope.consumer_tag].cancelled():
            self._consumers[envelope.consumer_tag].set_result(json.loads(body))

    async def _open_connection(self, retries=0):
        if self._connection is None or self._connection.connection_closed.is_set():
            try:
                _, self._connection = await aioamqp.connect(**self._conn_params)
                logger.info("AMQP connection successfully established")
            except (aioamqp.exceptions.AmqpClosedConnection, ConnectionError):
                if retries > 10:
                    raise TimeoutError('Could not establish AMQP connection after 10 retries') from None
                logger.debug('AMQP connection failed, reconnecting (%i/%i)...', retries, 10)
                await asyncio.sleep(2)
                return await self._open_connection(retries + 1)

    async def _open_channel(self):
        return await self._connection.channel()

    async def close(self):
        logger.info('Closing AMQP connection')
        await self._connection.close(timeout=3)
