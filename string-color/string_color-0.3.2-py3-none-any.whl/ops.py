import json
import os

class String:
    "A regular string"
    def __init__(self, string):
        self.string = string

    def render(self):
        return self.string

    def bold(self):
        return Bold(str(self))

    def cs(self, color, bkg=None):
        return Color(str(self), color, bkg)

    def underline(self):
        return Underline(str(self))

    def __str__(self):
        return self.render()

    def concatenate(self, other, order=None):
        """ shared logic for __add__() and __radd__()"""
        types = [int, float, type(open)]
        if type(other) in types:
            raise TypeError('Cannot concat ' + ', '.join([str(t) for t in types]))
        try:
            other = str(other)
            if order == "reverse":
                return other + self.render()
            else:
                return self.render() + other
        except Exception:
            raise TypeError(f"Cannot concat {type(other)}")

    def __add__(self, other):
        return self.concatenate(other)

    def __radd__(self, other):
        return self.concatenate(other, "reverse")

class Bold(String):
    "Make string bold"
    def render(self):
        return f"\033[1m{self.string}\033[0m"


def _load_colors():
    colors_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'colors.json'
    )
    with open(colors_path) as f:
        colors = json.loads(f.read())
    return colors


class Color(String):
    "Color a string"
    colors = _load_colors()

    def __init__(self, string, color, bkg=None):
        self.string = string
        self.color = color
        self.bkg = bkg

    def render(self):
        """color a string"""
        ret = False
        bkg_term = None
        if self.bkg is not None:
            for key, value in self.colors.items():
                if (self.bkg.lower() == value["name"].lower() or
                        self.bkg == value["hex"] or
                        self.bkg == value["term"]):
                    bkg_term = value["term"]
                    break
        for key, value in self.colors.items():
            if (self.color.lower() == value["name"].lower() or
                    self.color == value["hex"] or
                    self.color == value["term"]):
                ret = True
                if bkg_term:
                    return f"\033[38;5;{value['term']};48;5;{bkg_term}m{self.string}\033[0m"
                else:
                    return f"\033[38;5;{value['term']}m{self.string}\033[0m"
                break
        if not ret:
            return self.string


class Underline(String):
    "Underline a string"
    def render(self):
        return f"\033[4m{self.string}\033[0m"
