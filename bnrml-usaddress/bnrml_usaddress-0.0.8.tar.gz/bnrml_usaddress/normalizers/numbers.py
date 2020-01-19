#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 1/12/20
"""
Normalize numbers in text.

.. currentmodule:: numbers
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
from collections import OrderedDict
from decimal import Decimal
import re
import string
from typing import Union
from bnrml.normalizers import Normal, Normalization, Normalizer
from ..errors import BnrmlUsAddressValueError
from ..strutils import camel_dash


#: matches address number suffix separators
_ADDRNUM_SUFFIX_SEP = re.compile(
    r'^[\-]+'
)

#: ordinal suffixes that don't use the common 'nd' suffix
_IRREGULAR_ORDINALS = {
    '1': 'st',
    '3': 'rd'
}

#: matches one or more whitespace characters
_WS = re.compile(r'\s+')


class Extras:
    """Well-known normalization extras for number normalizations."""
    fraction = 'fraction'
    prefix = 'prefix'
    suffix = 'suffix'
    algorithm = 'algorithm'


def tidy_suffix(suffix: str) -> str:
    """
    Clean noise characters from an address suffix.

    :param suffix: the suffix value
    :return: the tidy value
    """
    return _ADDRNUM_SUFFIX_SEP.sub('', suffix) if suffix else suffix


def isnums(s: str):
    """
    Test a string to see if it represents a number.

    :param s: the value
    :return: `True` if and only if the value represents a number
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


