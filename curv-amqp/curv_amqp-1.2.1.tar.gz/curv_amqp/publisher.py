from typing import Optional, NamedTuple, List, Union
from copy import deepcopy
from uuid import uuid4

from pika.spec import BasicProperties
from pika.exceptions import NackError, UnroutableError

import simplejson

from curv_amqp.channel import Channel
from curv_amqp.timestamp import get_timestamp_in_milliseconds

NackError = NackError
UnroutableError = UnroutableError
PublishBody = Union[NamedTuple, dict, list, tuple, str, bytes]


class Publisher(Channel):
    def publish_messages(self,
                         routing_key: str,
                         bodies: List[PublishBody],
                         exchange: str = '',
                         properties: Optional[BasicProperties] = None,
                         mandatory: bool = False):
        self.queue_declare(queue=routing_key)

        for body in bodies:
            self.publish(routing_key=routing_key,
                         body=body,
                         exchange=exchange,
                         properties=properties,
                         mandatory=mandatory,
                         queue_declare=False)

    def publish(self,
                routing_key: str,
                body: PublishBody,
                exchange: str = '',
                properties: Optional[BasicProperties] = None,
                mandatory: bool = False,
                queue_declare: bool = True):
        """Publish to the channel with the given exchange, routing key, and
        body.
        NOTE: Having this automatically decalre the queue for you is slow in a loop.

        For more information on basic_publish and what the parameters do, see:

            http://www.rabbitmq.com/amqp-0-9-1-reference.html#basic.publish

        NOTE: mandatory may be enabled even without delivery
          confirmation, but in the absence of delivery confirmation the
          synchronous implementation has no way to know how long to wait for
          the Basic.Return.

        :param str routing_key: The routing key to bind on
        :param bytes body: The message body; empty string if no body
        :param str exchange: The exchange to publish to
        :param pika.spec.BasicProperties properties: message properties
        :param bool mandatory: The mandatory flag
        :param bool queue_declare: Set to False to skip auto queue declare

        :raises UnroutableError: raised when a message published in
            publisher-acknowledgments mode (see
            `BlockingChannel.confirm_delivery`) is returned via `Basic.Return`
            followed by `Basic.Ack`.
        :raises NackError: raised when a message published in
            publisher-acknowledgements mode is Nack'ed by the broker. See
            `BlockingChannel.confirm_delivery`.
        """
        if isinstance(body, NamedTuple):
            body_dict = body._asdict()
            message_body = simplejson.dumps(body_dict, ignore_nan=True)
        elif isinstance(body, (dict, list, tuple)):
            message_body = simplejson.dumps(body, ignore_nan=True)
        elif isinstance(body, str):
            message_body = bytes(body, 'utf-8')
        elif isinstance(body, bytes):
            message_body = body
        else:
            raise ValueError(f'Invalid body input type="{type(body)}"')
        # NOTE: Defaults to persistent delivery mode, creates a timestamp,
        # and unique message id as a uuid4 hex
        if properties is not None:
            props = deepcopy(properties)
        else:
            props = BasicProperties()
        if props.delivery_mode is None:
            props.delivery_mode = 2
        if props.timestamp is None:
            props.timestamp = get_timestamp_in_milliseconds()
        if props.message_id is None:
            props.message_id = uuid4().hex
        self.conditional_reconnect()

        if queue_declare:
            # NOTE: This makes the sending of a message much slow so don't do this in a loop.
            self.queue_declare(queue=routing_key)

        self.blocking_channel.basic_publish(exchange=exchange,
                                            routing_key=routing_key,
                                            body=message_body,
                                            properties=props,
                                            mandatory=mandatory)
