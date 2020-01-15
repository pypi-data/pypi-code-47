from ..base import BaseEnum


class MarketStatus(BaseEnum):
    INACTIVE = '''The market has been 
    created but isn't yet available.'''

    OPEN = '''The market is open for betting.'''

    SUSPENDED = '''The market is suspended 
    and not available for betting.'''

    CLOSED = '''The market has been settled 
    and is no longer available for betting.'''
