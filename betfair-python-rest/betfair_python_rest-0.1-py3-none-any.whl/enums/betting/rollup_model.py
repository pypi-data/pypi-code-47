from ..base import BaseEnum


class RollupModel(BaseEnum):
    STAKE = '''The volumes will be rolled up to
     the minimum value which is >= rollupLimit.'''

    PAYOUT = '''The volumes will be rolled up 
    to the minimum value where the
     payout( price * volume ) is >= rollupLimit. 
     On a LINE market, volumes will be rolled up 
     where payout( 2.0 * volume ) is >= rollupLimit'''

    MANAGED_LIABILITY = '''The volumes will be 
    rolled up to the minimum value which 
    is >= rollupLimit, until a lay price threshold. 
    There after, the volumes will be rolled up 
    to the minimum value such that the 
    liability >= a minimum liability. 
    Not supported as yet.'''

    NONE = '''No rollup will be applied.
     However the volumes will be filtered by currency 
     specific minimum stake unless 
     overridden specifically for the channel.'''

