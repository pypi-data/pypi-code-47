import torch
import numpy as np 
import skimage
from tqdm import tqdm 
import os 
import pickle


from albumentations import (HorizontalFlip, VerticalFlip, CLAHE, RandomContrast, RandomGamma, RandomBrightness, MedianBlur, IAASharpen, IAAEmboss, HueSaturationValue, ToGray, OneOf, RGBShift, ChannelShuffle, Compose)

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
            
        self.data_loc = self.opt.data_loc
        
        
        if self.train:
            self.transforms = ListDataset.train_transformations(self.opt)
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
        if self.train:
            self.aspect_ratios = self.load_aspect_ratio(self.opt.aspect_loc_train)
        else:
            self.aspect_ratios = self.load_aspect_ratio(self.opt.aspect_loc_valid)
        
        if self.opt.normalize:
            self.normalizer = Normalizer(self.opt.mean, self.opt.std)
        if self.opt.resize:
            self.resize = MyResizer(min_side = self.opt.min_size)

    def __getitem__(self, idx):
        img_loc = self.images[idx]
        label = self.labels[idx]
        img, scale = self.get_image(img_loc)
        if self.multiclass:
            label = torch.FloatTensor(self.one_hot.fit_transform([label])).view(-1)
        else:
            label = label.long()
        output = {"img": img, "scale": scale, "label": label}
        return output

    def __len__(self):
        return len(self.images)

    def get_image(self, img_loc):
        img = self.load_image(img_loc)
        img = np.asarray(img)
        if self.train:
            img = self.transforms(image = img)
        else:
            img = {"image": img}
        if self.opt.normalize:
            img = self.normalizer(img)
        if self.opt.resize:
            img = self.resize(img)
            
        return img["image"], img["scale"]

    def inverse_image(self):
        pass ## Given torch output tensor output of a dataloader, this should reverse engineer the options and output another image.
    
    def load_image(self, loc):
        path = self.data_loc + loc
        img = skimage.io.imread(path)
        if len(img.shape) == 2:
            img = skimage.color.gray2rgb(img)
        return img.astype(np.float32)/255.0
            
    
    @staticmethod
    def train_transformations(opt):
        """Albugumentations 
        
        """
        img_transforms = []
        if opt.hflip:
            img_transforms.append(HorizontalFlip(p=0.5))
        if opt.vflip:
            img_transforms.append(VerticalFlip(p=0.5))
        if opt.color_transforms:
            color_transforms = [
                                RGBShift(p=0.5),
                                ChannelShuffle(p=0.5),
                                CLAHE(p=0.5),
                                RandomContrast(p=0.5),
                                RandomGamma(p=0.5),
                                RandomBrightness(p=0.5),
                                MedianBlur(p=0.1),
                                IAASharpen(),
                                IAAEmboss()]
            img_transforms.extend(color_transforms)
            img_transforms.append(HueSaturationValue(p=0.3))
        if opt.togray:
            img_transforms.append(ToGray(p=0.05))
        return Compose(img_transforms)
    
#     @staticmethod
#     def test_transformations_new(opt):
#         img_transforms = []
#         if opt.normalize:
#             img_transforms.append(Normalizer(opt.mean, opt.std))
#         if opt.resize:
#             img_transforms.append(MyResizer(min_side=opt.min_size))
#         return Compose(img_transforms)

    def load_aspect_ratio(self, save_loc="img_attributes.pth"):
        import pickle
        if os.path.isfile(save_loc):
            with open(save_loc, 'rb') as handle:
                aspect_ratios = pickle.load(handle)
        else:
            aspect_ratios = list()
            for i in tqdm(range(self.num_samples)):
                img = self.load_image(self.images[i])
                aspect_ratios.append(float(img.shape[1])/float(img.shape[0]))
            with open(save_loc, 'wb') as handle:
                pickle.dump(aspect_ratios, handle, protocol=pickle.HIGHEST_PROTOCOL)
        assert len(aspect_ratios) == self.num_samples
        #print(aspect_ratios)
        return aspect_ratios
    
    def image_aspect_ratio(self, idx):
        return self.aspect_ratios[idx]      
