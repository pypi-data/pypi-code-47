""" Datagenerator to train the model

The list file looks like this

img.jpg xmin ymin xmax ymax label xmin ymin xmax ymax label .....
"""
import os
import sys
import random
import numpy as np

import torch
import torch.utils.data as data
import torchvision.transforms as transforms

from PIL import Image
#import cv2
from ..anchors import get_anchors
from person_tracking.fractal.loaders.bbox_transforms import resize, random_flip, random_crop, center_crop, random_distort_image
from person_tracking.fractal.anchors.utils import xyxy_xywh
# from fractal.loaders.bbox_transforms import resize, random_flip, random_crop, center_crop, random_distort_image
# from fractal.anchors.utils import xyxy_xywh

def size_setter(seen, batch_size):
    if seen < 2000*batch_size:
        input_size = 13*32
    elif seen < 4000*batch_size:
        input_size = (random.randint(0, 3) + 13)*32
    elif seen < 8000*batch_size:
        input_size = (random.randint(0, 5)+12)*32
    elif seen < 12000*batch_size:
        input_size = (random.randint(0, 7) + 11)*32
    else:# self.seen < 20000*self.opt.batch_size:
        input_size = (random.randint(0, 9)+10)*32
    return input_size


class ListDataset(data.Dataset):
    def __init__(self, cfg, train, input_size, encode_box=True, debugger=False, multi_scale=False):
        '''
        Important Args:
          root: (str) ditectory to images.
          list_file: (str) path to index file.
          train: (boolean) train or test.
          transform: ([transforms]) image transforms.
          input_size: (int) model input size.
        '''
        self.cfg = cfg
        self.train = train
        if self.train:
            list_file = self.cfg["data"]["train_data"]
        else:
            list_file = self.cfg["data"]["valid_data"]
        self.cfg = cfg
        self.input_size = input_size
        self.multi_scale = multi_scale

        self.fnames = []
        self.boxes = []
        self.labels = []
        self.transform = transforms.Compose([transforms.ToTensor()])

        self.encode_box = encode_box
        self.debugger=debugger
        self.seen = 0

        with open(list_file) as f:
            lines = f.readlines()
            self.num_samples = len(lines)

        for line in lines:
            splited = line.strip().split()
            self.fnames.append(splited[0])
            num_boxes = (len(splited) - 1) // 5
            box = []
            label = []
            for i in range(num_boxes):
                ymin = splited[1+5*i]
                xmin = splited[2+5*i]
                ymax = splited[3+5*i]
                xmax = splited[4+5*i]
                c = splited[5+5*i]
                box.append([float(ymin),float(xmin),float(ymax),float(xmax)])
                label.append(int(c))
            self.boxes.append(torch.Tensor(box))
            self.labels.append(torch.LongTensor(label))

    def __getitem__(self, idx):
        '''Load image.
        Args:
          idx: (int) image index.
        Returns:
          img: (tensor) image tensor.
          loc_targets: (tensor) location targets.
          cls_targets: (tensor) class label targets.
        '''
        # Load image and boxes.
        if self.multi_scale:
            if self.train and idx%self.cfg["train"]["batch_size"] == 0:
                self.input_size = size_setter(self.seen, self.cfg["train"]["batch_size"])
                
        self.seen += 1
        fname = self.fnames[idx]
        #print(fname)
        #os.path.join(self.root, fname)
        img = Image.open(self.cfg["data"]["data_loc"]+fname)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        boxes = self.boxes[idx].clone()

        labels = self.labels[idx]
        size = self.input_size
        
        if self.debugger:
            print("reading file:",  fname)
            print("labels:", labels)
            print("size:", size)

        # Data augmentation.
        if self.train:
            img, boxes = random_flip(img.copy(), boxes.clone())
            #img, boxes = random_crop(img, boxes)
            #print(boxes)
            img, boxes = resize(img.copy(), (self.input_size, self.input_size), boxes.clone())
            img = random_distort_image(img.copy(), self.cfg["train"]["hue"], self.cfg["train"]["saturation"], self.cfg["train"]["exposure"])
        else:
            img, boxes = resize(img, (self.input_size, self.input_size), boxes.clone())
            #img, boxes = center_crop(img, boxes, (size, size))

        img = self.transform(img)
        #print(boxes)
        #print(labels)
        if self.encode_box:
            fill_boxes = torch.zeros((500, 5))
            _, h, w = img.size()
            #print("boxes:", boxes)
            boxes = xyxy_xywh(boxes[:, [1, 0, 3, 2]], 0.5) #ctr_x, ctr_y, w, h
            #print(boxes.shape)
            #print("boxes:", boxes)
            boxes = torch.cat([labels.view(-1, 1).float(), boxes], 1)
            fill_boxes[:boxes.shape[0], :] = boxes
            return img, fill_boxes
        else:
            return img, boxes

    def __len__(self):
        return int(self.cfg["data"]["total_images"]/self.cfg["train"]["batch_size"]) * self.cfg["train"]["batch_size"]    
    @staticmethod
    def prep_image(img_loc, inp_dim):
        """
        Prepare image for inputting to the neural network. 

        Returns a Variable 
        
        img_loc: str: Location of the image
        inp_dim: tuple: resize dimension. The aspect ratio is not taken care off.
        """
        img = Image.open(img_loc)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        shape = (img.size[1], img.size[0]) #(h, w)
        
        img_, _ = resize(img, inp_dim)
        img_tensor = transforms.ToTensor()(img_)
        img_tensor = img_tensor.unsqueeze(0)
        return img, img_tensor, shape

if __name__ == '__main__':
    import torchvision.transforms as transforms
    transform = transforms.Compose([transforms.ToTensor()])
