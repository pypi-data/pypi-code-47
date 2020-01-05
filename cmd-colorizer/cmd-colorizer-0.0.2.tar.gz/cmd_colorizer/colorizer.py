# -*- coding: utf-8 -*-
# author: KoChan-s

from colorama import init
import re


class Colorizer(object):
    def __init__(self):
        self.ATTRIBUTES = {"bold": 1, "dark": 2, "underline": 4, "blink": 5, "reverse": 7, "concealed": 8}
        self.COLORS = {"grey": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "magenta": 35, "cyan": 36, "white": 37}
        self.HIGHLIGHTS = {"grey": 40, "red": 41, "green": 42, "yellow": 43, "blue": 44, "magenta": 45, "cyan": 46, "white": 47}
        self.RESET = '\033[0m'

        init() # needed to initialize colors in the cmd (using colorama)

    def colored(self, text, color, on_color, attrs):
        """ colors the text

        :param text: the text that should be colored (str)
        :param color: text color (grey, red, green, yellow, blue, magenta, cyan, white)
        :param on_color: highlights text (grey, red, green, yellow, blue, magenta, cyan, white)
        :param attrs: attributes for text (list)(bold, dark, underline, blink, reverse, concealed)
        """
        self.text = text

        if color:
            if re.match(r"grey|red|green|yellow|blue|magenta|cyan|white", color):
                self.text = f"\033[{self.COLORS[color]}m{self.text}"
            else:
                raise ValueError(f'color "{color}" is incorrect')

        if on_color:
            if re.match(r"grey|red|green|yellow|blue|magenta|cyan|white", on_color):
                self.text = f"\033[{self.HIGHLIGHTS[on_color]}m{self.text}"
            else:
                raise ValueError(f'color "{on_color}" is incorrect')

        if attrs:
            for attr in attrs:
                if re.match(r"bold|dark|underline|blink|reverse|concealed", color):
                    self.text = f"\033[{self.ATTRIBUTES[attr]}m{self.text}"
                else:
                    raise ValueError(f'attribute "{attr}" is incorrect')

        return f"{self.text}{self.RESET}"


color_ = Colorizer()


def colored(text, color=None, on_color=None, attrs=None):
    return color_.colored(text, color, on_color, attrs)