class WordsToNumbers:
    """A class that can translate strings of common English words that
    describe a number into the number described
    """

    _WS_PUNCTUATION = str.maketrans(
        string.punctuation, ' ' * len(string.punctuation)
    )  #: string transform that converts punctuation to white space

    #: a mapping of digits to their names when they appear in the
    #: relative "ones" place (this list includes the 'teens' because
    #: they are an odd case where numbers that might otherwise be called
    #: 'ten one', 'ten two', etc. actually have their own names as single
    #: digits do)
    _ONES = {
        'one': 1, 'eleven': 11,
        'two': 2, 'twelve': 12,
        'three': 3, 'thirteen': 13,
        'four': 4, 'fourteen': 14,
        'five': 5, 'fifteen': 15,
        'six': 6, 'sixteen': 16,
        'seven': 7, 'seventeen': 17,
        'eight': 8, 'eighteen': 18,
        'nine': 9, 'nineteen': 19
    }

    #: ordinal suffixes
    _ORDINAL_SUFFIXES = {'st', 'nd', 'rd', 'th'}

    #: words that end with an ordinal suffix, but aren't ordinal words
    _ORDINAL_SUFFIX_EXCEPTIONS = {
        'thousand'
    }

    #: a mapping of ordinal number words (i.e. "first") to their
    #: corresponding cardinal words (i.e. "one")
    _ORDINALS = {
        'first': 'one',
        'second': 'two',
        'third': 'three',
        'fourth': 'four',
        'fifth': 'five',
        'eighth': 'eight',
        'twelfth': 'twelve',
        **{
            f"{item}tieth": f"{item}ty"
            for item in (
                'twen', 'thir', 'four', 'fif', 'six', 'seven', 'eigh',
                'nine'
            )
        }
    }

    #: a mapping of digits to their names when they appear in the 'tens'
    #: place within a number group
    _TENS = {
        'ten': 10,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90
    }

    #: an ordered list of the names assigned to number groups
    _GROUPS = {
        'thousand': 1000,
        'million': 1000000,
        'billion': 1000000000,
        'trillion': 1000000000000
    }

    #: a regular expression that looks for number group names and captures:
    #:     1-the string that preceeds the group name, and
    #:     2-the group name (or an empty string if the
    #:       captured value is simply the end of the string
    #:       indicating the 'ones' group, which is typically
    #:       not expressed)
    _GROUPS_RE = re.compile(
        r'\s?([\w\s]+?)(?:\s((?:%s))|$)' %
        ('|'.join(_GROUPS))
    )

    #: a regular expression that looks within a single number group for
    #: 'n hundred' and captures:
    #:    1-the string that preceeds the 'hundred', and
    #:    2-the string that follows the 'hundred' which can
    #:      be considered to be the number indicating the
    #:      group's tens- and ones-place value
    _HUNDREDS = re.compile(r'([\w\s]+)\shundred(?:\s(.*)|$)')

    #: a regular expression that looks within a single number
    #: group that has already had its 'hundreds' value extracted
    #: for a 'tens ones' pattern (ie. 'forty two') and captures:
    #:    1-the tens
    #:    2-the ones
    _TENS_AND_ONES_RE = re.compile(
        r'((?:%s))(?:\s(.*)|$)' %
        ('|'.join(_TENS.keys()))
    )

    def parse(self, words: str) -> int:
        """
        Parse a string of words to the number they describe.

        :param words: the words
        :return: the number
        :raises BnrmlUsAddressValueError: if the argument isn't convertible
        """
        try:
            return self._parse(words)
        except Exception as ex:
            raise BnrmlUsAddressValueError(words, inner=ex)

    def _parse(self, words):
        """
        Parse a string of words to the number they describe.

        :param words: the words
        :return: the number
        :raises BnrmlUsAddressValueError: if the argument isn't convertible
        """
        # Create a string that eliminates case mismatches by lower-casing
        # letters, stripping leading and trailing whitespace, and replacing
        # punctuation with white spaces.
        _words = words.lower().strip().translate(self._WS_PUNCTUATION)

        # If the input appears to end with an ordinal suffix...
        if _words[-2:] in self._ORDINAL_SUFFIXES:
            # ...split it into tokens.
            wtokens = _words.split(' ')
            # Make sure we're not dealing with a tricky word that appears
            # to end with an ordinal exception, but isn't an ordinal word
            # (like "thousand").
            if wtokens[-1] not in self._ORDINAL_SUFFIX_EXCEPTIONS:
                # So it looks like we have an actual ordinal word.  Find its
                # numeric word analog.
                wtokens[-1] = self._ORDINALS.get(
                    wtokens[-1],
                    wtokens[-1][:-2]  #: the word minus the ordinal
                )
                # Put the string back together for further processesing.
                _words = ' '.join(wtokens)

        # Create the variable to hold the number that shall eventually
        # return to the caller.
        _num = 0
        # Using the 'groups' expression, find all of the number groups
        # and loop through them.
        for group in self._GROUPS_RE.findall(_words):
            # Determine the position of this number group within the entire
            # number...

            # Assume that the group index is the first/ones group
            # until it is determined that it's a higher group.
            group_multiplier = 1
            if group[1] in self._GROUPS:
                group_multiplier = self._GROUPS[group[1]]

            # Determine the value of this number group...

            # Create the variable to hold this number group's value.
            group_num = 0
            # Get the hundreds for this group.
            hundreds_match = self._HUNDREDS.match(group[0])

            # If there is a string in this group matching the 'n hundred'
            # pattern...
            if hundreds_match is not None and hundreds_match.group(
                    1) is not None:
                # ...multiply the 'n' value by 100 and increment this group's
                # running tally.
                group_num = group_num + (
                    self._ONES[hundreds_match.group(1)] * 100
                )
                # The tens- and ones-place value is whatever is left.
                tens_and_ones = hundreds_match.group(2)
            else:
                # iIf there was no string matching the 'n hundred' pattern,
                # assume that the entire string contains only tens- and ones-
                # place values.
                tens_and_ones = group[0]
            # If the 'tens and ones' string is empty, it is time to move along
            # to the next group.
            if tens_and_ones is None:
                # Increment the total number by the current group number, times
                # its multiplier.
                _num = _num + (group_num * group_multiplier)
                continue
            # Look for the tens and ones ('tn1' to shorten the code a bit).
            tn1_match = self._TENS_AND_ONES_RE.match(tens_and_ones)
            # If the pattern is matched, there is a 'tens' place value.
            if tn1_match is not None:
                # Add the tens.
                group_num = group_num + WordsToNumbers._TENS[
                    tn1_match.group(1)]
                # Add the ones.
                if tn1_match.group(2) is not None:
                    group_num = group_num + self._ONES[tn1_match.group(2)]
            else:
                # Assume that the 'tens and ones' actually contained only the
                # ones-place values.
                group_num = group_num + self._ONES[tens_and_ones]
            # Increment the total number by the current group number, times
            # its multiplier.
            _num = _num + (group_num * group_multiplier)
        # The loop is complete, return the result.
        return _num


