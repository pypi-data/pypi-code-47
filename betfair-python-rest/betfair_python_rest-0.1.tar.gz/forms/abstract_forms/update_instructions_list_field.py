from dataclasses import dataclass
from typing import List
from . import UpdateInstruction


@dataclass
class UpdateInstructionsField:
    '''
    The number of update instructions.
     The limit of update instructions per request is 60
    '''
    instructions: List[UpdateInstruction]

    @property
    def instructions_data(self):
        return [bet.data for bet in self.instructions]
