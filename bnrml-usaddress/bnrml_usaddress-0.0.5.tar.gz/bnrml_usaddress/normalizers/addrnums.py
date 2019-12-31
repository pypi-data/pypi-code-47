#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 12/27/19
"""
Normalize address numbers.

.. currentmodule:: bnrml_usaddress.normalizers.addrnums
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
from collections import OrderedDict
from decimal import Decimal
import re
from typing import Union
from bnrml.normalizers import Normal, Normalization, Normalizer
from ..strutils import camel_dash


class Extras:
    """
    Well-known normalization extras for address numbers.
    """
    fraction = 'fraction'
    prefix = 'prefix'
    suffix = 'suffix'
    algorithm = 'algorithm'


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


class SimpleNumberNormalizer(Normalizer):
    """
    Normalize simple numbers.
    """
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
                    group: match.group(group)
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


class AddressNumberNormalizer(Normalizer):
    """
    Normalize address numbers.
    """
    #: the algorithm tag we use hen no helper returns a normalization
    _default_algorithm_tag: str = 'default'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._helpers = [
            SimpleNumberNormalizer(),
            EmbeddedNumberNormalizer()
        ]  #: helper normalizers

    def normalize(
            self,
            s: str,
            default: Union[str, Normal, None] = None
    ) -> Normalization or None:
        """
        Normalize an integer value.

        :param s: the value to normalize
        :param default: the default value to return if no normal value applies
        :return: the normalized value
        """
        # Let each of the helpers take a crack.
        for helper in self._helpers:
            nzn = helper.normalize(s, default=None)
            if nzn is not None:
                return nzn

        # It looks as though none of the defined functions provided a
        # normalization, so...
        return (
            default if isinstance(default, Normalization)
            else Normalization(
                denormalized=s,
                normalized=default,
                extras=OrderedDict({
                    Extras.algorithm: self._default_algorithm_tag
                })
            )
        ) if default is not None else None
