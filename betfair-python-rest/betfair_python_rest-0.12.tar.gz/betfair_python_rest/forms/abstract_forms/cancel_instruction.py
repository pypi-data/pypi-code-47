from dataclasses import dataclass


@dataclass
class CancelInstruction:
    '''
    Instruction to place a new order
    :param bet_id:
    :param size_reduction: If supplied then this
     is a partial cancel.  Should be set to 'null'
     if no size reduction is required.

    '''
    bet_id: str
    size_reduction: float = None

    @property
    def data(self):
        return {
            'betId': self.bet_id,
            'sizeReduction': self.size_reduction
        }
