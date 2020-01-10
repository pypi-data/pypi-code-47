#!/usr/bin/env python3
# coding: utf-8

import weakref

from joker.aligner.algor import Aligner
from joker.aligner.utils import load_submat

__version__ = '0.1'

# cache a few aligners
_wref_aligners = weakref.WeakValueDictionary()

_all_schemes = {
    'local': Aligner.LOCAL,
    'global': Aligner.GLOBAL,
    'overlap': Aligner.OVERLAP,
}


def create_aligner(submat='blosum60', rho=13, sigma=1, scheme='global'):
    if scheme not in _all_schemes.values():
        scheme = _all_schemes[scheme]
    istr, jstr, submat = load_submat(submat)
    a = istr, jstr, submat, rho, sigma, scheme
    return Aligner.from_submat(*a)


def get_aligner(submat='blosum60', rho=13, sigma=1, scheme='global'):
    if scheme not in _all_schemes.values():
        scheme = _all_schemes[scheme]
    key = submat, rho, sigma, scheme
    try:
        return _wref_aligners[key]
    except KeyError:
        pass
    aligner = create_aligner(submat, rho, sigma, scheme)
    _wref_aligners[key] = aligner
    return aligner
