__author__ = "Yannick ARMENTI"

"""
A basic implementation
of the publisher / subscriber pattern.
"""

import abc
from typing import (
    Any, Sequence, Dict, Set
)


class Subscriber(metaclass=abc.ABCMeta):
    """
    The Subsriber is the abstract class (interface)
    for the definition of a listener in the pattern.
    """

    @abc.abstractmethod
    def on_message(self, message: str, arg: Any) -> Any:
        """Executes the action once a publisher
        publishes the message "message" with its argument.

        Args:
            message (str): The key message published from a publisher object.
            arg (Any): The argument published from a publisher object.
        """
        pass


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
        return self._subscribers.copy()

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


if __name__ == "__main__":
    print("Use of the sub/sub pattern.")

    class MockPublisher(Publisher):
        @property
        def triggerable_messages(self) -> Sequence[str]:
            return ["test"]

    class MockSubscriber(Subscriber):
        def on_message(self, message: str, arg: Any) -> Any:
            print(message)
            print(arg)

    print("Instanciation of a publisher-subscriber pair.")
    pub = MockPublisher()
    sub = MockSubscriber()

    print("Attach the subscriber to the publisher.")
    pub.attach(sub, "test")

    print("Publisher triggering 'test' with argument 'Hello' of type str.")
    print("Should print 'test' and 'Hello'")
    pub.trigger("test", "Hello")

    print("Detach the subscriber of the publisher.")
    pub.detach(sub, "test")

    print(
        "Shouldn't print anything as the subsriber"
        "is detached from the publisher."
    )
    pub.trigger("test", "World")

    try:
        pub.attach(sub, "not in messages")
    except Exception as e:
        print(e)
        pass
