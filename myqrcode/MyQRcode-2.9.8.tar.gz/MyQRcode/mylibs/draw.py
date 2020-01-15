# -*- coding: utf-8 -*-

from PIL import Image
import os
import requests
from io import BytesIO
import urllib.request


def draw_qrcode(abspath, qrmatrix, qrcolor, qrbg):
    unit_len = 3
    x = y = 4*unit_len
    pic = Image.new(mode='RGB', size=[
                    (len(qrmatrix)+8)*unit_len]*2, color='#ffffff')

    im = qrbg
    
    if qrbg != False :
        bg = urllib.request.urlretrieve(qrbg, 'bg.jpg')
        im = Image.open('bg.jpg').convert('RGB')

    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic, x, y, unit_len, qrcolor, im)
            x += unit_len
        x, y = 4*unit_len, y+unit_len

    saving = os.path.join(abspath, 'qrcode.png')
    pic.save(saving)
    return saving


def draw_a_black_unit(p, x, y, ul, color, bg):
    for i in range(ul):
        for j in range(ul):
            coord = a, b = x+i, y+j
            pixcolor = (0, 0, 0)

            if bg == False:
                pixcolor = color
            else:
                pixcolor = bg.getpixel(coord)
            
            p.putpixel((x+i, y+j), pixcolor)
