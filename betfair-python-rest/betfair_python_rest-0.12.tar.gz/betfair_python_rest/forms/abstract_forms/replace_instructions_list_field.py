from dataclasses import dataclass
from typing import List
from . import ReplaceInstruction


@dataclass
class ReplaceInstructionsField:
    '''
    The number of replace instructions.
    The limit of replace instructions per request is 60.
    '''
    instructions: List[ReplaceInstruction]

    @property
    def instructions_data(self):
        return [bet.data for bet in self.instructions]
