"""Correct recalled data by comparing with memorized data.

This module defines the core functions for correcting the memory
athletes' recalls.

An unit of data to me memorized and recalled is refered to as an
`item`. The "memorized item" is the data the athlete were supposed
to memorize. The "recall item" is the data the athlete recalled.

The type of item depends on the discipline.

Example items: Word, card, digit, name or date.
"""

# Builtin
import enum
import math
import itertools as it
import collections
from typing import Callable, List, Dict, Tuple, Generator

# PyPI
import unidecode
import numpy as np

# Local
from .types import item_type_numeric, item_type_text, item_type_date


class ItemState(enum.Enum):
    """State of a recalled item

    Attributes:

    correct
        The item is correctly recalled. Recalled item is equal or
        equivalent to memorized item.
    wrong
        The item is not correctly recalled and considered an error.
    spelling_mistake
        The item is not correctly recalled but is not considered an
        error. This is only used in the Words discipline.
    gap
        The item was not recalled at all AND there exists at least one
        item having state correct, wrong or spelling_mistake coming
        somewhere after this item.
    not_reached
        The item was not recalled at all AND there is NO item after
        this one having state equal to correct, wrong, spelling_mistake
        or gap.
    off_limits
        The item has no corresponding memorized-item. E.i. the athlete
        recalled more items than there were items to memorize.
    """
    correct = 0
    wrong = 1
    spelling_mistake = 2
    gap = 3
    not_reached = 4
    off_limits = 5


def _correct_items(m_data, r_data, equivalent_func=None,
                   spelling_mistake_func=None):
    """Internal correcter.

    :param m_data: List of memorized items
    :param r_data: List of recalled items
    :param equivalent_func: Callable used to determine if two items
        are equivalent.
    :param spelling_mistake_func: Callable used to determine if recall
        item is a spelling mistake of memorized item.
    :return: Data structures holding statistics and data needed to
        compute raw score.
    """

    # "No value" refers to a recall gap - no recall value was provided
    no_value = '' if np.issubdtype(m_data.dtype, item_type_text) else -1

    ms = m_data.size
    if ms == 0:
        raise ValueError(f'Memo data is empty!')
    rs = r_data.size
    if rs > ms:
        raise ValueError(f'Recall data length ({r_data.size}) > '
                         f'Memo data length ({m_data.size})')
    elif rs < ms:
        # Add "no value" to r_data to make it same length as m_data
        r_data = np.append(r_data, np.full(ms - rs, no_value))

    # When a memo item is the special value "" (empty string), then no
    # matter what the competitor has recalled, it will be treated as a
    # recall gap.
    if no_value == '':
        m_data[m_data == ''] = 'N/A'
        r_data[m_data == 'N/A'] = ''

    # Correction result, integers are used to indicate item state
    # Ones - because wrong as default
    c_data = np.ones_like(r_data, dtype=np.int32)

    # count will count the different item states
    count = dict()

    # stop_index is the index of the first -1 where all remaining
    # elements are also -1 (and ms when the last element is not -1)
    stop_index = ms - np.argmax(r_data[::-1] != no_value)
    if stop_index == ms and r_data[-1] == no_value:
        # This is needed when r_data is only -1s
        stop_index = 0

    # Not reached items
    c_data[stop_index:] = ItemState.not_reached.value
    count[ItemState.not_reached.name] = ms - stop_index

    # Gap items
    gaps = r_data[:stop_index] == no_value
    c_data[:stop_index][gaps] = ItemState.gap.value
    count[ItemState.gap.name] = np.count_nonzero(gaps)

    # Correct items
    corrects = r_data == m_data
    c_data[corrects] = ItemState.correct.value

    if equivalent_func is not None:
        index_wrong = (c_data == ItemState.wrong.value)
        index_maybe_correct = list()
        for m, r in zip(m_data[index_wrong], r_data[index_wrong]):
            index_maybe_correct.append(equivalent_func(m, r))
        c_data[index_wrong] = np.where(
            index_maybe_correct,
            ItemState.correct.value,
            ItemState.wrong.value
        )

    count[ItemState.correct.name] = np.count_nonzero(
        c_data == ItemState.correct.value)

    if spelling_mistake_func is not None:
        index_wrong = (c_data == ItemState.wrong.value)
        index_spelling_mistake = list()
        for m, r in zip(m_data[index_wrong], r_data[index_wrong]):
            index_spelling_mistake.append(spelling_mistake_func(m, r))
        c_data[index_wrong] = np.where(
            index_spelling_mistake,
            ItemState.spelling_mistake.value,
            ItemState.wrong.value
        )
        count[ItemState.spelling_mistake.name] = \
            np.count_nonzero(index_spelling_mistake)

    # Wrong items (default since c_data was created by ones_like)
    count[ItemState.wrong.name] = np.count_nonzero(
        c_data == ItemState.wrong.value)

    return c_data, stop_index, count


