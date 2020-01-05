"""This is the arbeiter package

This module implements the most important tasks an arbeiter does during
a memory competition:

- Compute raw scores of recall data for each type of discipline.
- Compute championship points from raw score.
- Help organizer to generate memorization/recall data to the correct
  data type.

"""


from ._correct import (
    # Raw score calculators
    correct_numbers, correct_spoken, correct_dates, correct_words,
    correct_images, correct_names,

    # Calculate points from raw score
    points,

    # Spellcheck words functions
    naive_spellcheck,

    # Names and faces - compare names without diaeresis
    remove_diaeresis,

    # Cell value
    ItemState
)

from ._generate import (
    # Used to help arbeiter generate memorization data of correct type
    set_random_state,

    get_binary, get_numbers, get_cards, get_dates, get_words, get_images,
    get_names,

    get_binary_from_text, get_numbers_from_text, get_cards_from_text,
    get_dates_from_text, get_words_from_text,

    get_lines_from_text,
    get_lines_from_file,
)

__all__ = [
    # Core functions
    'correct_numbers',
    'correct_spoken',
    'correct_dates',
    'correct_words',
    'correct_images',
    'correct_names',

    # Helpers
    'points',
    'naive_spellcheck',
    'remove_diaeresis',
    'ItemState',

    # Set seed for random generator
    'set_random_state',

    # Get data in correct type
    'get_binary',
    'get_numbers',
    'get_cards',
    'get_dates',
    'get_words',
    'get_images',
    'get_names',

    # Get data from text
    'get_binary_from_text',
    'get_numbers_from_text',
    'get_cards_from_text',
    'get_dates_from_text',
    'get_words_from_text',

    # Utility functions
    'get_lines_from_text',
    'get_lines_from_file',
]
