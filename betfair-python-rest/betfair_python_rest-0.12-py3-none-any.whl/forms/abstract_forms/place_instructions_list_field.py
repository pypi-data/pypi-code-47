from dataclasses import dataclass
from typing import List
from . import PlaceInstruction


@dataclass
class PlaceInstructionsField:
    '''
    The list of place instructions.
    The limit of place instructions per request is
    200 for the Global Exchange and 50 for the Italian Exchange.
    '''
    instructions: List[PlaceInstruction]

    @property
    def instructions_data(self):
        return [bet.data for bet in self.instructions]
