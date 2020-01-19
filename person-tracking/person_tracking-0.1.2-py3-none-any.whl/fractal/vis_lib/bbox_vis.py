import torch
from PIL import Image, ImageDraw, ImageFont 
import colorsys
import torch
import numpy as np 
import os
from remo.utils import yxyx_yxhw
import matplotlib.pyplot as plt
from matplotlib import patches

__all__ = ["Img_with_labels", "Img_with_grid", "Img_with_obj_ctr", "Img_obj_ctr_grid", "Img_obj_ctr_grid_boxes"]

def Img_with_labels(img, bboxes, labels, labels_mapping, save_loc=None, path="./"):
    """ Outputs an image with bounding boxes and labels 
    
    img: A PIL image. 
    bboxes: numpy array: [N, 4] [y1, x1, y2, x2]
    lables: numpy array: [N]
    labels_mapping: dict
    
    Returns a PIL image
    """
    image = img.copy()
    hsv_tuples = [(x/(len(labels_mapping)+5), 1., 1.) for x in range(len(labels_mapping)+5)]
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(map(lambda x: (int(x[0]*255), int(x[1]*255), int(x[2]*255)), colors))
    
    font = ImageFont.truetype(font=path+"/FiraMono-Medium.otf",
                             size=np.floor(1e-1 * (image.size[1]+0.5)/2).astype("int32"))
    thickness = (image.size[0]+image.size[1]) // 600
    
    for i, c in enumerate(labels):
        box = bboxes[i]
        label = '{}'.format(labels_mapping[c])
        draw = ImageDraw.Draw(image)
        label_size = draw.textsize(label, font)
        
        ymin, xmin, ymax, xmax = box
        bottom = ymax
        top = ymin
        left = xmin
        right = xmax

        if top - label_size[1] >=0:
            text_origin = np.array([left, top-label_size[1]])
        else:
            text_origin = np.array([left, top+1])

        for i in range(thickness):
            draw.rectangle(
            [left+i, top+i, right-i, bottom-i], outline=colors[c])

        draw.rectangle([tuple(text_origin), tuple(text_origin+label_size)], fill=colors[c])
        draw.text(text_origin, label, fill=(0, 0, 0), font=font)
        del draw
    
    if save_loc is not None:
        image.save(save_loc, quality=90)
    else:
        return image
    
def Img_with_grid(img, grid=(32, 32)):
    """ Outputs a PIL image with grid
    
    img: PIL image 
    grid: tuple. The size of the grid. (h, w)
    """
    image = img.copy()
    
    h = image.size[1]//grid[0]
    w = image.size[0]//grid[1]
    
    hlines = np.array([[0, h+n*h, image.size[1], h+n*h] for n in range(image.size[1]//h)])
    vlines = np.array([[w+n*w, 0, w+n*w, image.size[0]] for n in range(image.size[0]//w)])
    
    for i in hlines:
        draw = ImageDraw.Draw(image)
        draw.line([i[0], i[1], i[2], i[3]], fill="red", width=2)
        del draw 
    
    for i in vlines:
        draw = ImageDraw.Draw(image)
        draw.line([i[0], i[1], i[2], i[3]], fill="red", width=2)
        del draw 
    
    return image

def Img_with_obj_ctr(img, bboxes, labels, labels_mapping):
    """Outputs Image with object centers
    
    img: PIL image 
    bboxes: numpy array [N, 4] [x_ctr, y_ctr, h, w]
    labels: numpy array [N, 1] 
    labels_mapping: A dict with keys as numbers and values as labels
    """
    
    image = img.copy()
    hsv_tuples = [(x/(len(labels_mapping)+5), 1., 1.) for x in range(len(labels_mapping)+5)] #+5 is hardcoded
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(map(lambda x: (int(x[0]*255), int(x[1]*255), int(x[2]*255)), colors))
    r = (image.size[0]+image.size[1]) // 600
    
    for c, i in enumerate(bboxes):
        label = labels[c]
        draw = ImageDraw.Draw(image)
        x, y = i[1], i[0]
        draw.ellipse([x-r, y-r, x+r, y+r], fill=colors[label])
        del draw
        
    return image

def Img_obj_ctr_grid(img, bboxes, labels, labels_mapping, grid=(32, 32)):
    """ Combining Img_with_obj_ctr and Img_with_grid
    
    img: PIL image 
    bboxes: numpy array [N, 4]
    labels: numpy array [N, 1] 
    labels_mapping: A dict with keys as numbers and values as labels
    grid: tuple. The size of the grid. (h, w)
    """
    image = img.copy()
    image = Img_with_grid(image, grid)
    box = yxyx_yxhw(bboxes)
    image = Img_with_obj_ctr(image, box, labels, labels_mapping)
    return image


def Img_obj_ctr_grid_boxes(img, bboxes, labels, labels_mapping, grid=(32, 32), path="./", save_loc=None):
    """ Combining Img_with_obj_ctr and Img_with_grid
    
    img: PIL image 
    bboxes: numpy array [N, 4]
    labels: numpy array [N, 1] 
    labels_mapping: A dict with keys as numbers and values as labels
    grid: tuple. The size of the grid. (h, w)
    """
    image = img.copy()
    image = Img_with_grid(image, grid)
    box = yxyx_yxhw(bboxes)
    image = Img_with_obj_ctr(image, box, labels, labels_mapping)
    image = Img_with_labels(image, bboxes, labels, labels_mapping, save_loc, path)
    return image


def draw_bounding_boxes(image, bbox, line_color="blue", linewidth=2, figsize=(30, 20), fill=None):
    fig = plt.figure(figsize=figsize)
    ax = fig.subplots(1)
    ax.imshow(image)
    for i in bbox:
        top = i[0]
        left = i[1]
        height = i[2]
        width = i[3]
        rect = patches.Rectangle([left, top], width, height, fill=fill)
        ax.add_patch(rect)
    plt.show()
    return ax 

def draw_grid(image, bbox, outline="white"):
    draw = ImageDraw.Draw(image)
    for i in bbox:
        y0, x0, y1, x1 = i
        draw.rectangle([x0, y0, x1, y1], outline=outline)
    return image