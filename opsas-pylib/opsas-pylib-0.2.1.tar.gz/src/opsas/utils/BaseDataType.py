from dataclasses import asdict
from dataclasses import dataclass


@dataclass()
class BaseDataType:

    @property
    def dict(self):
        return asdict(self)

    def __str__(self):
        return self.format_str

    @property
    def format_str(self):
        return ", ".join([f"{key}:{str(value)}" for (key, value) in self.dict.items()])

    @classmethod
    def get_attr_list(cls):
        return cls.__init__.__code__.co_varnames[1:]

    @classmethod
    def create_instance_from_dict(cls, data_dict):
        """
        Create an class instance and set value with dict.
        If required param defined in cls.__init__ , fill it with None.

        Args:
            data_dict:

        Returns:
            cls instance
        """
        init_kwargs = {}
        for attr in cls.get_attr_list():
            init_kwargs[attr] = data_dict.get(attr, None)
        return cls(**init_kwargs)
