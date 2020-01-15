# -*- coding: utf-8 -*-

from PIL import Image
import os
import requests
from io import BytesIO


def draw_qrcode(abspath, qrmatrix, qrcolor):
    unit_len = 3
    x = y = 4*unit_len
    pic = Image.new(mode='RGB', size=[
                    (len(qrmatrix)+8)*unit_len]*2, color='#ffffff')
    response = requests.get('http://placehold.it/200x200')
    bg = Image.open(BytesIO(response.content))

    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic, x, y, unit_len, qrcolor, bg)
            x += unit_len
        x, y = 4*unit_len, y+unit_len

    saving = os.path.join(abspath, 'qrcode.png')
    pic.save(saving)
    return saving


def draw_a_black_unit(p, x, y, ul, color, background):
    for i in range(ul):
        for j in range(ul):
            pixcolor = background.getpixel(x+i, y+j)
            p.putpixel((x+i, y+j), color)
