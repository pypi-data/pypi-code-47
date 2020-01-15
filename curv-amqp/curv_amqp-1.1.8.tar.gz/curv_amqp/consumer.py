from __future__ import annotations
import atexit
from typing import Optional, Callable, Any

from pika import spec
from pika.exceptions import ChannelClosed
from pika.adapters.blocking_connection import _QueueConsumerGeneratorInfo, _ConsumerCancellationEvt
import pika.compat as compat

from curv_amqp.channel import Channel
from curv_amqp.publisher import Publisher
from curv_amqp.exceptions import RequeueRetryCountError, PriorityLevelError, MessageAutoAckError, ChannelClosedError
from curv_amqp.timestamp import get_timestamp_difference_in_seconds


ChannelClosed = ChannelClosed


class ConsumerMessage:
    queued_time: Optional[float] = None

    def __init__(self,
                 consumer: Consumer,
                 method: spec.Basic.Deliver,
                 properties: spec.BasicProperties,
                 body: bytes,
                 auto_ack: bool):
        self.consumer = consumer
        self.method = method
        self.properties = properties
        self.body = body
        self.auto_ack = auto_ack
        if not self.auto_ack:
            atexit.register(self.nack)
        if self.properties.timestamp:
            self.queued_time = get_timestamp_difference_in_seconds(self.properties.timestamp)
            self.consumer.logger.info(f'queued_time: "{self.queued_time}"s')

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
        :raises MessageAutoAckError
        """
        if self.auto_ack:
            raise MessageAutoAckError('Message was set to auto ack')
        try:
            self.consumer.conditional_reconnect()
            self.consumer.blocking_channel.basic_ack(delivery_tag=self.method.delivery_tag, multiple=multiple)
        except ChannelClosedError:
            self.consumer.logger.info('ack failed due to ChannelClosedError')
        except Exception as e:
            self.consumer.logger.error(e, exc_info=True)
        atexit.unregister(self.nack)

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
        :raises MessageAutoAckError

        """
        if self.auto_ack:
            raise MessageAutoAckError('Message was set to auto ack')
        try:
            self.consumer.conditional_reconnect()
            self.consumer.blocking_channel.basic_nack(delivery_tag=self.method.delivery_tag,
                                                      multiple=multiple,
                                                      requeue=requeue)
        except ChannelClosedError:
            self.consumer.logger.info('nack failed due to ChannelClosedError')
        except Exception as e:
            self.consumer.logger.error(e, exc_info=True)
        atexit.unregister(self.nack)

    def priority_requeue(self,
                         publisher: Publisher,
                         priority: Optional[int] = None,
                         max_priority: int = 5,
                         max_retries: int = 3):
        """This method allows a client to reject/requeue incoming messages while increasing its priority.
        :raises PriorityLevelError
        :raises RequeueRetryCountError
        :raises MessageAutoAckError
        """
        if self.auto_ack:
            raise MessageAutoAckError('Message was set to auto ack')
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


class InactivityTimeout:
    def __init__(self, value: float):
        self.value = value


