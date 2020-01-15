import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import torch

import cvt

img = cv.imread('assets/image.jpg')

tfms = cvt.from_file('configs/transform1.json')
img = tfms(img)
plt.imshow(img)
plt.show()