Correction = Tuple[int, Dict[str, int], Generator[ItemState, None, None]]


def correct_numbers(memo_data: List[int], recall_data: List[int],
                    row_length: int = 40) -> Correction:
    """Correct `recall_data` of numerical type.

    >>> m_data = [1, 2, 3, 4, 5, 6,
    ...           7, 8, 9, 0, 1, 2]
    >>> r_data = [1, 2, -1, 4, 5, 6,
    ...           0, 8, 9, -1, -1, -1]
    >>> raw_score, count, c_data=correct_numbers(m_data, r_data, row_length=6)
    >>> raw_score
    5.0
    >>> count
    {'not_reached': 3, 'gap': 1, 'correct': 7, 'wrong': 1}
    >>> status = list(e.name for e in c_data)
    >>> status[:6]
    ['correct', 'correct', 'gap', 'correct', 'correct', 'correct']
    >>> status[-6:]
    ['wrong', 'correct', 'correct', 'not_reached', 'not_reached', 'not_reached']


    :param memo_data: Array of positive integers representing the memorized
        items
    :param recall_data: Array of integers representing the recalled items.
        The value -1 has the special meaning of "empty item" or "recall
        gap". Except -1, other negative values are not allowed.
    :param row_length: Nr of items on each row
    :type row_length: int
    :return: tuple
    """
    if row_length <= 0:
        raise ValueError(f'Row length must be positive ({row_length})')
    m_data = np.array(memo_data, dtype=item_type_numeric)
    r_data = np.array(recall_data, dtype=item_type_numeric)

    c_data, stop_index, count = _correct_items(m_data, r_data)

    # Reshape the data into a matrix with rows of row_length
    grid_data = c_data.reshape(len(c_data) // row_length, row_length)
    raw_score = 0

    # We start by figuring out the score of the last recalled row
    final_row_length = stop_index%row_length
    if final_row_length > 0:
        final_row = grid_data[stop_index//row_length]
        # Compute nr correct items
        nr_c = np.count_nonzero(final_row == ItemState.correct.value)
        if nr_c == final_row_length:
            raw_score += nr_c
        elif nr_c + 1 == final_row_length:
            raw_score += final_row_length/2
        if raw_score < 1:
            # This special case was clarified by Simon Reinhard
            # on messenger 2018-09-16.
            raw_score = 0
        grid_data = grid_data[:stop_index//row_length]
    # From this point we don't have to care about the final row

    # Compute the nr of correct items in each row
    row_result = np.count_nonzero(grid_data == ItemState.correct.value, axis=1)

    # Completely correct rows
    raw_score += row_length*np.count_nonzero(row_result == row_length)

    # Rows with one single mistake
    raw_score += (row_length/2)*np.count_nonzero(row_result + 1 == row_length)
    raw_score = np.ceil(raw_score)

    return raw_score, count, (ItemState(i) for i in c_data)


def correct_words(memo_data: List[str], recall_data: List[str], row_length=20,
                  equivalent_func: Callable[[str, str], bool] = None,
                  spelling_mistake_func: Callable[[str, str], bool] = None
                  ) -> Correction:
    """Correct words

    :param memo_data: Memorized names.
    :param recall_data: Recalled names.
    :param row_length: Nr of columns.
    :param equivalent_func: A callable
    :param spelling_mistake_func:
    :return:
    """
    if row_length <= 0:
        raise ValueError(f'Row length must be positive ({row_length})')
    m_data = np.array(memo_data, dtype=item_type_text)
    r_data = np.array(recall_data, dtype=item_type_text)

    # Convert all words to lowercase so that they can be compared
    m_data = np.char.lower(m_data)
    r_data = np.char.lower(r_data)

    c_data, stop_index, count = _correct_items(
        m_data, r_data, equivalent_func, spelling_mistake_func)
    grid_data = np.reshape(c_data, (len(c_data) // row_length, row_length))
    raw_score = 0

    # We start by figuring out the score of the last recalled row
    final_row_length = stop_index%row_length
    if final_row_length > 0:
        final_row = grid_data[stop_index//row_length]
        # Compute nr correct items
        nr_c = np.count_nonzero(final_row == ItemState.correct.value)
        nr_a = np.count_nonzero(final_row == ItemState.spelling_mistake.value)
        if nr_c + nr_a == final_row_length:
            raw_score += nr_c
        elif nr_c + nr_a + 1 == final_row_length:
            raw_score += max(0, final_row_length/2 - nr_a)
        if raw_score < 1 and nr_a == 0:
            # This special case was clarified by Simon Reinhard
            # on messenger 2018-09-16.
            raw_score = 0
        grid_data = grid_data[:stop_index//row_length]

    # Compute the nr of correct items in each row
    nr_c = np.count_nonzero(grid_data == ItemState.correct.value, axis=1)
    nr_a = np.count_nonzero(grid_data == ItemState.spelling_mistake.value, axis=1)
    nr_ca = nr_c + nr_a

    # Rows with only correct or spelling_mistake
    raw_score += np.sum(nr_c[nr_ca == row_length])

    # Correct and spelling errors
    spelling_mistake_score = (row_length/2 - nr_a).clip(min=0)
    raw_score += np.sum(spelling_mistake_score[nr_ca + 1 == row_length])

    raw_score = np.ceil(raw_score)
    return raw_score, count, (ItemState(i) for i in c_data)


def correct_spoken(memo_data: List[int], recall_data: List[int]) -> Correction:
    """Correct spoken numbers"""
    m_data = np.array(memo_data, dtype=item_type_numeric)
    r_data = np.array(recall_data, dtype=item_type_numeric)
    c_data, _, count = _correct_items(m_data, r_data)

    raw_score = np.argmax(c_data != ItemState.correct.value)
    if raw_score == 0 and c_data[0] == ItemState.correct.value:
        # No non-correct values found => all correct
        raw_score = len(c_data)

    return raw_score, count, (ItemState(i) for i in c_data)


def correct_dates(memo_data: List[int], recall_data: List[int]) -> Correction:
    """Correct historical dates"""
    m_data = np.array(memo_data, dtype=item_type_date[1][1])
    r_data = np.array(recall_data, dtype=item_type_date[1][1])
    c_data, _, count = _correct_items(m_data, r_data)

    c = ItemState.correct.name
    w = ItemState.wrong.name
    raw_score = count[c] - count[w]/2
    raw_score = max(0, raw_score)
    raw_score = np.ceil(raw_score)
    return raw_score, count, (ItemState(i) for i in c_data)


def correct_images(memo_data: List[int], recall_data: List[int]) -> Correction:
    """Correct images"""
    m_data = np.array(memo_data, dtype=item_type_numeric)
    r_data = np.array(recall_data, dtype=item_type_numeric)
    c_data, _, count = _correct_items(m_data, r_data)

    # Reshape the data into a matrix with rows of length 5
    grid_data = c_data.reshape(len(c_data) // 5, 5)

    # Compute the nr of correct items in each row
    row_result = np.count_nonzero(grid_data == ItemState.correct.value, axis=1)
    correct_rows = np.count_nonzero(row_result == 5)

    row_result = np.count_nonzero(grid_data == ItemState.not_reached.value, axis=1)
    empty_rows = np.count_nonzero(row_result == 5)

    row_result = np.count_nonzero(grid_data == ItemState.gap.value, axis=1)
    empty_rows += np.count_nonzero(row_result == 5)

    wrong_rows = len(row_result) - correct_rows - empty_rows

    raw_score = 5*correct_rows - wrong_rows
    raw_score = max(raw_score, 0)
    return raw_score, count, (ItemState(i) for i in c_data)


def correct_names(memo_data: List[str], recall_data: List[str],
                  equivalent_func: Callable[[str, str], bool] = None
                  ) -> Correction:
    """Correct names"""
    m_data = np.array(memo_data, dtype=item_type_text)
    r_data = np.array(recall_data, dtype=item_type_text)

    # Convert all words to lowercase so that they can be compared
    m_data = np.char.lower(m_data)
    r_data = np.char.lower(r_data)

    c_data, _, count = _correct_items(m_data, r_data, equivalent_func)

    # Compute the nr of correct items in each row
    raw_score = np.count_nonzero(c_data == ItemState.correct.value)

    # Anti-guessing rule: To prevent athletes from excessively guessing
    # names, no first or last name must appear more than twice on the
    # recall sheet. From the third name on, there is a penalty of -0.5
    # for each. Example: "Jerry" is written 5 times. 5-2=3 (first two
    # do not count). -0.5*3=-1.5. The penalty is -1.5.
    anti_guessing = collections.Counter(r_data)
    del anti_guessing['']  # Empty values not considered guessing
    penalty = -0.5*sum((v - 2) for v in anti_guessing.values() if v > 2)
    raw_score += penalty

    raw_score = np.ceil(raw_score)
    raw_score = max(raw_score, 0)
    return raw_score, count, (ItemState(i) for i in c_data)


def naive_spellcheck(m_word: str, r_word: str) -> bool:
    """Check if `m_word` equals `r_word` except from one character

    A character may be missing, extra or wrong.

    NOTE: These rules are only applied if the length of `m_word` is
    greater than 5 characters. I.e. for short words, the the words
    has to be exactly equal.

    One character missing:

    >>> naive_spellcheck('daniel', 'danil')
    True

    One character extra:

    >>> naive_spellcheck('daniel', 'daniell')
    True

    One character wrong:

    >>> naive_spellcheck('daniel', 'danjel')
    True

    Short word:

    >>> naive_spellcheck('danie', 'danje')
    False
    """
    m = m_word
    r = r_word
    if m == r:
        return True
    m_len = len(m)
    r_len = len(r)
    if m_len <= 5 or m == r:
        return False
    first_error = 0
    for first_error, (char1, char2) in enumerate(it.zip_longest(m, r)):
        if char1 != char2:
            break
    if m_len == r_len:
        return m[first_error + 1:] == r[first_error + 1:]
    if m_len == r_len + 1:
        return m[first_error + 1:] == r[first_error:]
    if m_len + 1 == r_len:
        return m[first_error:] == r[first_error + 1:]
    return False

def remove_diaeresis(m_word: str, r_word: str) -> bool:
    """Compare if two words are equal except from diaeresis.

    >>> remove_diaeresis('åäöéi', 'aaoei')
    True

    >>> remove_diaeresis('åäöéi', 'åäöéi')
    True
    """
    m = m_word
    r = r_word
    if m != r:
        _m = unidecode.unidecode(m)
        _r = unidecode.unidecode(r)
        return _m == _r
    return True


def points(raw_score: float, standard: float, type_: str = None) -> float:
    """Calculate championship points from raw score.

    >>> points(540, 1_000, type_='other')
    540.0

    The `raw_score` is computed by the arbiter when correcting the
    memory athletes recall data.

    There are three different ways to compute championship points from
    raw score depending on discipline type. Three types are available:

    1. Speed cards
    2. Spoken numbers
    3. Other disciplines.

    The `type_` is used to signal which case to use.

    The `standard` value is specific for each discipline and you should
    lookup a millennium standards table to find the value you want.


    :param raw_score: Integer computed by one of the
        `correct_[numbers/spoken/dates/words/images/names]` functions.
    :param standard: Millennium Standard for this discipline.
    :param type_: The type of discipline. One of: "speed_cards",
        "spoken" or "other".
    :return: Championship points.
    """
    raw_score = float(raw_score)
    if type_ == 'speed_cards':
        # raw_score = seconds
        if raw_score == 0:
            p = 0
        elif raw_score < -52:
            raise ValueError(
                f'Raw score for speed cards too negative: {raw_score}')
        elif raw_score < 0:
            # A negative raw score on speed cards is used to
            # signal the number of correctly recalled cards
            # when at least one error/gap occurred.
            ratio = -raw_score / 52
            max_time = 300  # Seconds
            points_max_time = standard * math.pow(max_time, -0.75)
            p = ratio * points_max_time
        else:
            # Raw score is here interpreted as time in seconds.
            p = standard*math.pow(raw_score, -0.75)
    elif type_ == 'spoken':
        p = standard*math.sqrt(raw_score)
    else:
        p = 1000*raw_score/standard
    # According to Simon Reinhard's comment on Messenger 2018, points
    # should not be rounded. Only the sum of points from each
    # discipline should be rounded to an integer.
    # Quote:
    # "The proper procedure is to keep the points for each discipline
    # to the second decimal - behind the scenes. For the sake of
    # simplicity, the results sheet for a single event always shows
    # an integer. But the Excel sheet carried the decimals for each
    # event over to the total score and only rounded then."
    return p
