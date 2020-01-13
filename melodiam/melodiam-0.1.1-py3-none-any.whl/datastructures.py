import json
from enum import Enum


class Serializable:
    """
        JSON serializable class with __slots__ defined.
    """

    __slots__ = ()

    def to_dict(self) -> dict:
        object_dict = {  # type: ignore[var-annotated]
            key: getattr(self, key, None) for key in self.__slots__
        }
        for key, value in object_dict.items():  # type: ignore[var-annotated]
            if isinstance(value, Serializable):
                object_dict[key] = value.to_dict()
            elif isinstance(value, Enum):
                object_dict[key] = value.value

        return object_dict

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
