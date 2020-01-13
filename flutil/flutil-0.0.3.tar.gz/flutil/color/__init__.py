"""Package for easy color handling."""
from typing import Union, Iterable
from matplotlib import colors
from .xkcd import XKCD_COLS
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HEX_SYMS = ['0', '1', '2', '3',
            '4', '5', '6', '7',
            '8', '9', 'a', 'b',
            'c', 'd', 'e', 'f']


class Color:
    def __init__(self, color: Union[str, int, Iterable],
                 alpha=None,
                 hsv=False):
        """
        :param Union[str, int, Iterable] color: a color that can be given as:

        - an RGB or RGBA tuple of int values in [0, 255] (e.g., (128, 55, 30));
        - an RGB or RGBA tuple of float values in [0, 1] (e.g., (0.1, 0.2, 0.5)
        or (0.1, 0.2, 0.5, 0.3));
        - a hex RGB or RGBA string (e.g., '#0f0f0f', '#0f0f0f80', or '0f0f0f';
        case-insensitive);
        - a CSS-like 3- or 4-char RGB hex string (e.g. '#f0f', '#f0f8', or
        'f0e')
        - a string representation of a float value in [0, 1] inclusive for gray
        level (e.g., '0.5');
        - one of {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'};
        - a name from the xkcd color survey, (e.g., 'sky blue'; case
        insensitive);
        :param float alpha: (optional) when given, this alpha overrides the
        alpha from the `color` arg
        :param bool hsv: (optional) interpret the color as HSV instead of RGB.
        Only relevant when `color` is given as a tuple.
        """
        if isinstance(color, str):
            color2 = color.replace('#', '')
            if all(c.lower() in HEX_SYMS for c in color2):
                # Probably a hex string
                if len(color2) == 6 or len(color2) == 8:
                    # RGB(A) hex string
                    color = f'#{color2}'
                elif len(color2) == 3 or len(color2) == 4:
                    # CSS hex string like fff that should be turned into ffffff
                    # Just repeat each character
                    color = ''.join([c for c in color2
                                     for _ in range(2)])
                    color = f'#{color}'
            elif color in XKCD_COLS:
                # xkcd color
                color = f'xkcd:{color}'

        elif isinstance(color, Iterable):
            if all(isinstance(c, int) and c >= 0 for c in color):
                color = tuple(c/255 for c in color)
            elif hsv:
                color = tuple(colors.hsv_to_rgb([color[0]/360, *color[1:]]))

        self._rgba = colors.to_rgba(color)
        if alpha:
            self._rgba = tuple([*self._rgba[:-1], alpha])
            if not colors.is_color_like(self._rgba):
                raise ValueError('Alpha should be a float in range [0, 1]')

    @property
    def alpha(self):
        """The alpha of the color."""
        return self.rgba[-1]

    @alpha.setter
    def alpha(self, value):
        self._rgba = tuple([*self._rgba[:-1], value])

    @property
    def rgb(self):
        """Color as int RGB tuple in range [0, 255]."""
        return tuple(int(c*255)
                     for c in colors.to_rgb(self._rgba))

    @property
    def rgb2(self):
        """Color as float RGB tuple in range [0, 1]."""
        return tuple(colors.to_rgb(self._rgba))

    @property
    def rgba(self):
        """Color as int RGB tuple in range [0, 255]."""
        return tuple([*self.rgb, self._rgba[-1]])

    @property
    def rgba2(self):
        """Color as float RGB tuple in range [0, 1]."""
        return self.rgba

    @property
    def hex(self):
        if self._rgba[-1] == 1:
            return colors.to_hex(self._rgba)
        else:
            return colors.to_hex(self._rgba, keep_alpha=True)

    @property
    def hsv(self):
        """
        Color as float HSV tuple with:
            - Hue in range [0, 360)
            - Saturation in range [0, 1]
            - Value in range [0, 1]
        """
        hsv = colors.rgb_to_hsv(self._rgba[:-1])
        return tuple([
            hsv[0]*360,  # Hue
            hsv[1],      # Saturation
            hsv[2],      # Value
        ])

    @property
    def hsv2(self):
        """
        Color as float HSV tuple with:
            - Hue in range [0, 1]
            - Saturation in range [0, 1]
            - Value in range [0, 1]
        """
        return tuple(colors.rgb_to_hsv(self._rgba[:-1]))

    def __repr__(self):
        return (self.hex)

    @staticmethod
    def from_hsv(hue: float, saturation: float, value: float):
        """Return a `Color` instance from hue, saturation and value

        :param hue: the hue; in range [0, 360)
        :param saturation: the saturation; in range [0, 1]
        :param value: the value/brightness; in range [0, 1]
        """
        return Color((hue, saturation, value), hsv=True)

    def to_patch(self):
        """Return the color as a colored Circle patch."""
        return Circle((0, 0), radius=1, fc=self._rgba, ec=None)

    def show(self):
        """Show the color as a matplotlib Figure"""
        fig, ax = plt.subplots(figsize=(1, 1))
        ax.add_patch(self.to_patch())
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_axis_off()
        return fig
