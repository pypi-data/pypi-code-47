# -*- coding: utf-8 -*-

from PIL import Image
import os
import requests
from io import BytesIO
import urllib.request


def draw_qrcode(abspath, qrmatrix, qrcolor):
    unit_len = 3
    x = y = 4*unit_len
    pic = Image.new(mode='RGB', size=[
                    (len(qrmatrix)+8)*unit_len]*2, color='#ffffff')
    bg = urllib.request.urlretrieve('http://placehold.it/200x200', 'bg.jpg')
    im = Image.open('bg.jpg').convert('RGB')

    # width = im.width
    # height = im.height
    # for w in range(0, width):
    #     for h in range(0, height):
    #         r, g, b = im.getpixel((w, h))
    #         print(r, g, b)

    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic, x, y, unit_len, qrcolor, im)
            x += unit_len
        x, y = 4*unit_len, y+unit_len

    saving = os.path.join(abspath, 'qrcode.png')
    pic.save(saving)
    return saving


def draw_a_black_unit(p, x, y, ul, color, source):
    for i in range(ul):
        for j in range(ul):
            coord = a, b = x+i, y+j
            pixcolor = source.getpixel(coord)
            print(pixcolor)
            p.putpixel((x+i, y+j), color)
