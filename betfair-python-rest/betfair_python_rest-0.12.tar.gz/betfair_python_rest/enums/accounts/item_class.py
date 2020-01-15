from ..base import BaseEnum


class ItemClass(BaseEnum):
    UNKNOWN = '''Statement item not mapped to 
    a specific class. All values will be concatenated 
    into a single key/value pair. The key will be 
    'unknownStatementItem' and the value will be a 
    comma separated string. Please note: This is 
    used to represent commission payment items.'''
