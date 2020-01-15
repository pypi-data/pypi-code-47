from cvt.transform import (RandomBright, RandomContrast, RandomHorizontalFlip,
                           RandomHue, RandomRotation, RandomVerticalFlip,
                           Sample, Sequence, Shuffle)

tfms = Sequence([
    Sample([RandomBright(0.2), RandomContrast(0.2), RandomHue(0.2)]),
    Shuffle([RandomHorizontalFlip(), RandomVerticalFlip(), RandomRotation(30)])
])

import cv2 as cv 
img = cv.imread('test/assets/001.jpg')[:,:,[2,1,0]]
data = {'image':img}
data = tfms(data)
import matplotlib.pyplot as plt
plt.imshow(data['image'])
plt.show()