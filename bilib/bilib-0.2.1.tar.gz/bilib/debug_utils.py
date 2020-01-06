#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 bily     Huazhong University of Science and Technology
#
# Distributed under terms of the MIT license.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ipdb
import inspect

__all__ = ['printd', 'debug']

# Copied from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printd(*args):
  # current frame is in the current function, so we move up one level to the caller frame
  last_frame = inspect.currentframe().f_back
  info = inspect.getframeinfo(last_frame)
  print(bcolors.WARNING + '{}/{}/{}:'.format(info.filename, info.lineno, info.code_context[0].strip()) + bcolors.ENDC, *args)

def debug(on=True, context=5):
  if on:
    # current frame is in the current function, so we move up one level to the caller frame
    last_frame = inspect.currentframe().f_back
    ipdb.set_trace(last_frame, context)
