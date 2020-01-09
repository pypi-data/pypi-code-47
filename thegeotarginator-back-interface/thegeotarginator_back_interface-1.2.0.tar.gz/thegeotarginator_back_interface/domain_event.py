from typing import Generic, TypeVar, Type

from thegeotarginator_back_interface.json_serializable import DictSerializable

T = TypeVar('T', bound=DictSerializable)


class DomainEvent(Generic[T]):

    def __init__(self, timestamp: int, data: T):
        self.timestamp: int = timestamp
        self.data: T = data

        self.__is_domain_event__: bool = True

    @staticmethod
    def from_dict(json_dict: dict, event_type: Type[T]):
        data = json_dict["data"]
        loaded_data = event_type.from_dict(data)
        timestamp = json_dict["timestamp"]
        return DomainEvent(timestamp, loaded_data)
