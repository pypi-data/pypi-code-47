#   Copyright (c) 2019-2020 AnimatedLEDStrip
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.

from client.Animation import *
from client.ColorContainer import ColorContainer
from client.Direction import *


class AnimationData(object):

    def __init__(self):
        self.animation = Animation.COLOR
        self.colors = []
        self.center = -1
        self.continuous = None
        self.delay = -1
        self.delayMod = 1.0
        self.direction = Direction.FORWARD
        self.distance = -1
        self.endPixel = -1
        self.id = ""
        self.spacing = -1
        self.startPixel = 0

    def add_color(self, color):
        if not isinstance(color, ColorContainer):
            raise ValueError("Bad data type: color")
        self.colors.append(color)

    def colors_json(self):
        if len(self.colors) == 0:
            return ""
        else:
            arr_str = ""
            for color in self.colors:
                arr_str = arr_str + color.json() + ","
            return arr_str[:-1]

    def json(self):
        if not isinstance(self.animation, Animation):
            raise ValueError("Bad data type: animation")
        for color in self.colors:
            if not isinstance(color, ColorContainer):
                raise ValueError("Bad data type: color")
        if not isinstance(self.center, int):
            raise ValueError("Bad data type: center")
        if not isinstance(self.continuous, bool) and self.continuous is not None:
            raise ValueError("Bad data type: continuous")
        if not isinstance(self.delay, int):
            raise ValueError("Bad data type: delay")
        if not isinstance(self.delayMod, float):
            raise ValueError("Bad data type: delayMod")
        if not isinstance(self.direction, Direction):
            raise ValueError("Bad data type: direction")
        if not isinstance(self.distance, int):
            raise ValueError("Bad data type: distance")
        if not isinstance(self.endPixel, int):
            raise ValueError("Bad data type: endPixel")
        if not isinstance(self.id, str):
            raise ValueError("Bad data type: id")
        if not isinstance(self.spacing, int):
            raise ValueError("Bad data type: spacing")
        if not isinstance(self.startPixel, int):
            raise ValueError("Bad data type: startPixel")

        return "DATA:{" + '"animation":"{}","colors":[{}],"center":{},"continuous":{},"delay":{},"delayMod":{},' \
                          '"direction":"{}","distance":{},"endPixel":{},"id":"{}","spacing":{},"startPixel":{}' \
            .format(self.animation.name,
                    self.colors_json(),
                    str(self.center),
                    "null" if self.continuous is None else str(
                        self.continuous),
                    str(self.delay),
                    str(self.delayMod),
                    self.direction.name,
                    str(self.distance),
                    str(self.endPixel),
                    self.id,
                    str(self.spacing),
                    str(self.startPixel)
                    ) + "}"
