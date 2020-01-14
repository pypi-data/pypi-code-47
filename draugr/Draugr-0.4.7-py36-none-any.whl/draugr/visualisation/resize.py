#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from warg import passes_kws_to
import cv2

__author__ = 'Christian Heider Nielsen'
__doc__ = r'''

           Created on 01/12/2019
           '''


@passes_kws_to(cv2.resize)
def resize_image_cv(x, target_size: tuple, interpolation=cv2.INTER_LINEAR, **kwargs):
  """

:param x:
:param target_size: proper (width, height) shape, no cv craziness
:return:
"""
  if x.shape != target_size:
    x = cv2.resize(x, target_size[::-1], interpolation=interpolation, **kwargs)
  return x
