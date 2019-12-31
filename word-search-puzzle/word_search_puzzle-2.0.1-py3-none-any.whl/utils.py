import random
import string
from typing import List
from typing import Generator
from .models import Panel
from .models import Word
from .models import Position
from .models import PositionDistributor
from .models import DEFAULT_IGNORE_CHARACTER


def choose_position_distributor(wights: List[int] = [0.05, 0.15, 0.4, 0.4]) -> PositionDistributor:
    """
    Choose position distributor randomly in order to use it later in the algorithm.

    :param wights: Wights of the selection window.

    :rtype Path:
    :return: A position distributor.
    """
    return PositionDistributor(random.choices(PositionDistributor.get_values(), wights).pop())


def choose_position(panel: Panel) -> Position:
    """
    Choose a random position between [0, panel.height][0, panel.width].

    :param panel: A panel of tpe Panel, where the position selection is executed.

    :rtype Position:
    :return: A random position between [0, panel.height][0, panel.width].
    """
    return Position(r=random.randint(0, panel.height() - 1), c=random.randint(0, panel.width() - 1))


def produce_positions(position: Position, length: int, position_distributor: PositionDistributor) -> Generator[Position, None, None]:
    """
    Produce a list of connected positions starting of a specific position and depending on a position distributor.

    :param position: The starting position.
    :param length: The length of the positions' list.
    :param position_distributor: The position distributor.

    :rtype Generator:
    :return: A generator of requested positions.
    """
    if position_distributor == PositionDistributor.L2R:
        indexes = ((position.r, c) for c in range(position.c, position.c + length))
    if position_distributor == PositionDistributor.U2D:
        indexes = ((r, position.c) for r in range(position.r, position.r + length))
    if position_distributor == PositionDistributor.DU:
        indexes = zip(range(position.r, position.r - length, -1), range(position.c, position.c + length))
    if position_distributor == PositionDistributor.DD:
        indexes = zip(range(position.r, position.r + length), range(position.c, position.c + length))

    return (Position(*index) for index in indexes)


def valid_positions(positions: Generator[Position, None, None], panel: Panel) -> bool:
    """
    Validate if the positions generator is fitting the panel requirements.

    :param positions: A list of position represented as a generator.
    :param panel: The panel.

    :rtype bool:
    :return: Return the validation result.
    """
    def validate(r: int, c: int, height: int, width: int):
        return c < 0 or width <= c or r < 0 or height <= r

    return not any((validate(position.r, position.c, panel.height(), panel.width())) for position in positions)


def insert_word(word: Word, panel: Panel):
    """
    Insert a word in a panel.

    :param word: A hidden word.
    :param panel: The word search puzzle panel.
    """
    index = 0
    for position in word.positions:
        panel[position.r, position.c] = word.value[index]
        index += 1


def fill_remaining_cells(panel: Panel):
    """
    Fill the remaining cells with random letters.

    :param panel: The word search puzzle panel.
    """
    for index in panel.cells.keys():
        if panel[index] == DEFAULT_IGNORE_CHARACTER:
            panel[index] = random.choice(string.ascii_lowercase)


def display_panel(panel: Panel):
    """
    Used for debug purpose.

    :param panel: The word search puzzle panel.
    """
    for r in range(panel.height()):
        for c in range(panel.width()):
            print(panel[r, c], end='  ')
        print()
