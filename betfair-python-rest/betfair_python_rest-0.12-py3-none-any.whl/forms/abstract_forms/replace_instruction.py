from dataclasses import dataclass


@dataclass
class ReplaceInstruction:
    '''
    Instruction to place a new order
    :param bet_id:
    :param new_price: The price to replace the bet at

    '''
    bet_id: str
    new_price: float

    @property
    def data(self):
        return {
            'betId': self.bet_id,
            'newPrice': self.new_price
        }
