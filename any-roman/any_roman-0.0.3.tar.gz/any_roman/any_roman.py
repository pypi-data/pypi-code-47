#!/usr/bin/env python3


def int_to_roman(input_number: int, overline_code: str = '\u0305') -> str:
    """
    Recursive function which returns roman numeral (string), given input number (int)

    >>> int_to_roman(0)
    'N'
    >>> int_to_roman(3999)
    'MMMCMXCIX'
    >>> int_to_roman(4000)
    'MV\u0305'
    >>> int_to_roman(4000, overline_code='^')
    'MV^'
    """
    if input_number < 0 or not isinstance(input_number, int):
        raise ValueError(f'Only integers, n, within range, n >= 0 are supported.')
    if input_number <= 1000:
        numeral, remainder = core_lookup(input_number=input_number)
    else:
        numeral, remainder = thousand_lookup(input_number=input_number, overline_code=overline_code)
    if remainder != 0:
        numeral += int_to_roman(input_number=remainder, overline_code=overline_code)
    return numeral


def roman_to_int(roman_numeral: str, overline_code: str = '\u0305') -> int:
    """
    Recursive function which returns arabic numeral (int), given roman numeral (string)

    #>>> roman_to_int('N')
    #0
    #>>> roman_to_int('MMMCMXCIX')
    #'3999'
    #>>> roman_to_int('MV\u0305')
    #4000
    #>>> int_to_roman('MV^', overline_code='^')
    #4000
    """
    pass


def core_lookup(input_number: int) -> (str, int):
    """
    Returns highest roman numeral (string) which can (or a multiple thereof) be looked up from number map and the
    remainder (int).

    >>> core_lookup(3)
    ('III', 0)
    >>> core_lookup(999)
    ('CM', 99)
    >>> core_lookup(1000)
    ('M', 0)
    """
    if input_number < 0 or input_number > 1000 or not isinstance(input_number, int):
        raise ValueError(f'Only integers, n, within range, 0 <= n <= 1000 are supported.')
    basic_lookup = NUMBER_MAP.get(input_number)
    if basic_lookup:
        numeral = basic_lookup
        remainder = 0
    else:
        multiple = get_multiple(input_number=input_number, multiples=NUMBER_MAP.keys())
        count = input_number // multiple
        remainder = input_number % multiple
        numeral = NUMBER_MAP[multiple] * count
    return numeral, remainder


def thousand_lookup(input_number: int, overline_code: str = '\u0305') -> (str, int):
    """
    Returns highest roman numeral possible, that is a multiple of or a thousand that of which can be looked up from
    number map and the remainder (int).

    >>> thousand_lookup(3000)
    ('MMM', 0)
    >>> thousand_lookup(300001, overline_code='^')
    ('C^C^C^', 1)
    >>> thousand_lookup(30000002, overline_code='^')
    ('X^^X^^X^^', 2)
    """
    if input_number <= 1000 or not isinstance(input_number, int):
        raise ValueError(f'Only integers, n, within range, n > 1000 are supported.')
    num, k, remainder = get_thousand_count(input_number=input_number)
    numeral = int_to_roman(input_number=num, overline_code=overline_code)
    numeral = add_overlines(base_numeral=numeral, num_overlines=k, overline_code=overline_code)

    # Assume:
    # 4000 -> MV^, https://en.wikipedia.org/wiki/4000_(number)
    # 6000 -> V^M, see https://en.wikipedia.org/wiki/6000_(number)
    # 9000 -> MX^, see https://en.wikipedia.org/wiki/9000_(number)
    numeral = numeral.replace(NUMBER_MAP[1] + overline_code, NUMBER_MAP[1000])
    return numeral, remainder


def get_thousand_count(input_number: int) -> (int, int, int):
    """
    Returns three integers defining the number, number of thousands and remainder

    >>> get_thousand_count(999)
    (999, 0, 0)
    >>> get_thousand_count(1001)
    (1, 1, 1)
    >>> get_thousand_count(2000002)
    (2, 2, 2)
    """
    num = input_number
    k = 0
    while num >= 1000:
        k += 1
        num //= 1000
    remainder = input_number - (num * 1000 ** k)
    return num, k, remainder


def get_multiple(input_number: int, multiples: iter) -> int:
    """
    Given an input number(int) and a list of numbers, finds the number in list closest (rounded down) to input number

    >>> get_multiple(45, [1, 2, 3])
    3
    >>> get_multiple(45, [1, 2, 3, 44, 45, 46])
    45
    >>> get_multiple(45, [1, 4, 5, 9, 10, 40, 50, 90])
    40
    """
    options = sorted(list(multiples) + [input_number])
    return options[options.index(input_number) - int(input_number not in multiples)]


def add_overlines(base_numeral: str, num_overlines: int = 1, overline_code: str = '\u0305') -> str:
    """
    Adds overlines to input base numeral (string) and returns the result.

    >>> add_overlines(base_numeral='II', num_overlines=1, overline_code='^')
    'I^I^'
    >>> add_overlines(base_numeral='I^I^', num_overlines=1, overline_code='^')
    'I^^I^^'
    >>> add_overlines(base_numeral='II', num_overlines=2, overline_code='^')
    'I^^I^^'
    """
    return ''.join([char + overline_code*num_overlines if char.isalnum() else char for char in base_numeral])


def gen_number_map() -> dict:
    """
    Returns base number mapping including combinations like 4 -> IV and 9 -> IX, etc.
    """
    mapping = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I',
        0: 'N'
    }
    for exponent in range(3):
        for num in (4, 9,):
            power = 10 ** exponent
            mapping[num * power] = mapping[1 * power] + mapping[(num + 1) * power]
    return mapping


NUMBER_MAP = gen_number_map()


if __name__ == '__main__':
    import sys
    print(int_to_roman(int(sys.argv[1])))
