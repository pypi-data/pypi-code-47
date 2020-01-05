import re
from typing import List


def replace_non_en(string: str, non_en_repl='_', ignore_case=True) -> str:
    if ignore_case:
        string = re.sub(r'[^a-z]', non_en_repl, string, flags=re.IGNORECASE)
    else:
        string = re.sub(r'[^a-z]', non_en_repl, string)
    return string


def decompose_field(string: str) -> List[str]:
    string = re.sub(r'^([^a-z]*)(.*)([^a-z]*)$',
                    r'\2',
                    string,
                    flags=re.IGNORECASE)
    if string.find('_') > -1:
        return string.split('_')

    if string.find('-') > -1:
        return string.split('-')

    if string.lower() == string:
        return [string]

    if string.upper() == string:
        return [string]

    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).split('_')


def to_upper(string: str) -> str:
    strings = decompose_field(string)
    return '_'.join([s.upper() for s in strings])


def to_upper_without_underscore(string: str) -> str:
    strings = decompose_field(string)
    return ''.join([s.upper() for s in strings])


def to_lower(string: str) -> str:
    strings = decompose_field(string)
    return '_'.join([s.lower() for s in strings])


def to_ucc(string: str) -> str:
    strings = decompose_field(string)
    return ''.join([s[0].upper() + s[1:] for s in strings])


def to_lcc(string: str) -> str:
    string = to_ucc(string)
    return string[0].lower() + string[1:]
