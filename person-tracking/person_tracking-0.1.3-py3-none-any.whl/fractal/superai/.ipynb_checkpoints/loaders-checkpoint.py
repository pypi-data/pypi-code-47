import torch
import numpy as np
from PIL import Image
from tqdm import tqdm 
import os
import pickle

from torchvision import transforms

from .img_transforms import MyResizer, Normalizer

class ListDataset():
    def __init__(self,
                 opt,
                 train=True):
        self.opt = opt
        self.train = train
        self.multiclass = self.opt.multiclass
        #self.aspect_loc = self.opt.aspect_loc
        if self.multiclass:
            from sklearn.preprocessing import MultiLabelBinarizer
            self.one_hot = MultiLabelBinarizer(classes=np.arange(self.opt.num_classes))
        if self.train:
            self.list_file = self.opt.train_data_loc
        else:
            self.list_file = self.opt.val_data_loc
            
        
        self.input_size = self.opt.input_size
        self.data_loc = self.opt.data_loc
        
        
        if self.train:
            self.transforms = ListDataset.train_transformations(self.opt)
        else:
            self.transforms = ListDataset.test_transformations(self.opt)
        self.images, self.labels = [], []

        with open(self.list_file) as f:
            lines = f.readlines()
            self.num_samples = len(lines)

        for line in lines:
            splited = line.strip().rsplit(" ")
            self.images.append(splited[0])
            if self.multiclass:
                self.labels.append([int(i) for i in splited[1:]])
            else:
                self.labels.append(torch.LongTensor([int(splited[1])]))
        print("images:", len(self.images))
        
    def __getitem__(self, idx):
        img_loc = self.images[idx]
        label = self.labels[idx]
        img = self.get_image(img_loc)
        if self.multiclass:
            label = torch.FloatTensor(self.one_hot.fit_transform([label])).view(-1)
        else:
            label = label.long()
        return img, label, img_loc

    def __len__(self):
        return len(self.images)

    def get_image(self, img_loc):
        img = Image.open(self.data_loc+img_loc)
        if img.mode != self.opt.input_space:
            img = img.convert(self.opt.input_space)
        #img = np.asarray(img)
        img = self.transforms(img)
        return img

    def inverse_image(self):
        pass ## Given torch output tensor output of a dataloader, this should reverse engineer the options and output another image.
        
    @staticmethod
    def train_transformations(opt):
        img_transforms = []
        
        if opt.rotation:
            img_transforms.append(transforms.RandomRotation(2))
        if opt.h_flip:
            img_transforms.append(transforms.RandomHorizontalFlip())
        if opt.v_flip:
            img_transforms.append(transforms.RandomVerticalFlip())
        if opt.hue > 0 or opt.saturation > 0 or opt.contrast > 0 or opt.brightness >0:
            img_transforms.append(transforms.ColorJitter(brightness=opt.brightness,
                                             contrast=opt.contrast,
                                             saturation=opt.saturation,
                                             hue=opt.hue))
        if opt.pad:
            img_transforms.append(transforms.ToTensor())
            m = torch.nn.ReflectionPad2d((4,4,4,4))
            img_transforms.append(transforms.Lambda(lambda x: m(x.unsqueeze(0)).data.squeeze()))
            img_transforms.append(transforms.ToPILImage())
        if isinstance(opt.input_size, tuple):
            input_size = opt.input_size[0]
        else:
            input_size = opt.input_size
        if opt.resize:
            img_transforms.append(transforms.Resize((input_size, input_size)))
        img_transforms.append(transforms.ToTensor())
        
        if opt.normalize:
            img_transforms.append(transforms.Normalize(opt.mean, opt.std))
        
        return transforms.Compose(img_transforms)
    
    @staticmethod
    def test_transformations(opt):
        img_transforms = []
        
        if isinstance(opt.input_size, tuple):
            input_size = opt.input_size[0]
        else:
            input_size = opt.input_size
        
        if opt.use_tencrop:
            if opt.resize:
                img_transforms.append(transforms.Resize(input_size))
            img_transforms.append(transforms.TenCrop(input_size))
            img_transforms.append(transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])))
            if opt.normalize:
                img_transforms.append(transforms.Lambda(lambda crops:torch.stack([transforms.Normalize(opt.mean, opt.std)(crop) for crop in crops])))
        else:
            if opt.resize:
                img_transforms.append(transforms.Resize((input_size, input_size)))
            img_transforms.append(transforms.ToTensor())
            if opt.normalize:
                img_transforms.append(transforms.Normalize(opt.mean, opt.std))
            
        return transforms.Compose(img_transforms)
