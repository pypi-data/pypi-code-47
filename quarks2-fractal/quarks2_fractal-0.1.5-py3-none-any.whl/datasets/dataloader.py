import torch
#from loguru import logger

from .seversteal import SeverDL
from .datasets import CSVDataloader, JsonDataloader
from .agu import get_transforms

def get_dataloader(config, dl=True):
    train_transforms, val_transforms = get_transforms(config)
    
    if config.dataset_type =="seg+rle":
        train_dl = SeverDL(config.train_loc, config.train_images_loc, train_transforms, classifier=config.classifier, binary=config.binary)
        val_dl = SeverDL(config.val_loc, config.val_images_loc, val_transforms, classifier=config.classifier, binary=config.binary)
    elif config.dataset_type == "csv":
       labels = [i.strip() for i in open(config.labels, "r")]
       label_mapping = {k:v for v, k in enumerate(labels)}
       print(label_mapping)
       train_dl = CSVDataloader(csv_file=config.train_loc, img_root=config.train_images_loc, transforms=train_transforms, label_mapping=label_mapping)
       val_dl = CSVDataloader(csv_file=config.val_loc, img_root=config.val_images_loc, transforms=val_transforms, label_mapping=label_mapping)
    elif config.dataset_type == "json":
        train_dl = JsonDataloader(ann_file=config.train_loc, img_root=config.train_images_loc, transforms=train_transforms)
        val_dl = JsonDataloader(ann_file=config.val_loc, img_root=config.val_images_loc, transforms=val_transforms)
    else:
        raise ValueError("dataset is not implemented: {}", config.name)
        #logger.debug("dataset is not implemented: {}", config.name)
    if dl:
        train_dataloader = torch.utils.data.DataLoader(train_dl, batch_size=config.batch_size, shuffle=True, num_workers=config.num_workers)
        val_dataloader = torch.utils.data.DataLoader(val_dl, batch_size=config.batch_size, shuffle=False, num_workers=config.num_workers)

        if config.dataparallel:
            raise NotImplementedError("Data Parallel module is not implemented it yet")
        return train_dataloader, val_dataloader
    else:
        return train_dl, val_dl