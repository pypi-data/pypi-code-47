from enum import Enum


class BaseEnum(Enum):
    '''
    Parent class for all enums allowed tp get tuples of two format:
    key-value (in that package the key is a value too, so its rather call key-key)
    key-description (key, which can be used as a value too, and a description of enum choice)
    '''
    @classmethod
    def choices(cls):
        return ((x.name, x.name) for x in cls)

    @classmethod
    def choices_with_descriptions(cls):
        return ((x.name, x.value) for x in cls)
