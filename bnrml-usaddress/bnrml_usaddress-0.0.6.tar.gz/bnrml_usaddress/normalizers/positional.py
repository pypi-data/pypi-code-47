#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 12/29/19
"""
Normalize place names.

.. currentmodule:: bnrml_usaddress.normalizers.placenames
.. moduleauthor:: Pat Daburu <pat@daburu.net>
"""
# from typing import Any, Dict, Iterable, Mapping, NamedTuple, Set, Union
# from bnrml import Normal, Normalizer, Normalization
# from pytypewriter import Exportable
#
#
# class PositionalNormal(Exportable):
#
#     def __init__(
#             self,
#             normal: Normal,
#             positions: Iterable[int]
#     ):
#         self._normal: Normal = normal
#         self._positions = set(positions) if positions else None
#
#     @property
#     def normal(self) -> Normal:
#         return self._normal
#
#     @property
#     def positions(self) -> Iterable[int]:
#         return self._positions
#
#     def export(self) -> Mapping[str, Any]:
#         """
#         Export the instance as a mapping of simple types.
#
#         :return: the mapping
#         """
#         return {
#             'normal': self._normal.export(),
#             'positions': list(self._positions)
#         }
#
#     @classmethod
#     def load(cls, data: Mapping[str, Any]) -> 'PositionalNormal':
#         """
#         Create an instance from a mapping.
#
#         :param data: the data
#         :return: the instance
#         """
#         # Construct the instance.
#         return cls(
#             **{
#                 'normal': Normal.load(data.get('normal')),
#                 'positions': data.get('positions')
#             }
#         )
#
#
# class PositionalNormalizer(Normalizer):
#     """
#     Normalize place names.
#     """
#
#     def __init__(
#             self,
#             normals: Iterable[PositionalNormal],
#             **kwargs
#     ):
#         self._pos_normals: Set[int, Dict[str, Normal]] = set()
#         super().__init__(**kwargs)
#
#     def normalize(
#             self,
#             s: str,
#             default: Union[str, Normal, None] = None
#     ) -> Normalization or None:
#         """
#         Normalize a place name.
#
#         :param s: the value to normalize
#         :param default: the default value to return if no normal value applies
#         :return: the normalized value
#         """
#         # Type hints should prevent us from getting an actual numeric type,
#         # but we'll allow it.
#         if any([isnums(s), isinstance(s, (int, float, Decimal))]):
#             sf = float(s)  # the value as an integer
#             fr = sf - float(s)  # the fraction
#             # Prepare a set of constructor arguments for the normalization.
#             cargs = {
#                 'denormalized': str(s),
#                 'normalized': str(int(sf)),
#                 'extras': OrderedDict({
#                     Extras.algorithm: camel_dash(type(self).__name__)
#                 })
#             }
#             # If the number had a fraction, add that to the extras.
#             if fr != 0:
#                 cargs['extras'][Extras.fraction] = str(fr)
#             # There's our normalization.
#             return Normalization(**cargs)
#         # The value doesn't seem to be a simple number expression.
#         return None
