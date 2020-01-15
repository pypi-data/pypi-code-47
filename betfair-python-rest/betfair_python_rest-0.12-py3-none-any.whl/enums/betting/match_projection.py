from ..base import BaseEnum


class MatchProjection(BaseEnum):
    NO_ROLLUP = '''No rollup, return raw fragments'''

    ROLLED_UP_BY_PRICE = '''Rollup matched amounts 
    by distinct matched prices per side.'''

    ROLLED_UP_BY_AVG_PRICE = '''Rollup matched amounts 
    by average matched price per side'''
