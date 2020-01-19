import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import colorsys

from PIL import Image, ImageFont, ImageDraw
from ..anchors.utils import xywh_xyxy

## printing a few bounding boxes

def draw_grid(image, bbox, outline="white", input_format="xyxy"):
    """draws rectangles on the image given by bbox 
    
    image: PIL image 
    bbox: numpy with each box representing the format defined by "format"
    outline: color of the bbox 
    input_format: "xxyy" or "xyhw": use one of this 
    
    """
    draw = ImageDraw.Draw(image)
    if input_format == "xywh":
        bbox = xywh_xyxy(bbox)
    
    if isinstance(bbox, torch.Tensor):
        bbox = bbox.numpy()
        
    for i in bbox:
        x0, y0, x1, y1 = i
        draw.rectangle([x0, y0, x1, y1], outline=outline)
    return image

def draw_centre(image, bbox, outline="white", input_format="xyxy"):
    r = (image.size[0]+image.size[1])//600
    print(r)
    draw = ImageDraw.Draw(image)
    
    if input_format == "xywh":
        bbox = xywh_xyxy(bbox)
    
    if isinstance(bbox, torch.Tensor):
        bbox = bbox.numpy()
    
    for i in bbox:
        x0, y0, x1, y1 = i
        x_ctr = (x1+x0)/2
        y_ctr = (y1+y0)/2
        draw.ellipse([x_ctr-r, y_ctr-r, x_ctr+r, y_ctr+r], outline=outline)
    return image


def vis_bbox(image, bbox, color="red"):
    """ Randomly plots every 20th anchor box

    image = np.zeros((800, 600, 3)).astype(np.uint8)
    bbox = anchor[index_inside, :]
    """
    print(image.shape)
    fig = plt.figure(figsize=(416//52, 416//52))
    ax = fig.subplots(1)
    ax.imshow(image)
    for m, i in enumerate(bbox):
        xmin, ymin, xmax, ymax = i
        height = ymax - ymin
        width = xmax - xmin

        if np.random.randint(0, 20) ==0:
            rect = patches.Rectangle([xmin, ymin], width, height, color = color, fill=False)
            ax.add_patch(rect)
    plt.show()


def vis_bbox_inference(image, bbox, color="red"):
    """ Plots all the anchor boxes. No randomness involved
    image = np.zeros((800, 600, 3)).astype(np.uint8)
    bbox = anchor[index_inside, :]
    """
    print(image.shape)
    fig = plt.figure(figsize=(416//52, 416//52))
    ax = fig.subplots(1)
    ax.imshow(image)
    for m, i in enumerate(bbox):
        xmin, ymin, xmax, ymax = i
        height = ymax - ymin
        width = xmax - xmin
        rect = patches.Rectangle([xmin, ymin], width, height, color = color, fill=False)
        ax.add_patch(rect)
    plt.show()


def save_img_with_labels(image, bboxes, prob_scores, labels, labels_mapping, save_loc="pred_img.png",
                        font_loc="fractal/vis_lib/FiraMono-Medium.otf"):
    """saves the image to input location

    image: Input PIL image
    bboxes: bounding boxes of the image. ndarray [N, 4]
    prob_scores: prob_scores of the boxes. ndarray [N,]
    labels: labels for the box . ndarray [N,]
    labels_mapping: mapping of the labels dict example: {1:"person", 2: "box"}
    save_loc: location to save the image

    Returns:
    save the PIL image at given location if save_loc is not None, else outputs a PIL image with bboxes
    """
    hsv_tuples = [(x/len(labels_mapping), 1., 1.) for x in range(len(labels_mapping))]
    colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
    colors = list(map(lambda x: (int(x[0]*255), int(x[1]*255), int(x[2]*255)), colors))

    font = ImageFont.truetype(font=font_loc, size=np.floor(3e-2 * image.size[1]+0.5).astype("int32"))
    thickness = (image.size[0]+image.size[1]) // 300

    for i, c in enumerate(labels):
        predicted_class = labels_mapping[c]
        box = bboxes[i]
        score = prob_scores[i]

        label = '{} {:.2f}'.format(predicted_class, score)

        draw = ImageDraw.Draw(image)

        label_size = draw.textsize(label, font)
        
        xmin, ymin, xmax, ymax = box
        #ymin, xmin, ymax, xmax = box
        bottom = int(ymax)
        top = int(ymin)
        left = int(xmin)
        right = int(xmax)

        if top - label_size[1] >=0:
            text_origin = np.array([left, top-label_size[1]])
        else:
            text_origin = np.array([left, top+1])
        
        for i in range(thickness):
            draw.rectangle(
            [left+i, top+i, right-i, bottom-i], outline=colors[int(c)])

        draw.rectangle([tuple(text_origin), tuple(text_origin+label_size)], fill=colors[int(c)])
        draw.text(text_origin, label, fill=(0, 0, 0), font=font)
        del draw

    if save_loc is not None:
        image.save(save_loc, quality=90)
    else:
        return image