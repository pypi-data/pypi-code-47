import torch
import torch.utils.data

import numpy as np # linear algebra
from PIL import Image
import cv2
import pandas as pd 

def keep_only_damaged_image(df):
    imgs_having_defects = df[~df["EncodedPixels"].isna()]["image_name"].unique()
    df = df[df["image_name"].isin(imgs_having_defects)]
    return df, imgs_having_defects

def damaged_non_damaged(df):
    _, imgs_having_defects = keep_only_damaged_image(df)
    image_name = np.unique(df["image_name"].values)
    imgs_not_having_defects = [i for i in image_name if i not in imgs_having_defects]
    return imgs_having_defects, imgs_not_having_defects


def create_binary_df(df):
    imgs_having_defects, imgs_not_having_defects = damaged_non_damaged(df)
    act_df = pd.DataFrame()
    act_df["image_name"] = np.concatenate([imgs_having_defects, imgs_not_having_defects])
    act_df["class"] = np.concatenate([np.ones(len(imgs_having_defects)), np.zeros(len(imgs_not_having_defects))])
    return act_df


def give_me_img_and_mask(df, img_name, folder_loc):
    img = Image.open(folder_loc+img_name)
    w, h = img.size
    masks = df[df["image_name"] == img_name]
    #print(masks)
    masks_final = masks[~masks["EncodedPixels"].isna()]["EncodedPixels"].values
    labels = masks[~masks["EncodedPixels"].isna()]["label_name"].values
    assert len(masks_final) == len(labels)
    fmasks = np.zeros((h, w))
    for label, mask_final in zip(labels, masks_final):
        #print(mask_final)
        mask = rle2mask(mask_final, shape=(w, h))
        mask[mask>0] = label 
        fmasks +=mask
    fmasks = np.int64(fmasks)
    assert np.max(np.unique(fmasks)) <=4 
    return img, fmasks

def give_img_mask_predmask(df, img_name, folder_loc):
    img = Image.open(folder_loc+img_name)
    w, h = img.size 
    masks = df[df["image_name"] == img_name]
    
    masks_final = masks[~masks["EncodedPixels"].isna()]["EncodedPixels"].values
    labels = masks[~masks["EncodedPixels"].isna()]["label_name"].values

    predmasks_final = masks[~masks["Pred_EncodedPixels"].isna()]["Pred_EncodedPixels"].values
    predlabels = masks[~masks["Pred_EncodedPixels"].isna()]["label_name"].values

    assert len(masks_final) == len(labels)
    assert len(predmasks_final) == len(predlabels)
    
    fmasks = np.zeros((h, w))
    fpredmasks = np.zeros((h, w))

    for label, mask_final in zip(labels, masks_final):
        mask = rle2mask(mask_final, shape=(w, h))
        mask[mask>0] = label
        fmasks +=mask

    for label2, predmask_final in zip(predlabels, predmasks_final):
        predmask = rle2mask(predmask_final, shape=(w, h))
        predmask[predmask>0] = label2
        fpredmasks +=predmask
        
    fmasks = np.int64(fmasks)
    fpredmasks = np.int64(fpredmasks)

    assert np.max(np.unique(fmasks)) <=4
    assert np.max(np.unique(fpredmasks)) <=4
    return img, fmasks, fpredmasks


def process_df(df):
    df["label_name"] = df["ImageId_ClassId"].apply(lambda x: x.rsplit("_")[-1])
    df["image_name"] = df["ImageId_ClassId"].apply(lambda x: x.rsplit("_")[0])
    return df 

def get_rle_from_mask(fout, num_classes=5):
    masks = []
    for i in range(1, num_classes):
        out= np.zeros(fout.shape)
        out[fout == i] = 1
        x = mask2rle(out)
        masks.append(x)
    return masks


def rle2mask(mask_rle, shape=(1600,256)):
    '''
    mask_rle: run-length as string formated (start length)
    shape: (width,height) of array to return 
    Returns numpy array, 1 - mask, 0 - background

    '''
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T


def mask2rle(img):
    '''
    https://www.kaggle.com/paulorzp/rle-functions-run-lenght-encode-decode
    img: numpy array, 1 - mask, 0 - background
    Returns run length as string formated
    '''
    pixels= img.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)


class SeverDL(torch.utils.data.DataLoader):
    def __init__(self, path, img_loc="../input/train_images/", transforms=None, classifier=True, binary=False):
        super(SeverDL).__init__()
        
        print("Reading data")
        self.df = pd.read_csv(path)
        print("Processing df")
        self.df = process_df(self.df)
        self.imgs = self.df["image_name"].unique()
        self.img_loc = img_loc
        self.cls = classifier
        self.binary=binary
        self.transforms = transforms
    
    def __getitem__(self, idx):
        select_img = self.imgs[idx]
        img, masks = give_me_img_and_mask(self.df, select_img, self.img_loc)
        if self.transforms is not None:
            aug = self.transforms(image=np.asarray(img), mask=masks)
            img = aug["image"]
            masks = aug["mask"]
        if self.binary:
            masks[masks>0] = 1
        if self.cls:
            target = 1 if masks[masks >0].sum() > 0 else 0
            masks = torch.Tensor([target])

        return img, masks

    def __len__(self):
        return len(self.imgs)

class SegDL(torch.utils.data.DataLoader):
    def __init__(self, path, transforms=None, use_all=False, img_loc="../input/train_images/", crop=False, crop_size=(256, 256), binary=False, downsample=None, resize=False):
        super(SegDL).__init__()
        
        print("Reading data")
        self.df = pd.read_csv(path)
        print("Processing df")
        self.df = process_df(self.df)
        self.use_all = use_all 
        self.imgs = self.df["image_name"].unique()
        self.img_loc = img_loc
        self.crop = crop
        self.crop_size = crop_size
        self.binary = binary
        self.downsample = downsample
        self.resize = resize
        if self.binary:
            print("Binary data will be generated. non-defective vs defective")
        
        if not self.use_all:
            print("Removing images which don't have any defects")
            self.df, self.imgs = keep_only_damaged_image(self.df)
            
        self.transforms = transforms
    
    def __getitem__(self, idx):
        select_img = self.imgs[idx]
        img, masks = give_me_img_and_mask(self.df, select_img, self.img_loc)
        if self.crop:
            img, masks = special_crop(img, masks, self.crop)
        if isinstance(self.resize, int):
            img, masks = resize_image(img, masks, self.resize)
            img, masks = pad_image(img, masks, multiple=32, value=0)
            img = Image.fromarray(img)
        if self.transforms is not None:
            img, masks = self.transforms(img, masks)
        if self.binary:
            masks[masks>0] = 1 
        if isinstance(self.downsample, int):
            if isinstance(masks, torch.Tensor):
                masks = masks.numpy()
            h, w = masks.shape
            masks = cv2.resize(masks, (int(w/self.downsample), int(h/self.downsample)),  interpolation=cv2.INTER_NEAREST)
        if isinstance(masks, np.ndarray):
            masks = torch.from_numpy(masks)
        masks = masks.unsqueeze(0)
        return img, masks.float()

    def __len__(self):
        return len(self.imgs)