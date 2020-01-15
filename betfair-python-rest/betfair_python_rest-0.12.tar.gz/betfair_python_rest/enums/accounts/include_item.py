from ..base import BaseEnum


class IncludeItem(BaseEnum):
    ALL = '''The'''
    DEPOSITS_WITHDRAWALS = '''Include payments only'''
    EXCHANGE = '''Include exchange bets only'''
    POKER_ROOM = '''Include poker transactions only'''
