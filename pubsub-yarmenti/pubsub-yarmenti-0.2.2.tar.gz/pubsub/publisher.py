
import abc
from typing import (
    Any, Sequence, Dict, Set
)
from .subscriber import Subscriber


class Publisher(metaclass=abc.ABCMeta):
    """
    The Publisher is the abstract class (interface)
    for the definition of a sender in the pattern.
    """

    @property
    @abc.abstractmethod
    def triggerable_messages(self) -> Sequence[str]:
        """
        Returns an iterable of the messages (type <str>) that can
        be sent by any of the instances.
        """
        pass

    @property
    def subscribers(self) -> Dict[str, Set[Subscriber]]:
        """Lazy initialization of the object's subsribers.

        Returns:
            Dict[str, Set[Subscriber]]: A dictionary with the messages as keys
            and values as a set of Subscriber.
        """
        if not hasattr(self, "_subscribers"):
            self._subscribers: Dict[str, Set[Subscriber]] = {}
        return self._subscribers

    def attach(self, subscriber: Subscriber, message: str) -> None:
        """Attaches the given Subscriber with the given message
        to the current instance.

        Args:
            subscriber (Subscriber): The Subscriber (listener) to attach.
            message (str): The message it listens to.

        Raises:
            ValueError: If the given message is not in
            the triggerable_messages.

        """
        if message not in self.triggerable_messages:
            raise ValueError(
                "Message '{}' not in triggerable_messages.".format(message)
            )

        self.subscribers.setdefault(message, set()).add(subscriber)

    def detach(self, subscriber: Subscriber, message: str) -> None:
        """Detaches the given Subscriber with the given message
        to the current instance.

        Args:
            subscriber (Subscriber): The Subscriber (listener) to attach.
            message (str): The message it listened to.
        """
        self.subscribers.setdefault(message, set()).discard(subscriber)

    def trigger(self, message: str, arg: Any = None) -> None:
        """Publishes (sends) the given message with the given arguments
        to all listeners in the subsribers variable.

        Args:
            message (str): The message to be sent
            arg (Any, optional): The optional argument sent with this message.
        """
        subscribers = self.subscribers.setdefault(message, set())
        _ = [sub.on_message(message, arg) for sub in subscribers]
