import itertools
import time
from typing import List
from typing import Dict
from typing import Any
from .models import Panel
from .models import Word
from .models import Position
from .models import DEFAULT_IGNORE_CHARACTER
from .utils import choose_position
from .utils import fill_remaining_cells
from .utils import produce_positions
from .utils import insert_word
from .utils import valid_positions
from .utils import choose_position_distributor
from .exceptions import PermutationsExceededException


def find_place(word: Word, panel: Panel):
    """
    Find a place for a word inside the panel. The position will be written into word.positions.

    :param panel: The panel where the word should find a place.
    :param word: The word which is looking for a place inside the panel.

    :raise PermutationsExceededException:
    """

    place_found = False
    history = []
    while not place_found and len(history) < 4*len(panel.cells.keys()):
        proposed_position: Position = choose_position(panel)
        position_distributor = choose_position_distributor()
        if [proposed_position, position_distributor] not in history:
            history.append([proposed_position, position_distributor])
        proposed_positions = []
        _, positions = itertools.tee(produce_positions(proposed_position, len(word.value), position_distributor))

        if valid_positions(_, panel):
            for position in positions:
                if panel[position.r, position.c] != DEFAULT_IGNORE_CHARACTER:
                    place_found = False
                    break
                proposed_positions.append(position)
            else:
                place_found = True
                word.positions = proposed_positions

    if not place_found:
        raise PermutationsExceededException(f'Permutations exceeded for word={word}')


def create_panel(height: int, width: int, words_value_list: List[str], maximum_attempts: int = 25, as_dict: bool = False) -> Dict[str, Any]:
    """
    Create a panel with list of hidden words.

    :param height: The number of the rows.
    :param width: The number of the columns.
    :param words_value_list: A list of raw words in order to hide it in the panel.
    :param maximum_attempts: The maximum number of attempts.

    :raise PermutationsExceededException:

    :rtype Dict[str, Any]:
    :return: A word search puzzle panel.
    """

    start_time = int(round(time.time() * 1000))
    attempts = 0
    found = False

    while not found:
        attempts += 1
        try:
            words = []
            panel = Panel(height=height, width=width)
            for word_value in sorted(words_value_list, reverse=True):
                word = Word(word_value.lower())
                find_place(word, panel)
                insert_word(word, panel)
                words.append(word)
            found = True
        except PermutationsExceededException as exception:
            if attempts == maximum_attempts:
                raise exception

    fill_remaining_cells(panel)

    elapsed_time = int(round(time.time() * 1000)) - start_time

    result = {
        'panel': panel,
        'words': words,
        'attempts': attempts,
        'found': found,
        'elapsed_time': elapsed_time
    }

    if as_dict:
        result['panel'] = panel.as_dict()
        result['words'] = [word.as_dict() for word in words]

    return result
