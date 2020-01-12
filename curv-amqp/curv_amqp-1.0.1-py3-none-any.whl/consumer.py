from __future__ import annotations
import atexit
from typing import Optional, Callable, Any

from pika import spec
from pika.exceptions import ChannelClosed
from curv_amqp.channel import Channel
from curv_amqp.publisher import Publisher
from curv_amqp.exceptions import RequeueRetryCountError, PriorityLevelError


class ConsumerMessage:
    def __init__(self,
                 consumer: Consumer,
                 method: spec.Basic.Deliver,
                 properties: spec.BasicProperties,
                 body: bytes):
        self.consumer = consumer
        self.method = method
        self.properties = properties
        self.body = body
        atexit.register(self.nack)

    def ack(self, multiple: bool = False):
        """Acknowledge one or more messages. When sent by the client, this
        method acknowledges one or more messages delivered via the Deliver or
        Get-Ok methods. When sent by server, this method acknowledges one or
        more messages published with the Publish method on a channel in
        confirm mode. The acknowledgement can be for a single message or a
        set of messages up to and including a specific message.

        :param bool multiple: If set to True, the delivery tag is treated as
                              "up to and including", so that multiple messages
                              can be acknowledged with a single method. If set
                              to False, the delivery tag refers to a single
                              message. If the multiple field is 1, and the
                              delivery tag is zero, this indicates
                              acknowledgement of all outstanding messages.
        """
        try:
            self.consumer.blocking_channel.basic_ack(delivery_tag=self.method.delivery_tag,
                                                     multiple=multiple)
            atexit.unregister(self.nack)
        except Exception as e:
            self.consumer.logger.warning(e)

    def nack(self, multiple: bool = False, requeue: bool = True):
        """This method allows a client to reject one or more incoming messages.
        It can be used to interrupt and cancel large incoming messages, or
        return untreatable messages to their original queue.

        :param bool multiple: If set to True, the delivery tag is treated as
                              "up to and including", so that multiple messages
                              can be acknowledged with a single method. If set
                              to False, the delivery tag refers to a single
                              message. If the multiple field is 1, and the
                              delivery tag is zero, this indicates
                              acknowledgement of all outstanding messages.
        :param bool requeue: If requeue is true, the server will attempt to
                             requeue the message. If requeue is false or the
                             requeue attempt fails the messages are discarded or
                             dead-lettered.

        """
        try:
            self.consumer.blocking_channel.basic_nack(delivery_tag=self.method.delivery_tag,
                                                      multiple=multiple,
                                                      requeue=requeue)
            atexit.unregister(self.nack)
        except Exception as e:
            self.consumer.logger.warning(e)

    def priority_requeue(self,
                         publisher: Publisher,
                         priority: Optional[int] = None,
                         max_priority: int = 5,
                         max_retries: int = 3):
        """This method allows a client to reject/requeue incoming messages while increasing its priority.
            :raises PriorityLevelError
            :raises RequeueRetryCountError
        """
        if priority is not None:
            self.properties.priority = priority
        else:
            if isinstance(self.properties.priority, int):
                self.properties.priority += 1
            else:
                self.properties.priority = 1

        if self.properties.priority > max_priority:
            raise PriorityLevelError(f'Priority exceeded maximum of max_priority={max_priority}')

        if not isinstance(self.properties.headers, dict):
            self.properties.headers = {}

        if 'retries' in self.properties.headers:
            retries = self.properties.headers['retries']
            if isinstance(retries, int):
                retries += 1
            else:
                self.consumer.logger.warning("Invalid header type for retries")
                retries = 1
        else:
            retries = 1

        if retries > max_retries:
            raise RequeueRetryCountError(f'Retries exceeded maximum of {max_retries}')

        self.properties.headers['retries'] = retries
        publisher.publish(routing_key=self.method.routing_key,
                          exchange=self.method.exchange,
                          properties=self.properties,
                          body=self.body)
        # acknowledge the original message after its been re-publish
        self.ack()


class Consumer(Channel):
    is_stopped: bool = False
    consumer_tag: Optional[str] = None

    def stop_consuming(self):
        self.is_stopped = True
        self.blocking_channel.stop_consuming(self.consumer_tag)
        atexit.unregister(self.stop_consuming)

    def consume(self,
                queue: str,
                on_message_callback: Callable[[ConsumerMessage], Any],
                prefetch_count: Optional[int] = None,
                auto_ack: bool = False,
                exclusive: bool = False,
                consumer_tag: Optional[str] = None,
                arguments: Optional[dict] = None):
        self.is_stopped = False
        if prefetch_count is not None:
            self.qos(prefetch_count=prefetch_count)
        atexit.register(self.stop_consuming)

        def _on_message_callback(_,
                                 method: spec.Basic.Deliver,
                                 properties: spec.BasicProperties,
                                 body: bytes):
            message = ConsumerMessage(consumer=self,
                                      method=method,
                                      properties=properties,
                                      body=body)
            on_message_callback(message)

        while not self.is_stopped:
            self.conditional_reconnect()
            self.queue_declare(queue=queue)
            self.consumer_tag = self.blocking_channel.basic_consume(queue=queue,
                                                                    on_message_callback=_on_message_callback,
                                                                    auto_ack=auto_ack,
                                                                    exclusive=exclusive,
                                                                    consumer_tag=consumer_tag,
                                                                    arguments=arguments)
            try:
                self.blocking_channel.start_consuming()
            except ChannelClosed as e:
                self.connection.logger.warning(e)
            except KeyboardInterrupt:
                self.stop_consuming()
