
import abc
from typing import Any


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
