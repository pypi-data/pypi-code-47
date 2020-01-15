import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import torch

import cvt

img = cv.imread('assets/image.jpg')
mask = cv.imread('assets/mask.png')
data = {'image':img, 'mask':mask}

tfms = cvt.from_file('configs/transform1.json')
data = tfms(data)
plt.imshow(data['image'])
plt.show()
plt.imshow(data['mask'])
plt.show()


img = cv.imread('assets/image.jpg')
mask = cv.imread('assets/mask.png')
data = {'image':img, 'mask':mask}

tfms = cvt.from_file('configs/transform2.json')
data = tfms(data)
print('data:', data['image'].shape, type(data['image']))
print('mask:', data['mask'].shape, type(data['mask']))
print('mask:', data['mask'].unique())