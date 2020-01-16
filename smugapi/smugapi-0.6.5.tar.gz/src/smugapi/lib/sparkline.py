# -*- coding: utf-8 -*-

# found https://rosettacode.org/wiki/Sparkline_in_unicode#Python

from math import ceil

from pngcanvas import PNGCanvas


# Unicode: 9601, 9602, 9603, 9604, 9605, 9606, 9607, 9608
bar = '▁▂▃▄▅▆▇█'
barcount = len(bar)


def text_sparkline(numbers):
    mn, mx = min(numbers), max(numbers)
    extent = mx - mn
    return ''.join(bar[min([
        barcount - 1, int((n - mn) / extent * barcount)]
        )] for n in numbers)
    return sline


png_colors= dict(
    gray = (0x90, 0x90, 0x90, 0xff),
    red = (0xff, 0, 0, 0xff),
    blue = (0, 0, 0xff, 0xa0),
    green = (0, 0xff, 0, 0xff),
    clear = (0, 0, 0, 0),
    white = (0xff, 0xff, 0xff, 0xff),
)

# take a list of lists and flatten it out
def flatten(lst):
    def fl_(ls):
        for sublist in ls:
            for mem in sublist:
                yield mem
    return list(fl_(lst))


def _draw_series(img, numbers, width, height):
    # just repeat the data elements to be plotted if there are few. this looks
    # better and is easier to read as it fills the width
    if len(numbers) < width/2:
        numbers = flatten(zip(numbers,numbers))
    mn, mx = min(numbers), max(numbers)
    vv = []
    for i,val in enumerate(numbers):
        drawval = height - int(((val - mn)/mx) * height)
        if drawval == 0: drawval = 1
        if drawval == height: drawval -= 1
        vv.append(drawval)
    dv = [ (vv[i],vv[i+1]) for i in range(len(vv)-1)]
    stepwidth = ceil(width / len(dv))
    for i,(y0,y1) in enumerate(dv):
        img.line(stepwidth * i, y0, stepwidth * (i+1), y1)
    return img.dump()


def png_sparkline(numbers, width=60, height=14, color=None, bgcolor='white'):
    if len(numbers) > width: return None
    color = png_colors.get(color) or png_colors.get('blue')
    bgcolor = png_colors.get(bgcolor) or png_colors.get('white')
    img = PNGCanvas(width, height, color=color, bgcolor=bgcolor)
    img.color = color
    _draw_series(img, numbers, width, height)
    return img.dump()

