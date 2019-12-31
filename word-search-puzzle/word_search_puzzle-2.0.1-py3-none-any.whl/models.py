import copy
import itertools
from typing import List
from typing import Dict
from enum import IntEnum
from dataclasses import field
from dataclasses import dataclass
from .exceptions import PanelCreationException


DEFAULT_IGNORE_CHARACTER = '*'


class PositionDistributor(IntEnum):
    """
    PositionDistributor enum used to to tell the algorithm how to find a position for a word inside a panel.

        1. L2R (Left to Right). Find the following example for (word='cat' and panel=3x4):
            * * * *
            * c a t
            * * * *
        2. U2D (Up to Down). Find the following example for (word='cat' and panel=3x4):
            * * c *
            * * a *
            * * t *
        3. DU (Diagonal Up). Find the following example for (word='cat' and panel=3x4):
            * * * t
            * * a *
            * c * *
        4. DD (Diagonal Down). Find the following example for (word='cat' and panel=3x4):
            c * * *
            * a * *
            * * t *
    """

    L2R = 0
    U2D = 1
    DU = 2
    DD = 3

    @staticmethod
    def get_values():
        """
        Get all values of the enum.

        :rtype List:
        :return: List of PositionDistributor values.
        """
        return list(map(int, PositionDistributor))


@dataclass
class Position:
    """
    Position class used only to store 2D positions and has to fields:

        1. r (Row number)
        1. c (Column number)
    """
    r: int = field(metadata={'description': 'Horizontal index'})
    c: int = field(metadata={'description': 'Vertical index'})

    def as_dict(self):
        return {
            'r': self.r,
            'c': self.c
        }


@dataclass
class Word:
    """
    Word class used to store a word with its corresponding position inside a panel.
    """
    value: str = field(metadata={'description': 'The actual text'})
    positions: List[Position] = field(default_factory=list, metadata={'description': 'The positions of the letters'})

    def as_dict(self):
        return {
            'value': self.value,
            'positions': [position.as_dict() for position in self.positions]
        }


@dataclass
class Panel:
    """
    Panel class is the main class where all the words should be hidden.
    """
    cells: Dict[tuple, str] = field(default_factory=dict, metadata={'description': 'Matrix of letters'})

    def __init__(self, height: int = None, width: int = None, clone: 'Panel' = None, **kwargs):
        """
        Panel initializer. If the dimensions (height, width) or a reference panel to clone, then the panel will be
        created with a 0x0 dimensions.

        :param height: The number of the rows.
        :param width: The number of the columns.
        :param clone: A reference panel to clone.
        :param kwargs: Used for the super class.

        :raise PanelCreationException:
        """
        super(Panel, self).__init__(**kwargs)
        if height is not None or width is not None or clone is not None:
            if clone is not None:
                if height is not None or width is not None:
                    raise PanelCreationException('Arguments conflict. Pass either (clone:{}) or (height:{}, width:{})'.format(
                        Panel.__init__.__annotations__.get('clone'),
                        Panel.__init__.__annotations__.get('height'),
                        Panel.__init__.__annotations__.get('width')
                    ))
            else:
                if height is None or width is None:
                    raise PanelCreationException('Arguments conflict. Pass either (clone:{}) or (height:{}, width:{})'.format(
                        Panel.__init__.__annotations__.get('clone'),
                        Panel.__init__.__annotations__.get('height'),
                        Panel.__init__.__annotations__.get('width')
                    ))

            if clone is not None and isinstance(clone, Panel):
                self.cells = copy.deepcopy(clone.cells)
            else:
                self.cells = dict()
                for index in itertools.product(range(height), range(width)):
                    self.cells[index] = DEFAULT_IGNORE_CHARACTER
        else:
            self.cells = dict()

    def height(self) -> int:
        """
        Get the number of the rows.

        :rtype int:
        :return: The number of the rows.
        """
        return 1 + max(self.cells.keys(), key=lambda index: index[0])[0]

    def width(self) -> int:
        """
        Get the number of the columns.

        :rtype int:
        :return: The number of the columns.
        """
        return 1 + max(self.cells.keys(), key=lambda index: index[1])[1]

    def __getitem__(self, index: tuple) -> str:
        """
        Get the letter at index, where index is a tuple of 2 integers (r, c).

        :param index: The index of the requested letter.

        :rtype str:
        :return: The letter at index.
        """
        r, c = index[0], index[1]
        return self.cells[r, c]

    def __setitem__(self, index: tuple, letter: str):
        """
        Set a letter at index, where index is a tuple of 2 integers (r, c).

        :param index: The index of the requested letter.
        :param letter: The letter that should be inserted at the index.
        """
        self.cells[index] = letter

    def as_dict(self):
        return {
            'cells': [{
                'position': Position(*key).as_dict(),
                'value': value
            } for key, value in self.cells.items()]
        }