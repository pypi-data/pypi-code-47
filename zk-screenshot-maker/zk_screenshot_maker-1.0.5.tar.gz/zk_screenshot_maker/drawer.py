#!/usr/bin/env python3
import os
import sys
from PIL import Image, ImageDraw, ImageFont
from theme_info import load_theme_infos, safe_get


def text_horzontal_center(text, color, font, img, screen_width, base_y):
    text_width, text_height = font.getsize(text)
    draw = ImageDraw.Draw(img)
    x = (screen_width-text_width)/2
    y = base_y-text_height
    draw.text((x, y), text, color, font=font)


def draw_title(img, title, title_font):
    screen_width = img.width
    title_y = safe_get(title_font, 'yoff')
    title_font_name = safe_get(title_font, 'font')
    title_font_size = int(safe_get(title_font, 'size'))
    font = ImageFont.truetype(
        brother_path(f"theme/{title_font_name}"),
        title_font_size
    )
    text_horzontal_center(title, "#fff", font, img, screen_width,  title_y)


def draw_bg(img, bg_file):
    bgImg = Image.open(bg_file)
    box = (0, 0,
           min(img.width,  bgImg.width),
           min(img.height, bgImg.height))
    bgImgCrop = bgImg.crop(box)
    img.paste(bgImgCrop, box)


def draw_fg(img, fg_file):
    fgImg = Image.open(fg_file)
    fgImg = fgImg.convert("RGBA")
    boxSrc = (0,
              0,
              min(img.width,  fgImg.width),
              min(img.height, fgImg.height))
    boxDst = (0,
              max(0, img.height-fgImg.height),
              min(img.width,  fgImg.width),
              img.height)

    bgImgCrop = fgImg.crop(boxSrc)
    img.paste(bgImgCrop, boxDst, bgImgCrop)


def draw_screenshot(img, screenshot_file, theme_info):
    ssImg = Image.open(screenshot_file)
    factor = 0.72
    screenshot_info = safe_get(theme_info, "screenshot_info")
    w = int(safe_get(screenshot_info, "width"))
    h = int(safe_get(screenshot_info, "height"))
    yoff = int(safe_get(screenshot_info, "yoff"))
    x = int((img.width - w)/2)
    y = int((img.height - h)/2)+yoff
    box = (x, y,
           x+w,
           y+h)

    device_type = safe_get(theme_info, "device_type")
    screenshot_type = safe_get(screenshot_info, "device_type")
    if device_type == 'iphone65':
        draw_iphone65(img, box)
    elif device_type == 'iphone55':
        draw_iphone55(img, box)
    else:
        draw_pad(img, box)
    draw_screen_edge(img, box)
    ssImg = ssImg.resize((w, h), Image.ANTIALIAS)
    img.paste(ssImg, box)


def draw_iphone65(img, box_screen_of_iphone65):
    '''
        屏幕：
            "width": 1242,
            "height": 2688,
        设备：
            宽度：77.4 毫米 (3.05 英寸) 1388 px
            高度：157.5 毫米 (6.20 英寸) 2825 px
        屏幕对角线 6.5 165.1mm 像素 2961px 17.934585099939431 px/mm
    '''

    x1, y1, x2, y2 = box_screen_of_iphone65
    screen_w = x2-x1
    screen_h = y2-y1
    # device_w = screen_w*1388/1242
    # device_h = screen_h*2825/2688
    device_w = screen_w+80
    device_h = screen_h+80
    draw_device_frame(img, box_screen_of_iphone65,
                      (device_w, device_h))


def draw_iphone55(img, box_screen_of_iphone55):
    '''
    1、长×宽×高：158.1毫米 × 77.8毫米× 7.1毫米；2493x1227
    2、5.5英寸Retina HD高清显示屏，1920x1080像素分辨率；
    5.5英寸=139.7mm  2203px 15.768841589708649 px/mm
    '''
    x1, y1, x2, y2 = box_screen_of_iphone55
    screen_w = x2-x1
    screen_h = y2-y1
    device_w = screen_w*1227/1080
    device_h = screen_h*2493/1920
    # device_w = screen_w+80
    # device_h = screen_h+160
    draw_device_frame(img, box_screen_of_iphone55,
                      (device_w, device_h))


