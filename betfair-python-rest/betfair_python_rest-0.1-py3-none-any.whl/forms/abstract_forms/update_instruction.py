from dataclasses import dataclass


@dataclass
class UpdateInstruction:
    '''
    Instruction to update LIMIT bet's
    persistence of an order that do not affect exposure
    :param bet_id:
    :param new_persistence_type: The new
    persistence type to update this bet to

    '''
    bet_id: str
    new_persistence_type: str

    @property
    def data(self):
        return {
            'betId': self.bet_id,
            'newPersistenceType': self.new_persistence_type
        }
