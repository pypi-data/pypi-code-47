#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2018 bily     Huazhong University of Science and Technology
#
# Distributed under terms of the MIT license.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

__all__ = ['unstack']


def unstack(array, axis=0):
  return [np.squeeze(x, axis) for x in np.split(array, array.shape[axis], axis)]
