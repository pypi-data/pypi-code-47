from collections import namedtuple

__all__ = [
    'EventType',
    'DataType',
    'ItemState',
    'KeyType',
]

def Enum(name, **fields):
    """Uses named tuple to make an instance with immutable attributes that
    is also enumerable. This is somewhat similar python 3.4 enum
    functionality.
    """
    class EnumFactory(namedtuple(name, fields.keys())):
        def __new__(cls, *args, **kwargs):
            self = super(EnumFactory, cls).__new__(cls, *args, **kwargs)

            reversed_items = tuple(( (v, k) for k,v in self._asdict().items() ))

            def _reverse_dict():
                return dict(reversed_items)

            self._reverse_dict = _reverse_dict
            self.__class__.__name__ = name

            return self

        def __call__(self, value):
            """Reverse lookup by value => SomeEnum('value') """
            return self._reverse_dict()[value]

    instance = EnumFactory(**fields)
    return instance

EventType = Enum('EventType',
    insert='INSERT',
    modify='MODIFY',
    remove='REMOVE')

KeyType = Enum('KeyType',
    hash='HASH',
    range='RANGE'
)

DataType = Enum('DataType',
    binary='B',
    boolean='BOOL',
    number='N',
    string='S',
    list='L',
    null='NULL',
    map='M',
    binary_set='BS',
    number_set='NS',
    string_set='SS')

ItemState = Enum('ItemState',
    does_not_exist='does_not_exist',
    exists='exists',
    new='new')
