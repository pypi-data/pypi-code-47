# -*- coding: utf-8 -*-

"""Module that contains some neat functions to print nice things to terminal.
"""

from typing import List, TextIO

from enum import Enum

from sys import stdout, stderr

from termcolor import colored  # pylint: disable=import-error


QUIET: bool = False
"""Set this to True to shut the mouse of prettyprint. It is not nice but you may need it sometimes.
"""


class Color(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "white"


def prettyprint(text: str, color: Color = Color.WHITE, out: TextIO = stdout, bold=True, dark=False,
                underline=False, blink=False, indent=0, end='\n'):
    """Awesome print.

    Args:
        text (str): your text
        color (Color, optional): color of the text. Default is white.
        out (TextIO, optional): output. Default is stdout.
        bold (bool, optional): print bold text. Default is True.
        dark (bool, optional): print dark text. Default is False.
        underline (bool, optional): underline text. Default is False.
        blink (bool, optional): the text blinks. Default is False.
        indent (int, optional): indentation level. Default is 0. Increase by 2 spaces for each level.
        end (str, optional): end - same as for standard print function. Default is '\n'.
    """

    if QUIET:
        return

    attrs: List[str] = []
    if bold:
        attrs.append("bold")
    if dark:
        attrs.append("dark")
    if underline:
        attrs.append("underline")
    if blink:
        attrs.append("blink")

    print(f"{' ' * 2 * indent}", end='')
    print(colored(text, color.value, attrs=attrs), file=out, end=end)