class SimpleNumberNormalizer(Normalizer):
    """Normalize simple numbers."""
    def normalize(
            self,
            s: str,
            default: Union[str, Normal, None] = None
    ) -> Normalization or None:
        """
        Normalize a simple number value.

        :param s: the value to normalize
        :param default: the default value to return if no normal value applies
        :return: the normalized value
        """
        # Type hints should prevent us from getting an actual numeric type,
        # but we'll allow it.
        if any([isnums(s), isinstance(s, (int, float, Decimal))]):
            sf = float(s)  # the value as an integer
            fr = sf - float(s)  # the fraction
            # Prepare a set of constructor arguments for the normalization.
            cargs = {
                'denormalized': str(s),
                'normalized': str(int(sf)),
                'extras': OrderedDict({
                    Extras.algorithm: camel_dash(type(self).__name__)
                })
            }
            # If the number had a fraction, add that to the extras.
            if fr != 0:
                cargs['extras'][Extras.fraction] = str(fr)
            # There's our normalization.
            return Normalization(**cargs)
        # The value doesn't seem to be a simple number expression.
        return None


class EmbeddedNumberNormalizer(Normalizer):
    """
    Normalize a number embedded within a string.
    """
    _number = re.compile(
        r'(?P<prefix>.*?)(?P<number>\d[\d\s,]+)(?P<suffix>.*)$'
    )  #: matches numbers or embedded numbers

    def normalize(
            self,
            s: str,
            default: Union[str, Normal, None] = None
    ) -> Normalization or None:
        """
        Normalize a simple number value

        :param s: the value to normalize
        :param default: the default value to return if no normal value applies
        :return: the normalized value
        """
        # Look for strings that appear to be numbers.
        match = self._number.match(s)
        # If we matched this pattern...
        if match:
            # ...get the values in the named capturing groups
            groups = {
                k: v.strip() for k, v in {
                    group: (
                        tidy_suffix(match.group(group))
                        if group == Extras.suffix
                        else match.group(group)
                    )
                    for group in (
                        Extras.prefix,
                        'number',
                        Extras.suffix
                    )
                }.items() if v
            }
            # Prepare a set of constructor arguments for a normalization
            # object.
            cargs = {
                'denormalized': s,
                'normalized': groups.get('number'),
            }
            # Round up the normalization extras.
            extras = {
                k: v for k, v in groups.items()
                if k in (
                    Extras.prefix,
                    Extras.suffix
                )
            }
            extras[Extras.algorithm] = camel_dash(type(self).__name__)
            cargs['extras'] = OrderedDict(extras)
            return Normalization(**cargs)
        # These weren't the droids we're looking for.
        return None


class ExpanderCompressorNormalizer(Normalizer):
    """
    Normalize a number embedded within a string.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._words_to_numbers = WordsToNumbers()

    def normalize(
            self,
            s: str,
            default: Union[str, Normal, None] = None
    ) -> Normalization or None:
        """
        Normalize a value.

        :param s: the value to normalize
        :param default: the default value to return if no normal value applies
        :return: the normalized value
        """
        try:
            # Parse the numeric string.
            nums = str(self._words_to_numbers.parse(s))
            return Normalization(
                denormalized=s,
                normalized=nums,
                extras=OrderedDict({
                    Extras.algorithm: camel_dash(type(self).__name__)
                })
            )
        except BnrmlUsAddressValueError:
            return default


def affix_ordinal(number: Union[int, str]) -> str:
    """
    Affix and ordinal suffix to a number.

    :param number: the number
    :return: a string with the appropriate ordinal suffix
    """
    if not number:
        return number
    _numstr = str(number).strip()
    ordinal = _IRREGULAR_ORDINALS.get(_numstr[-1])
    return f"{_numstr}{ordinal}" if ordinal else _numstr
