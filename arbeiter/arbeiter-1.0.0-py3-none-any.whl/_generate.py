
# Builtin
import re
from typing import List
import string

# PyPI
import unidecode
import numpy as np
import numpy.random as random

# Local
from .types import (item_type_numeric, item_type_date, item_type_text,
                    item_type_image, item_type_name)
from . import exc


def set_random_state(seed: int):
    """Set the numpy seed to make all"""
    global random
    random = np.random.RandomState(seed)


def _get_numbers(nr: int, base: int):
    return random.randint(0, base, size=int(nr), dtype=item_type_numeric)


def get_binary(nr: int):
    return _get_numbers(nr, 2)


def get_numbers(nr: int):
    return _get_numbers(nr, 10)


def get_cards(nr_decks: int):
    return np.array([random.permutation(52) for _ in range(nr_decks)],
                    dtype=item_type_numeric).flatten()


def get_dates(stories: List[str]):
    n = len(stories)
    shuffle_index = random.permutation(n)
    date = random.choice(range(1000, 2100), n, replace=False)
    data = list(zip(shuffle_index, date, stories))
    return np.array(data, dtype=item_type_date)


def get_words(words: List[str]):
    return np.array(words, dtype=item_type_text)


def get_images(files):
    if not len(files)%5 == 0:
        raise ValueError(
            f'Nr files provided ({len(files)}) is not a multiple of 5! '
            f'(Five images per row)'
        )
    shuffle_index = np.array(
        [random.permutation(5) + 1 for _ in range(len(files)//5)],
        dtype=np.int32
    ).flatten()
    data = list(zip(shuffle_index, files))
    return np.array(data, dtype=item_type_image)


def get_names(files, firstnames: List[str], lastnames: List[str]):
    nr = len(files)
    if nr != len(firstnames) or nr != len(lastnames):
        raise ValueError(
            f'Nr of files ({nr}) not same as nr firstnames or lastnames!'
        )
    # Make sure the empty images always comes at the end
    nr_empty = len([l for l in lastnames if l == ''])
    shuffle_index = list(random.permutation(nr - nr_empty))
    shuffle_index += list(range(nr - nr_empty, nr))
    data = list(zip(shuffle_index, files, firstnames, lastnames))
    return np.array(data, dtype=item_type_name)


# Todo: add test for below (or should they be removed?)


def get_binary_from_text(text):
    data = [int(digit) for digit in re.findall('[01]', text, re.MULTILINE)]
    return np.array(data, dtype=item_type_numeric)


def get_numbers_from_text(text):
    data = [int(digit) for digit in re.findall(r'\d', text, re.MULTILINE)]
    return np.array(data, dtype=item_type_numeric)


def get_cards_from_text(text):
    """Parse card-integers from a text"""
    cards = [int(digit) for digit in text.split(',') if digit.strip()]
    for card in cards:
        if not 0 <= card <= 51:
            raise ValueError(f'Card out of range: 0 <= {card} <= 51')
    return np.array(cards, dtype=item_type_numeric)


def get_lines_from_text(text: str, lower=False, only_ascii=False,
                        skip_diaeresis=False, allow_duplicates=False):
    if lower:
        text = text.lower()
    seen = dict()
    lines = text.splitlines()
    output = list()
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if only_ascii:
            if not set(line) <= set(string.ascii_letters):
                continue
        if skip_diaeresis:
            if line != unidecode.unidecode(line):
                continue
        if line in seen:
            # Words might not be unique since different languages
            # may use the same word for two different meanings
            if not allow_duplicates:
                raise exc.DuplicateLinesError(line, seen[line], line_number)
            continue
        seen[line] = line_number
        output.append(line)
    return output


def get_dates_from_text(text, **kwargs):
    return get_dates(get_lines_from_text(text, **kwargs))


def get_words_from_text(text, **kwargs):
    return get_words(get_lines_from_text(text, **kwargs))


def get_lines_from_file(file, error_file_missing=True, error_unicode=True,
                        **kwargs):
    try:
        with open(file, 'r', encoding='utf8') as h:
            text = h.read()
    except FileNotFoundError:
        print(f'Warning: Does not exist: {file}')
        if error_file_missing:
            raise
    except UnicodeDecodeError:
        print(f'Warning: Unicode Error: {file}')
        if error_unicode:
            raise
    else:
        return get_lines_from_text(text, **kwargs)
    return list()
