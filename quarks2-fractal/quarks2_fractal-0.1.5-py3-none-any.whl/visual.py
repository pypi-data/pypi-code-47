"""visualization scripts
"""
import math
import matplotlib.pyplot as plt 

from PIL import Image
from typing import List

def plot_img_and_labels(img_loc: List[str], pred_prob: List[float], imgs_per_row: int =3):
    """
    """
    pil_images= [Image.open(i) for i in img_loc]
    batches = math.ceil(len(pil_images)/float(imgs_per_row))
    for i in range(batches):
        imgs = pil_images[i*imgs_per_row:(i+1)*imgs_per_row]
        lab = pred_prob[i*imgs_per_row:(i+1)*imgs_per_row]
        fig, ax = plt.subplots(nrows=1, ncols=len(imgs), sharex="col", sharey="row", figsize=(5*(len(imgs)),4), squeeze=False)
        for i, img in enumerate(imgs):    
            ax[0,i].imshow(img)
            ax[0,i].set_title(str(lab[i]))