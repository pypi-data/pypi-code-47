from ..base import BaseEnum


class PriceData(BaseEnum):
    SP_AVAILABLE = '''Amount available for the BSP auction.'''

    SP_TRADED = '''Amount traded in the BSP auction.'''

    EX_TRADED = '''Amount traded on the exchange.'''

    EX_ALL_OFFERS = '''EX_ALL_OFFERS trumps EX_BEST_OFFERS
     if both settings are present'''

    EX_BEST_OFFERS = '''Only the best prices available 
    for each runner, to requested price depth.'''
