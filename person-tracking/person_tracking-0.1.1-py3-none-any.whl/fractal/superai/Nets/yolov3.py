import torch
import torch.nn as nn

class ConvBlock(nn.Module):
    def __init__(self, inplanes, planes, kernel_size, stride=1, pad=1, bias=False):
        super(ConvBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=inplanes,
                             out_channels = planes,
                             kernel_size = kernel_size,
                             bias = bias,
                             stride = stride,
                             padding = pad)
        self.bn1 = nn.BatchNorm2d(planes)
        self.lrelu = nn.LeakyReLU(negative_slope=0.1, inplace=True)

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.lrelu(out)
        return out
    
    
class ResBlock(nn.Module):
    def __init__(self, in_channels, reduce):
        super(ResBlock, self).__init__()
        self.conv1 = ConvBlock(in_channels, reduce, 1, 1, 0)
        self.conv2 = ConvBlock(reduce, in_channels, 3, 1, 1)
    
    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        return out+x
        

class Darknet53(nn.Module):
    def __init__(self):
        super(Darknet53, self).__init__()
        self.conv1 = ConvBlock(3, 32, 3, 1, 1) # 256 * 256
        self.conv2 = ConvBlock(32, 64, 3, 2, 1) # 128 * 128
        self.resblock1 = self._make_layers(64, 32, 1)
        self.conv3 = ConvBlock(64, 128, 3, 2, 1)
        self.resblock2 = self._make_layers(128, 64, 2)
        self.conv4 = ConvBlock(128, 256, 3, 2, 1)
        self.resblock3 = self._make_layers(256, 128, 8)
        self.conv5 = ConvBlock(256, 512, 3, 2, 1)
        self.resblock4 = self._make_layers(512, 256, 8)
        self.conv6 = ConvBlock(512, 1024, 3, 2, 1)
        self.resblock5 = self._make_layers(1024, 512, 4)

    
    def _make_layers(self, in_channels, reduce, blocks):
        layer = []
        for _ in range(blocks):
            layer.append(ResBlock(in_channels, reduce))
        return nn.Sequential(*layer)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.resblock1(x)
        x = self.conv3(x)
        x = self.resblock2(x)
        x = self.conv4(x)
        out1 = self.resblock3(x)
        x = self.conv5(out1)
        out2 = self.resblock4(x)
        x = self.conv6(out2)
        out3 = self.resblock5(x)
        return out3
    

class Yolov3_classifier(nn.Module):
    def __init__(self, num_classes = 211):
        super(Yolov3_classifier, self).__init__()
        self.num_classes = num_classes
        self.backend = Darknet53()
        self.avgpool = nn.AvgPool2d(13, stride=1)
        self.classifier = nn.Linear(1024, self.num_classes)
    
    def forward(self, x):
        x = self.backend(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x 
