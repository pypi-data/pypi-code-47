"""
"""
import argparse
import time

from typing import List, Optional

from . import cli
from . import logging
from . import nn
from . import utils


def main(args: argparse.Namespace, extra_args: Optional[List[str]] = None):
    logger = logging.initialize(__package__, args)
    utils.set_random_seed(args.seed)

    model1 = nn.load(args.network1)
    model2 = nn.load(args.network2)

    import torch
    import torch.nn.functional as F
    import torch.utils.data as data
    import torchvision.datasets as datasets
    import torchvision.transforms as transforms

    transform = transforms.Compose([transforms.ToTensor()])
    mnist = datasets.MNIST("./data", download=True, train=True, transform=transform)
    data_loader = data.DataLoader(mnist, batch_size=1000)

    with torch.no_grad():
        num_correct = 0.0
        for i, (x, y) in enumerate(data_loader):
            y_ = model1(x)[0]
            num_correct += (y_.argmax(dim=1) == y).sum()
        print(num_correct / len(data_loader.dataset))


def _main():
    main(*cli.parse_args())


if __name__ == "__main__":
    _main()