class Consumer(Channel):
    is_stopped: bool = False
    consumer_tag: Optional[str] = None

    def stop_consuming(self):
        self.is_stopped = True
        self.blocking_channel.stop_consuming(self.consumer_tag)
        atexit.unregister(self._at_exit_stop)

    def _at_exit_stop(self):
        try:
            self.stop_consuming()
        except Exception as e:
            self.logger.error(e, exc_info=True)

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
        atexit.register(self._at_exit_stop)

        def _on_message_callback(_,
                                 method: spec.Basic.Deliver,
                                 properties: spec.BasicProperties,
                                 body: bytes):
            message = ConsumerMessage(consumer=self,
                                      method=method,
                                      properties=properties,
                                      body=body,
                                      auto_ack=auto_ack)
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
            except ChannelClosedError:
                self.logger.info('consume channel closed')
                self.stop_consuming()
                break
            except KeyboardInterrupt:
                self.stop_consuming()
                break

    def consume_generator(self,
                          queue: str,
                          prefetch_count: Optional[int] = None,
                          auto_ack: bool = False,
                          exclusive: bool = False,
                          arguments: Optional[dict] = None,
                          inactivity_timeout: Optional[Union[int, InactivityTimeout]] = None):
        """
        NOTE: Use the self.updatable_inactivity_timeout attrbiute to update the inactivity timeout if needded
        Blocking consumption of a queue instead of via a callback. This
        method is a generator that yields each message as a tuple of method,
        properties, and body. The active generator iterator terminates when the
        consumer is cancelled by client via `BlockingChannel.cancel()` or by
        broker.

        Example:

            for method, properties, body in channel.consume('queue'):
                print body
                channel.basic_ack(method.delivery_tag)

        You should call `BlockingChannel.cancel()` when you escape out of the
        generator loop.

        If you don't cancel this consumer, then next call on the same channel
        to `consume()` with the exact same (queue, auto_ack, exclusive) parameters
        will resume the existing consumer generator; however, calling with
        different parameters will result in an exception.

        :param str queue: The queue name to consume
        :param int prefetch_count: qos prefetch_count
        :param bool auto_ack: Tell the broker to not expect a ack/nack response
        :param bool exclusive: Don't allow other consumers on the queue
        :param dict arguments: Custom key/value pair arguments for the consumer
        :param float inactivity_timeout: if a number is given (in
            seconds), will cause the method to yield (None, None, None) after the
            given period of inactivity; this permits for pseudo-regular maintenance
            activities to be carried out by the user while waiting for messages
            to arrive. If None is given (default), then the method blocks until
            the next event arrives. NOTE that timing granularity is limited by
            the timer resolution of the underlying implementation.
            NEW in pika 0.10.0.

        :yields: tuple(spec.Basic.Deliver, spec.BasicProperties, str or unicode)

        :raises ValueError: if consumer-creation parameters don't match those
            of the existing queue consumer generator, if any.
            NEW in pika 0.10.0
        :raises ChannelClosed: when this channel is closed by broker.
        """
        self.is_stopped = False
        self.conditional_reconnect()
        if prefetch_count is not None:
            self.qos(prefetch_count=prefetch_count)
        atexit.register(self.stop_consuming)

        consumer = self._consume_inactivity_timeout(queue=queue,
                                                    auto_ack=auto_ack,
                                                    exclusive=exclusive,
                                                    arguments=arguments,
                                                    inactivity_timeout=inactivity_timeout)

        while not self.is_stopped:
            try:
                self.conditional_reconnect()
                self.queue_declare(queue=queue)
                for method, properties, body in consumer:
                    if method is None and properties is None and body is None:
                        self.logger.warning(f'Consumer timed out after inactivity_timeout = {self.updatable_inactivity_timeout}s')
                        self.stop_consuming()
                        break
                    yield ConsumerMessage(consumer=self,
                                          method=method,
                                          properties=properties,
                                          body=body,
                                          auto_ack=auto_ack)
            except ChannelClosedError:
                self.logger.info('consume_generator channel closed')
                self.stop_consuming()
                break
            except KeyboardInterrupt:
                self.stop_consuming()
                break

    def _consume_inactivity_timeout(self,
                                    queue,
                                    auto_ack=False,
                                    exclusive=False,
                                    arguments=None,
                                    inactivity_timeout=None):
        """Modified blocking channel consume to have an inactivity timeout that can be updated

        Example:

            for method, properties, body in channel.consume('queue'):
                print body
                channel.basic_ack(method.delivery_tag)

        You should call `BlockingChannel.cancel()` when you escape out of the
        generator loop.

        If you don't cancel this consumer, then next call on the same channel
        to `consume()` with the exact same (queue, auto_ack, exclusive) parameters
        will resume the existing consumer generator; however, calling with
        different parameters will result in an exception.

        :param str queue: The queue name to consume
        :param bool auto_ack: Tell the broker to not expect a ack/nack response
        :param bool exclusive: Don't allow other consumers on the queue
        :param dict arguments: Custom key/value pair arguments for the consumer
        :param float inactivity_timeout: if a number is given (in
            seconds), will cause the method to yield (None, None, None) after the
            given period of inactivity; this permits for pseudo-regular maintenance
            activities to be carried out by the user while waiting for messages
            to arrive. If None is given (default), then the method blocks until
            the next event arrives. NOTE that timing granularity is limited by
            the timer resolution of the underlying implementation.
            NEW in pika 0.10.0.

        :yields: tuple(spec.Basic.Deliver, spec.BasicProperties, str or unicode)

        :raises ValueError: if consumer-creation parameters don't match those
            of the existing queue consumer generator, if any.
            NEW in pika 0.10.0
        :raises ChannelClosed: when this channel is closed by broker.

        """
        self.blocking_channel._impl._raise_if_not_open()

        params = (queue, auto_ack, exclusive)

        if self.blocking_channel._queue_consumer_generator is not None:
            if params != self.blocking_channel._queue_consumer_generator.params:
                raise ValueError(
                    'Consume with different params not allowed on existing '
                    'queue consumer generator; previous params: %r; '
                    'new params: %r' % (self.blocking_channel._queue_consumer_generator.params,
                                        (queue, auto_ack, exclusive)))
        else:
            # Need a consumer tag to register consumer info before sending
            # request to broker, because I/O might pick up incoming messages
            # in addition to Basic.Consume-ok
            consumer_tag = self.blocking_channel._impl._generate_consumer_tag()

            self.blocking_channel._queue_consumer_generator = _QueueConsumerGeneratorInfo(
                params, consumer_tag)

            try:
                self.blocking_channel._basic_consume_impl(
                    queue=queue,
                    auto_ack=auto_ack,
                    exclusive=exclusive,
                    consumer_tag=consumer_tag,
                    arguments=arguments,
                    alternate_event_sink=self.blocking_channel._on_consumer_generator_event)
            except Exception:
                self.blocking_channel._queue_consumer_generator = None
                raise

        while self.blocking_channel._queue_consumer_generator is not None:
            # Process pending events
            if self.blocking_channel._queue_consumer_generator.pending_events:
                evt = self.blocking_channel._queue_consumer_generator.pending_events.popleft()
                if type(evt) is _ConsumerCancellationEvt:  # pylint: disable=C0123
                    # Consumer was cancelled by broker
                    self.blocking_channel._queue_consumer_generator = None
                    break
                else:
                    yield (evt.method, evt.properties, evt.body)
                    continue

            if inactivity_timeout is None:
                # Wait indefinitely for a message to arrive, while processing
                # I/O events and triggering ChannelClosed exception when the
                # channel fails
                self.blocking_channel._process_data_events(time_limit=None)
                continue

            # Wait with inactivity timeout
            wait_start_time = compat.time_now()

            timeout_value = inactivity_timeout.value if isinstance(inactivity_timeout, InactivityTimeout) else inactivity_timeout

            wait_deadline = wait_start_time + timeout_value
            delta = timeout_value

            while (self.blocking_channel._queue_consumer_generator is not None and
                   not self.blocking_channel._queue_consumer_generator.pending_events):

                self.blocking_channel._process_data_events(time_limit=delta)

                if not self.blocking_channel._queue_consumer_generator:
                    # Consumer was cancelled by client
                    break

                if self.blocking_channel._queue_consumer_generator.pending_events:
                    # Got message(s)
                    break

                delta = wait_deadline - compat.time_now()
                if delta <= 0.0:
                    # Signal inactivity timeout
                    yield (None, None, None)
                    break