def draw_pad(img, box_screen_of_pad):
    '''
    一个iPad的屏幕120mm*160mm，外壳135mm*200mm
    '''
    x1, y1, x2, y2 = box_screen_of_pad
    screen_w = x2-x1
    screen_h = y2-y1
    device_w = screen_w*135/120
    device_h = screen_h*200/160

    draw_device_frame(img, box_screen_of_pad,
                      (device_w, device_h))


def draw_device_frame(img, box_screen, device_size):
    device_w, device_h = device_size

    screenshot_edg = 2
    pad_fill = "#DDBB99"
    pad_edg1 = "#CCB097"
    pad_edg2 = "#BEA286"
    screen_x1, screen_y1, screen_x2, screen_y2 = box_screen
    screen_w = screen_x2 - screen_x1
    screen_h = screen_y2 - screen_y1
    off_x = (device_w-screen_w)/2
    off_y = (device_h-screen_h)/2

    device_x1 = screen_x1-off_x
    device_y1 = screen_y1-off_y
    device_x2 = screen_x2+off_x
    device_y2 = screen_y2+off_y

    draw = ImageDraw.Draw(img)
    draw.rectangle((device_x1 - screenshot_edg,
                    device_y1 - screenshot_edg,
                    device_x2, device_y2),
                   pad_edg1)

    draw.rectangle((device_x1, device_y1,
                    device_x2 + screenshot_edg,
                    device_y2 + screenshot_edg),
                   pad_edg2)

    draw.rectangle((device_x1, device_y1, device_x2, device_y2), pad_fill)


def draw_screen_edge(img, box_screen):
    width_edg = 2
    screen_edg1 = "#CCAA88"
    screen_edg2 = "#BB9977"
    screen_x1, screen_y1, screen_x2, screen_y2 = box_screen
    draw = ImageDraw.Draw(img)
    draw.rectangle((screen_x1 - width_edg,
                    screen_y1 - width_edg,
                    screen_x2,
                    screen_y2),
                   screen_edg1)
    draw.rectangle((screen_x1,
                    screen_y1,
                    screen_x2 + width_edg,
                    screen_y2 + width_edg),
                   screen_edg2)


def make_screenshot(screenshot_info, theme_info, screenshot_index):
    width = safe_get(theme_info, "width")
    height = safe_get(theme_info, "height")
    device_type = safe_get(theme_info, "device_type")
    screen_shot_yoff = safe_get(safe_get(theme_info, "screen_shot"), "yoff")
    bg = safe_get(theme_info, "bg")
    fg = safe_get(theme_info, "fg")
    fg_frame = safe_get(fg[0], "frame")
    title_font = safe_get(theme_info, "title")
    sub_title_font = safe_get(theme_info, "sub_title")
    title = safe_get(screenshot_info, "title")
    sub_title = safe_get(screenshot_info, "sub_title")

    index = screenshot_index % len(bg)
    bg_file = brother_path(f"theme/{bg[index]}")
    fg_file = brother_path(f"theme/{fg_frame}")
    screenshot_dir = safe_get(screenshot_info, "screenshot_dir")
    screenshot_file = safe_get(screenshot_info, "screenshot_path")

    img = Image.new('RGB', (width, height), "#3399ff")
    draw_bg(img, bg_file)
    draw_screenshot(img, screenshot_file, theme_info)
    draw_title(img, title, title_font)
    draw_title(img, sub_title, sub_title_font)
    draw_fg(img, fg_file)
    path, filename = os.path.split(screenshot_file)
    name, ext = os.path.splitext(filename)
    file_dir = os.path.join(screenshot_dir, 'output', device_type)
    file_path = os.path.join(screenshot_dir, 'output',
                             device_type, f'{name}.png')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    img.save(file_path, 'PNG')
    print(
        f"""
------------------------------------
GEN:
    {file_path}
WITH:
    {screenshot_file}
    theme_type:{device_type}
    size:({width}x{height})
    """)


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)
