from PIL import Image, ImageFont, ImageDraw
from saenews.sae3 import *
from saenews.utils import quote, put_quote


title = "Arise, Awake, stop not till the goal is reached."
tag_line = "(Kathopanishad)"
input_file_orig = "SV.jpg"
in_img = input_file_orig

put_quote(input_file_orig=input_file_orig,
border_dim=0.2,border_dims= (0, 0, 0,0.15), title=title,tag_line='', cord = (0.1,0.886), border_color='red', text_font = '', cap_text_font = '', cap_width=0.055, cap_cord=(0.7,0.866),focus='false')

