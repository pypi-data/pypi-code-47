#!/usr/bin/env python

import curses_util.util as util
import curses
import re
import signal
import sys


def sigint(*args):
    util.cursesclean()
    sys.exit(1)


signal.signal(signal.SIGINT, sigint)

# Public API


class Menu():

    """A class representing a menu capable of vending items.

Usage:

    menu = Menu(mark_color_fg=curses.COLOR_MAGENTA,
                mark_color_bg=curses.COLOR_BLACK,
                select_color_bg=curses.COLOR_CYAN,
                select_color_fg=curses.COLOR_BLACK):

    selected = menu.vend([ 'item ' + str(i) for i in range(100) ])
"""

    def __init__(self,
                 select_color_bg='black',
                 select_color_fg='white',
                 mark_color_fg='white',
                 mark_color_bg='black',
                 custom_actions={},
                 exit_keys=['q'],
                 select_keys=['\n']):

        colors = {
            'black': curses.COLOR_BLACK,
            'blue': curses.COLOR_BLUE,
            'cyan': curses.COLOR_CYAN,
            'green': curses.COLOR_GREEN,
            'magenta': curses.COLOR_MAGENTA,
            'red': curses.COLOR_RED,
            'white': curses.COLOR_WHITE,
            'yellow': curses.COLOR_YELLOW
        }

        self.mark_color_fg = colors[mark_color_fg]
        self.mark_color_bg = colors[mark_color_bg]
        self.select_color_bg = colors[select_color_bg]
        self.select_color_fg = colors[select_color_fg]

        self.exit_keys = exit_keys
        self.select_keys = select_keys
        self.custom_actions = custom_actions

    def _move_up(self):
        self.sel -= self.opnum

        if self.sel < 0:
            self.first -= -1 * self.sel
            self.sel = 0

        if self.first < 0:
            self.first = 0
            self.sel = 0

    def _move_down(self):
        nitems = len(self.items)
        max_sel = nitems - 1 if self.sh > nitems else self.sh - 1
        max_first = 0 if self.sh > nitems else nitems - self.sh

        self.sel += self.opnum if self.opnum else 1

        if self.sel > max_sel:
            if self.sh < nitems:
                self.first += self.sel - self.sh + 1
            if self.first > max_first:
                self.first = max_first
            self.sel = max_sel

    def _unmark_items(self):
        base = self.first + self.sel
        for i in range(self.opnum):
            self.marked.discard(base + i)

        self._move_down()

    def _mark_items(self):
        nitems = len(self.items)
        base = self.first + self.sel
        num = self.opnum

        if base + num > nitems:
            num = nitems - base

        for i in range(num):
            self.marked.add(base + i)

        self._move_down()

    def _search_backward(self):
        num = self.opnum if self.opnum else 1
        for _ in range(num):
            for i in range(self.first + self.sel - 1, -1, -1):
                if self.search_query in self.display(self.items[i]):
                    self.opnum = self.sel + self.first - i
                    self._move_up()
                    break

    def _search_forward(self):
        num = self.opnum if self.opnum else 1
        for _ in range(num):
            for i in range(self.first + self.sel + 1, len(self.items)):
                if self.search_query in self.display(self.items[i]):
                    self.opnum = i - self.sel - self.first
                    self._move_down()
                    break

    def _draw_items(self):
        self.scr.erase()
        height, width = self.scr.getmaxyx()

        display_items = self.items[self.first:self.first + height]

        display_items = map(lambda x:
                            self.display(x).replace('\t', '    ')[:width - 1],
                            display_items)

        for i, item in enumerate(display_items):
            item += (width - len(item) - 1) * " "
            if i == self.sel:
                if i + self.first in self.marked:
                    self.scr.addstr(item, self.highlight_and_select_colors)
                else:
                    self.scr.addstr(item, self.select_colors)
            elif i + self.first in self.marked:
                self.scr.addstr(item, self.mark_colors)
            else:
                self.scr.addstr(item)

            if i < (height - 1):
                self.scr.addstr("\n")

        self.scr.move(self.sel, width - 1)
        self.scr.refresh()

    def _onresize(self):
        self.sh, self.sw = self.scr.getmaxyx()
        self.scr.clear()
        self._draw_items()

    def _vend(self, markable):
        if not self.items:
            return None

        for item in self.items:
            if "\n" in self.display(item):
                raise Exception("Newline not permitted in menu items")

        last_char = ''
        self._draw_items()
        while True:
            c = self.scr.getch()

            selected = [self.items[i] for i in self.marked] if self.marked else\
                [self.items[self.first + self.sel]]

            if c in self.custom_actions:
                self._cleanup()
                self.custom_actions[c](selected)
                self._curses_init()

            elif chr(c) in self.custom_actions:
                self._cleanup()
                self.custom_actions[chr(c)](selected)
                self._curses_init()

            elif chr(c) == 'g' and last_char == 'g':
                self.sel = 0
                self.first = 0

            elif chr(c) == 'G':
                if len(self.items) < self.sh:
                    self.first = 0
                    self.sel = len(self.items) - 1
                else:
                    self.first = len(self.items) - self.sh
                    self.sel = self.sh - 1

            elif c == curses.KEY_DOWN or chr(c) == 'j':  # Up
                self.opnum = self.opnum if self.opnum else 1
                self._move_down()
                self.opnum = 0

            elif c == curses.KEY_UP or chr(c) == 'k':  # Down
                self.opnum = self.opnum if self.opnum else 1
                self._move_up()
                self.opnum = 0

            elif c == 5:  # ctrl-e
                self.opnum = self.opnum if self.opnum else 1

                osel = self.el
                self.sel = self.sh - 1
                self._move_down()
                self.sel = osel

                self.opnum = 0

            elif c == 25:  # ctrl-y
                self.opnum = self.opnum if self.opnum else 1

                osel = self.sel
                self.sel = 0
                self._move_up()
                self.sel = osel

                self.opnum = 0

            elif c == 6 or c == curses.KEY_RIGHT:  # ctrl-f
                self.sel = self.sh - 1
                self.opnum = self.sh
                self._move_down()
                self.opnum = 0

            elif c == 2 or c == curses.KEY_LEFT:  # ctrl-b
                self.sel = 0
                self.opnum = self.sh
                self._move_up()
                self.opnum = 0

            elif chr(c) == 'f':  # expensive
                self.item_filter = util.input("Filter: ")
                if re.match('^[A-Za-z0-9]+$', self.item_filter):
                    fitems = [i
                              for i in self.oitems
                              if self.item_filter in self.display(i)]
                else:
                    fitems = [i
                              for i in self.oitems
                              if re.match(self.item_filter, self.display(i))]

                if len(fitems) != 0:
                    self.items = fitems
                    self.first = 0
                    self.sel = 0
                    self.marked.clear()

            elif chr(c) == 'n':
                self.opnum = self.opnum if self.opnum else 1
                self._search_forward()
                self.opnum = 0

            elif chr(c) == 'N':
                self.opnum = self.opnum if self.opnum else 1
                self._search_backward()
                self.opnum = 0

            elif chr(c) == '?':
                self.search_query = util.input('?')
                self._search_backward()

            elif chr(c) == '/':
                self.search_query = util.input('/')
                self._search_forward()

            elif c in self.exit_keys or chr(c) in self.exit_keys:
                util.cursesclean()
                return None

            elif c in self.select_keys or chr(c) in self.select_keys:
                util.cursesclean()
                return selected

            elif chr(c) == 'u':
                self.opnum = self.opnum if self.opnum else 1
                self._unmark_items()
                self.opnum = 0

            elif chr(c) == 'm':
                if markable:
                    self.opnum = self.opnum if self.opnum else 1
                    self._mark_items()
                self.opnum = 0

            elif chr(c) == 'M':
                if self.sh > len(self.items):
                    self.sel = int((len(self.items) - 1) / 2)
                else:
                    self.sel = int((self.sh - 1) / 2)

            elif chr(c) == 'L':
                self.opnum = self.opnum if self.opnum else 1
                if self.sh > len(self.items):
                    self.sel = len(self.items) - 1
                else:
                    self.sel = self.sh - 1

                self.sel -= self.opnum - 1
                self.opnum = 0

            elif chr(c) == 'H':
                self.opnum = self.opnum if self.opnum else 1
                self.sel = self.opnum - 1
                self.opnum = 0

            elif c >= ord('0') and c <= ord('9'):
                self.opnum *= 10
                self.opnum += int(chr(c))

            elif c == curses.KEY_RESIZE:
                self._onresize()

            last_char = chr(c)
            self.sh, self.sw = self.scr.getmaxyx()
            self._draw_items()

    def _cleanup(self):
        util.cursesclean()

    def _curses_init(self):
        self.scr = util.cursesinit()

        curses.curs_set(False)
        curses.init_pair(1, self.select_color_fg, self.select_color_bg)
        curses.init_pair(2, self.mark_color_fg, self.mark_color_bg)
        curses.init_pair(3, self.mark_color_fg, self.select_color_bg)

        self.select_colors = curses.color_pair(1)
        self.mark_colors = curses.color_pair(2)
        self.highlight_and_select_colors = curses.color_pair(3)

    def _init(self):
        self._curses_init()

        self.oitems = self.items
        self.sh, self.sw = self.scr.getmaxyx()
        self.sel = 0
        self.first = 0
        self.opnum = 0
        self.marked = set()

    def multi_vend(self, items, display=lambda x: x):
        """Consumes a list of items and allows the user to choose a
           subset of them. Users can mark items using the 'm' key and
           navigate using standard vi bindings (hjkl)."""
        try:
            self.display = display
            self.items = items

            self._init()
            return self._vend(True)
        finally:
            self._cleanup()

    def vend(self, items, display=lambda x: x):
        """Presents a menu which allows the user to select from a list
           of items.  If provided, the display parameter should yield
           a display string for each item in the provided list. If
           display is omitted it is the identity function and the
           provided items are expected to be strings."""

        try:
            self.display = display
            self.items = items

            self._init()
            res = self._vend(False)

            if res == None:
                return None
            return res[0]
        finally:
            self._cleanup()
