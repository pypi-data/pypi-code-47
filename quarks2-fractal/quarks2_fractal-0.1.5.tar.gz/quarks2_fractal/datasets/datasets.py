import torch
import pandas as pd
from PIL import Image
import numpy as np
import cv2
import random
import json
import glob
import os
from tqdm import tqdm
from .cls_labels import ClassList


class CSVDataloader(torch.utils.data.DataLoader):
    def __init__(self, csv_file, img_root="", label_mapping=None, transforms=None):
        super(CSVDataloader).__init__()
        self.csv_file = csv_file
        self.data = pd.read_csv(self.csv_file)
        self.data.columns = ["img_loc", "labels"]
        self.transforms = transforms 
        self.img_root = img_root 
        self.label_mapping = label_mapping
    
    def __getitem__(self, idx):
        img_loc, label = self.data.iloc[idx, :]
        file_path = self.img_root+img_loc

        if self.label_mapping is not None:
            label = self.label_mapping[label]
        # Read an image with OpenCV
        img = cv2.imread(file_path)
        # By default OpenCV uses BGR color space for color images,
        # so we need to convert the image to RGB color space.
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if self.transforms is not None:
            img = self.transforms(image=img)
            img = img["image"]
        label = torch.LongTensor([label])
        return img, label

    def __len__(self):
        return self.data.shape[0]
    
    def total_labels(self):
        return self.data["labels"].unique().shape
    
    @classmethod
    def infer(self, img_loc, transforms=None):
        img = cv2.imread(img_loc)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = img.copy()
        if transforms is not None:
            img = transforms(image=img)
            img = img["image"]
        img = img.unsqueeze(0)
        if torch.cuda.is_available():
           img = img.cuda()
        return img , image

def create_plant_seedling_ds(root, train_size=0.9):
    x = glob.glob(root+"/**/*.png")
    random.seed(50)
    random.shuffle(x)
    x_train = x[:int(train_size*len(x))]
    x_val = x[int(train_size*len(x)):]
    x1 = pd.DataFrame(x_train)
    x1[1] = x1[0].apply(lambda x: x.rsplit("/")[6])
    x1[0] = x1[0].apply(lambda x: x.split("/", 5)[-1])
    x2 = pd.DataFrame(x_val)
    x2[1] = x2[0].apply(lambda x: x.rsplit("/")[6])
    x2[0] = x2[0].apply(lambda x: x.split("/", 5)[-1])
    return x1, x2

class JsonDataloader(torch.utils.data.DataLoader):
    def __init__(self, ann_file, img_root="", transforms=None):
        super(JsonDataloader).__init__()
        self.ann_file = ann_file
        self.img_root = img_root 
        self.transforms = transforms
        with open(self.ann_file, "r") as f:
            data = json.load(f)
        self.img_id= data["images"]
    
    def __getitem__(self, idx):
        img = self.img_id[idx]
        label = torch.as_tensor([img["labels"]])
        file_path = self.img_root+img["image_id"]
        # Read an image with OpenCV
        img = cv2.imread(file_path)
        # By default OpenCV uses BGR color space for color images,
        # so we need to convert the image to RGB color space.
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if self.transforms is not None:
            img = self.transforms(image=img)
            img = img["image"]

        return img, label
        
    def __len__(self):
        return len(self.img_id)
    
    @classmethod
    def infer(self, img_loc, transforms=None):
        img = cv2.imread(img_loc)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = img.copy()
        if transforms is not None:
            img = transforms(image=img)
            img = img["image"]
        img = img.unsqueeze(0)
        if torch.cuda.is_available():
           img = img.cuda()
        return img , image

class ImageFolder(torch.utils.data.DataLoader):
    def __init__(self, img_root="", transforms=None):
        super(ImageFolder).__init__()
        self.transforms = transforms
        self.img_id = []
        img_paths = glob.glob(os.path.join(img_root,"*"))
        np.save("/mnt/nfshome1/FRACTAL/sindhura.k/quarks2/data/list.txt",img_paths)
        for i in tqdm(img_paths):
            try:
                img = cv2.imread(i)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.img_id.append(i)
            except:
                continue
    
    def __getitem__(self, idx):
        img_loc = self.img_id[idx]
        # Read an image with OpenCV
        img = cv2.imread(img_loc)
        # By default OpenCV uses BGR color space for color images,
        # so we need to convert the image to RGB color space.
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if self.transforms is not None:
            img = self.transforms(image=img)
            img = img["image"]

        return img, img_loc
        
    def __len__(self):
        return len(self.img_id)


if __name__ == "__main__":
    root = "/imagehdd/public_datasets/Food/"
    data = FoodDataloader(root+"train_info.csv", img_root=root+"train_set/", transforms=None)
    print(data.data.head(10))
    print(data.data.iloc[0, :])
    print(data.data.shape[0])
    img, label = data[9]
    print(img.size, label.shape)
    print(label)
    print(data.data.columns)
    print(data.total_labels())