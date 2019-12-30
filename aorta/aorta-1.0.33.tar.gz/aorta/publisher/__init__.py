import os
import uuid

from aorta import const
from aorta.lib import timezone
from aorta.lib.datastructures import DTO
from aorta.lib.datastructures import ImmutableDTO
from aorta.messaging import EventMessage
from aorta.messaging import CommandMessage
from aorta.buf.spooled import SpooledBuffer
from .base import BasePublisher


class CommandPublisher(BasePublisher):
    """A :class:`BasePublisher` implementation that
    publishes command messages.
    """
    message_class = CommandMessage

    #: Specifies the default lifetime of commands. Default
    #: is ``None``.
    lifetime = None

    def issue(self, name, params=None, on_settled=None, address=None, correlation_id=None, triggered_by=None):
        """Publishes a message representing the issued command `name`
        with the given parameters `params`.

        Args:
            name (str): the fully-qualified name of the issued
                command.
            params (dict): a dictionary containing the command parameters.
            on_settled: a callback function that is invoked, with the
                :class:`~aorta.messaging.CommandMessage` as its first
                positional argument, when durability responsibility
                is transferred to the backend.
            address (str): indicates the destination at the AMQP peer.
                May be ``None``.
            correlation_id (bytes): specifies the ``correlation-id``
                of the outgoing command, if it was issued because of
                a prior message.
            triggered_by (bytes): specifies the message that directly
                triggered this publication.

        Returns:
            None
        """
        if isinstance(params, (DTO, ImmutableDTO)):
            params = params.as_dict()
        message = self.message_class(address=address or self.address)
        message.set_object_type(name)
        message.body = params or {}
        message.correlation_id = correlation_id
        if triggered_by:
            message.set_triggered_by(triggered_by)
        return self.publish(message, on_settled=on_settled)

    def setdefaults(self, message):
        message.properties[const.APROP_COMMAND_ISSUED] = timezone.now()
        if self.lifetime:
            message.properties[const.APROP_COMMAND_EXPIRES] =\
                message.properties[const.APROP_COMMAND_ISSUED] + self.lifetime


class NullCommandPublisher(CommandPublisher):
    """A :class:`CommandPublisher` implementation that
    does not publish its messages and simply returns them.
    """

    def publish(self, message, *args, **kwargs):
        return message


class EventPublisher(BasePublisher):
    """A :class:`BasePublisher` implementation that provides
    additional functionality to publish event messages.
    """
    message_class = EventMessage

    def observe(self, name, params=None, on_settled=None, observed=None,
        occurred=None, address=None, correlation_id=None, triggered_by=None):
        """Publishes a message representing observed event `name` with
        the given parameters `params`.

        Args:
            name (str): the fully-qualified name of the observed
                event.
            params (dict): a dictionary containing the event parameters.
            observed (int): the number of milliseconds since the UNIX epoch,
                specifying the date and time at which the event was observed.
            occurred (int): the number of milliseconds since the UNIX epoch,
                specifying the date and time at which the event occurred.
            on_settled: a callback function that is invoked, with the
                :class:`~aorta.messaging.EventMessage` as its first
                positional argument, when durability responsibility
                is transferred to the backend.
            address (str): indicates the destination at the AMQP peer.
                May be ``None``.
            correlation_id (bytes): specifies the ``correlation-id``
                of the outgoing event, if it was observed because of
                a prior message.
            triggered_by (bytes): specifies the message that directly
                triggered this publication.

        Returns:
            None

        The :meth:`observe()` method ensures that all properties and
        annotations (refer to the AMQP 1.0 specification for their
        meanings) required by the Aorta framework are set on each
        outgoing message. For ``Event`` messages specifically,
        :meth:`publish()` provides defaults for the following
        properties:

        - `aorta.const.P_EVENT_OBSERVED`
        - `aorta.const.P_EVENT_OCCURRED`

        This is in addition to the properties set by the :class:`EventPublisher`
        superclasses.

        It also guarantees that the message body is a :class:`dict`.
        """
        if isinstance(params, (DTO, ImmutableDTO)):
            params = params.as_dict()
        message = self.message_class(address=address or self.address)
        message.properties[const.APROP_EVENT_OBSERVED] =\
            observed or timezone.now()
        message.properties[const.APROP_EVENT_OCCURRED] =\
            occurred or timezone.now()
        message.set_object_type(name)
        message.body = params or {}
        message.correlation_id = correlation_id
        if triggered_by:
            message.set_triggered_by(triggered_by)
        return self.publish(message, on_settled=on_settled)


class NullEventPublisher(EventPublisher):
    """A :class:`NullEventPublisher` implementation that
    does not publish its messages and simply returns them.
    """

    def publish(self, message, *args, **kwargs):
        return message
