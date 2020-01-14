""" Fractal AI research

uses albumentations and works together with everything
# Refrences 
- https://github.com/albu/albumentations/blob/master/notebooks/example.ipynb
"""
import cv2
from albumentations.pytorch import ToTensor
from albumentations import (
    Resize,
    PadIfNeeded,
    HorizontalFlip,
    VerticalFlip, 
    Flip,   
    CenterCrop,    
    Crop,
    Compose,
    Transpose,
    RandomRotate90,
    ElasticTransform,
    GridDistortion, 
    OpticalDistortion,
    RandomSizedCrop,
    OneOf,
    CLAHE,
    Normalize,
    RandomBrightnessContrast,    
    RandomGamma, 
    IAAPerspective, 
    ShiftScaleRotate,
    Blur,
    MotionBlur,
    MedianBlur,
    IAAPiecewiseAffine,
    HueSaturationValue,
    IAAAdditiveGaussianNoise,
    GaussNoise,
    IAASharpen, 
    IAAEmboss)


def get_transforms(config):
    if config.transforms == "simple":
        return simple_transforms(config)
    elif config.transforms == "adv1":
        return advanced_transforms(config)
    else:
        raise NotImplementedError("Following transforms are not implemented")


def simple_transforms(config):
    """border_mode=cv2.BORDER_CONSTANT, value=0
    """

    train_transforms = [PadIfNeeded(p=1.0, min_height=config.height, min_width=config.width), Resize(config.height, config.width)]#, #Flip(p=0.5)]

    val_transforms = [PadIfNeeded(p=1.0, min_height=config.height, min_width=config.width), Resize(config.height, config.width)]

    if config.normalize:
        norm = Normalize(mean=config.mean, std=config.std)
        train_transforms.append(norm)
        val_transforms.append(norm)
    
    train_transforms = train_transforms+[ToTensor()]
    val_transforms = val_transforms+[ToTensor()]
    train_transforms = Compose(train_transforms)
    val_transforms = Compose(val_transforms)
    
    return train_transforms, val_transforms


def advanced_transforms(config):
    train_transforms = [
        RandomRotate90(),
        Flip(),
        Transpose(),
        OneOf([
            IAAAdditiveGaussianNoise(),
            GaussNoise(),
        ], p=0.2),
        OneOf([
            MotionBlur(p=.2),
            MedianBlur(blur_limit=3, p=0.1),
            Blur(blur_limit=3, p=0.1),
        ], p=0.2),
        ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        OneOf([
            OpticalDistortion(p=0.3),
            GridDistortion(p=.1),
            IAAPiecewiseAffine(p=0.3),
        ], p=0.2),
        OneOf([
            CLAHE(clip_limit=2),
            IAASharpen(),
            IAAEmboss(),
            RandomBrightnessContrast(),            
        ], p=0.3),
        HueSaturationValue(p=0.3),
        PadIfNeeded(p=1.0, min_height=config.height, min_width=config.width), 
        Resize(config.height, config.width)
    ]

    val_transforms = [PadIfNeeded(p=1.0, min_height=config.height, min_width=config.width), Resize(config.height, config.width)]
    if config.normalize:
        norm = Normalize(mean=config.mean, std=config.std)
        train_transforms.append(norm)
        val_transforms.append(norm)
    
    train_transforms = train_transforms+[ToTensor()]
    val_transforms = val_transforms+[ToTensor()]
    train_transforms = Compose(train_transforms)
    val_transforms = Compose(val_transforms)
    return train_transforms, val_transforms

if __name__ == "__main__":
    from segmentation_models_pytorch.engine.trainer import easydict
    from segmentation_models_pytorch.datasets.agu import simple_transforms
    x = easydict("configs/food_exp1.yaml")
    train, val = simple_transforms(config)