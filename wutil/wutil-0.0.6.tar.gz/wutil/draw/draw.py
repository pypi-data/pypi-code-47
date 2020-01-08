import cv2
from matplotlib import colors as color_names


def color_name_to_bgr(color_name):
    r, g, b = color_names.to_rgb(color_name)
    return int(b * 255), int(g * 255), int(r * 255)


def draw_outlined_text(im, text, pos, font_size, font_color, font_thickness=1):
    cv2.putText(im, text, pos, cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 0), font_thickness+1)
    cv2.putText(im, text, pos, cv2.FONT_HERSHEY_SIMPLEX, font_size, color_name_to_bgr(font_color), font_thickness)
