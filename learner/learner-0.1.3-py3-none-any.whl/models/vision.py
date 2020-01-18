from collections import OrderedDict

import torch.nn as nn


class LeNet5(nn.Module):
    """LeNet 5 from LeCun Yann et al.

    LeCun, Yann, Léon Bottou, Yoshua Bengio, Patrick Haffner, and others.
    ‘Gradient-Based Learning Applied to Document Recognition’.
    Proceedings of the IEEE 86, no. 11 (1998): 2278–2324.

    Input    - 1x28x28
    Conv     - 6x28x28  (5x5 kernel, padding 2) --> ReLU
    Maxpool  - 6@14x14  (2x2 kernel, stride 2) Subsampling
    Conv     - 16@10x10 (5x5 kernel) --> ReLU
    Maxpool  - 16@5x5   (2x2 kernel, stride 2) Subsampling
    Conv     - 120@1x1  (5x5 kernel) --> ReLU
    FC       - 84  --> ReLU
    FC       - 10  (Output) --> LogSoftmax
    """

    def __init__(self):
        super().__init__()
        self.convnet = nn.Sequential(OrderedDict([
            ('conv1', nn.Conv2d(1, 6, kernel_size=(5, 5), padding=2)),
            ('relu1', nn.ReLU()),
            ('maxpool1', nn.MaxPool2d(kernel_size=(2, 2), stride=2)),
            ('conv2', nn.Conv2d(6, 16, kernel_size=(5, 5))),
            ('relu2', nn.ReLU()),
            ('maxpool2', nn.MaxPool2d(kernel_size=(2, 2), stride=2)),
            ('conv3', nn.Conv2d(16, 120, kernel_size=(5, 5))),
            ('relu3', nn.ReLU())
        ]))

        self.fc = nn.Sequential(OrderedDict([
            ('fc1', nn.Linear(120, 84)),
            ('relu', nn.ReLU()),
            ('fc2', nn.Linear(84, 10)),
            ('logsoft', nn.LogSoftmax(dim=-1))
        ]))

    def forward(self, x):
        return self.fc(self.convnet(x).view(x.size(0), -1))
