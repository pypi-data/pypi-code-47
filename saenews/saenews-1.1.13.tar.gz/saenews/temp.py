from PIL import Image, ImageFont, ImageDraw
import cv2
from saenews.sae2 import sae2
import datetime
from saenews.sae3 import *
import os
from saenews.utils import quote

def add_border(input_image, output_image, border, border_color='black'):
    img = Image.open(input_image) 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=border_color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    bimg.save(output_image)
    print (output_image)

def put_quote(border_dim=0.2,*args, **kwargs):
    bottom_factor = border_dim
    in_img = input_file
    img = Image.open(in_img)
    W,H = img.size
    add_border(in_img,
               output_image='bordered.jpg',
               border=(0, 0, 0,round(W*bottom_factor)))
    quote(input_file='bordered.jpg', *args,**kwargs)
    
    
    
    


title = "Arise, Awake, stop not till the goal is reached."
tag_line = "(Kathopanishad)"
input_file_orig = "SV.jpg"
put_quote(border_dim=0.3,title=title,tag_line=tag_line,input_file_orig=input_file, cord = (0.03,0.766), border_color='red', text_font = '', cap_text_font = '', cap_width=0.055, cap_cord=(0.7,0.866), border_width=0)

