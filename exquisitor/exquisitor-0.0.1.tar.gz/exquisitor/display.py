#!/usr/bin/env python2
#
# Copyright (C) 2015-2019 David J. Beal, All Rights Reserved
#

import Xlib
import Xlib.display
from Xlib import X

class Display(object):
    display = Xlib.display.Display()
    screen = display.screen()
    root = screen.root
    screen_width = screen.width_in_pixels
    screen_height = screen.height_in_pixels

