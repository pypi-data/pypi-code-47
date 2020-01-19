#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 1/12/20
"""
Normalize street names.

.. currentmodule:: bnrml_usaddress.normalizers.streetnames
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
from collections import OrderedDict
from typing import Union
from bnrml.normalizers import Normal, Normalization, Normalizer
from .numbers import (
    affix_ordinal,
    Extras,
    ExpanderCompressorNormalizer,
    SimpleNumberNormalizer
)


class StreetNameNormalizer(Normalizer):
    """
    Normalize address numbers.
    """
    #: the algorithm tag we use hen no helper returns a normalization
    _default_algorithm_tag: str = 'default'

    def __init__(
            self,
            affix_ordinals: bool = True,
            **kwargs
    ):
        super().__init__(**kwargs)
        self._affix_ordinals = affix_ordinals
        self._helpers = [
            SimpleNumberNormalizer(),
            ExpanderCompressorNormalizer()
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
                if self._affix_ordinals:
                    return Normalization(
                        denormalized=nzn.denormalized,
                        normalized=affix_ordinal(nzn.normalized),
                        normals=nzn.normals,
                        extras=nzn.extras
                    )
                # Otherwise, just return the normalization.
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
