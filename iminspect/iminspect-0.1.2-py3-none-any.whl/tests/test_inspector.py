#!/usr/bin/env python
# coding=utf-8

"""
Very simple test suite (as most of the functionality is GUI-based and thus,
rather complex to test).
"""

import numpy as np
from ..inspector import fmti, fmtb, fmtf, fmt1f, fmt2f, fmt3f, fmt4f, \
    flipLayers


def test_fmtb():
    assert fmtb(True) == 'True'
    assert fmtb(False) == 'False'
    assert fmtb(0) == 'False'
    assert fmtb(-17) == 'True'


def test_fmti():
    assert fmti(3) == '3'
    assert fmti(-0) == '0'
    assert fmti(-42) == '-42'


def test_fmtf():
    assert fmtf(3) == '{:f}'.format(3)
    assert fmtf(17.0099123) == '{:f}'.format(17.0099123)


def test_fmt1f():
    assert fmt1f(3) == '3.0'
    assert fmt1f(17.0099123) == '17.0'
    assert fmt1f(-12.08) == '-12.1'


def test_fmt2f():
    assert fmt2f(3) == '3.00'
    assert fmt2f(17.0099123) == '17.01'
    assert fmt2f(-12.08) == '-12.08'


def test_fmt3f():
    assert fmt3f(3) == '3.000'
    assert fmt3f(17.0099123) == '17.010'
    assert fmt3f(-12.08) == '-12.080'


def test_fmt4f():
    assert fmt4f(3) == '3.0000'
    assert fmt4f(17.0099123) == '17.0099'
    assert fmt4f(-12.08) == '-12.0800'


def test_flipLayers():
    # Single channel image
    x = np.random.rand(3, 3)
    xf = flipLayers(x)
    assert np.all(x == xf)

    # rgb to bgr conversion
    x = np.random.rand(16, 32, 3)
    xf = flipLayers(x)
    for c in range(x.shape[2]):
        assert np.all(x[:, :, c] == xf[:, :, x.shape[2]-c-1])

    # rgbA should be flipped to bgrA
    x = np.random.rand(17, 5, 4)
    xf = flipLayers(x)
    for c in range(x.shape[2]):
        complement = 2-c if c < 3 else 3
        assert np.all(x[:, :, c] == xf[:, :, complement])
