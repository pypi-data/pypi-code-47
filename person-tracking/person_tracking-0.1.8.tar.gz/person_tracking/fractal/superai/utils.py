import torch 
import torchvision
import numpy as np
import math
import matplotlib.pyplot as plt

from tqdm import tqdm 

def get_mean_std(dataset_loader):
    mean = torch.zeros(3)
    std = torch.zeros(3)
    print('==> Computing mean and std..')
    for k in tqdm(dataset_loader):
        inputs, _ = k["img"], k["label"]
        for i in range(3):
            mean[i] += inputs[:,i,:,:].mean()
            std[i] += inputs[:,i,:,:].std()
    mean.div_(len(dataset_loader))
    std.div_(len(dataset_loader))
    print( mean, std)
    return mean,std

def imshow(images, labels, imgs_per_row=4):
    """
    images - stack of images 
    """
    opt = config()
    mean = list(opt.mean)
    std = list(opt.std)
    for img in images:
        for i in range(3):
            img[i] = img[i]*std[i] + mean[i]
    pil_convertor = torchvision.transforms.ToPILImage(mode='RGB')
    pil_images = [ pil_convertor(img) for img in images ]
    batches = math.ceil(len(pil_images)/float(imgs_per_row))
    for i in range(batches):
        imgs = pil_images[i*imgs_per_row:(i+1)*imgs_per_row]
        lab = labels[i*imgs_per_row:(i+1)*imgs_per_row]
        fig, ax = plt.subplots(nrows=1, ncols=len(imgs), sharex="col", sharey="row", figsize=(4*(len(imgs)),4), squeeze=False)
        for i, img in enumerate(imgs):    
            ax[0,i].imshow(img)
            ax[0,i].set_title(lab[i].item())

def vis_unnormalise(train_dataloader, nums):
    dataiter = iter(train_dataloader)
    images, labels = dataiter.next()
    imshow(images[:nums], labels[:nums])

    
def inference_imshow(images, pred_prob, imgs_per_row=3):
    """
    images - stack of images 
    pred_prob - contains list of probabilities and predicted class(incase of incorrect predictions)
    """
    print(type(images))
    print(images.shape)
    print(type(pred_prob))
    pil_convertor = torchvision.transforms.ToPILImage(mode='RGB')
    pil_images = [ pil_convertor(img) for img in images ]
    batches = math.ceil(len(pil_images)/float(imgs_per_row))
    for i in range(batches):
        imgs = pil_images[i*imgs_per_row:(i+1)*imgs_per_row]
        lab = pred_prob[i*imgs_per_row:(i+1)*imgs_per_row]
        fig, ax = plt.subplots(nrows=1, ncols=len(imgs), sharex="col", sharey="row", figsize=(5*(len(imgs)),4), squeeze=False)
        for i, img in enumerate(imgs):    
            ax[0,i].imshow(img)
            ax[0,i].set_title(lab[i])


if __name__ == '__main__':
    from .loaders import ListDataset
    from ..cfgs.ifood import config
    opt = config()
    opt.normalize = False
    trainset = ListDataset(opt, train=True)
    print(len(trainset))
    trainloader = torch.utils.data.DataLoader(trainset, opt.batch_size, shuffle=True, num_workers=4)
    mean, std = get_mean_std(trainloader)
