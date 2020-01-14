import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.nn.init as init
from .remap import Remap, l2_norm

class SimpleDecoder(nn.Module):
    def __init__(self, input_channels, classes):
        super().__init__()
        self.input_channels= input_channels
        self.classes= classes
        self.decoder = torch.nn.Linear(self.input_channels, self.classes, bias=True)

    def forward(self, x):
        out = x[0]
        global_feat = F.avg_pool2d(out, out.size()[2:])
        x = torch.flatten(global_feat, 1)
        x = self.decoder(x)
        return x

class Quarksdecoder(nn.Module):
    def __init__(self, input_channels, classes):
        super().__init__()
        self.input_channels= input_channels
        self.classes= classes
        #self.local_conv = nn.Conv2d(self.input_channels, local_planes, 1)
        #self.local_bn = nn.BatchNorm2d(local_planes)
        #self.local_bn.bias.requires_grad_(False)  # no shift
        self.bottleneck_g = nn.BatchNorm1d(self.input_channels)
        self.bottleneck_g.bias.requires_grad_(False)  # no shift
        # self.archead = Arcface(embedding_size=planes, classnum=num_classes, s=64.0)
        #
        self.fc = nn.Linear(self.input_channels, self.classes)
        init.normal_(self.fc.weight, std=0.001)
        init.constant_(self.fc.bias, 0)

    def forward(self, x):
        feat = x[0]
        global_feat = F.avg_pool2d(feat, feat.size()[2:])
        global_feat = global_feat.view(global_feat.size(0), -1)
        global_feat = F.dropout(global_feat, p=0.2)
        global_feat = self.bottleneck_g(global_feat)
        global_feat = l2_norm(global_feat)
        out = self.fc(global_feat) * 16
        return  out

class Remap_decoder(nn.Module):
    def __init__(self, classes, output_channels, encoder_name, pca_channels, img_size, n_regions, n_layers):
        """ Applying remap module as given in the paper 

        classes: number of classes to output
        output_shapes: tuple: list of output shapes 
        encoder_name: str, name of the encoder 
        pca_channels: int, number of channels in the bottleneck layer 
        img_size: tuple, (w, h) width and height of the input image
        """
        super().__init__()
        self.n_regions = n_regions
        self.pca_channels = pca_channels
        self.classes = classes
        self.n_layers = n_layers

        if "resnet" in encoder_name or "se_resnet" in encoder_name:
            out_shapes = [(img_size[0]//scale, img_size[1]//scale) for scale in [64, 32, 16, 8, 4]][:self.n_layers]
        else:
            raise NotImplementedError("REMAP implementation is now only tested for resnet and se_resnet variants. Please raise a pull request if you tested for any other architecture")

        self.in_channels_pca = sum(output_channels[:self.n_layers])
        self.linear_pca = nn.Linear(self.in_channels_pca, self.pca_channels, bias=True)
        self.remap = Remap(output_channels[:n_layers], out_shapes, self.n_regions)
        self.classifier = nn.Linear(self.pca_channels, self.classes)
    
    def forward(self, x):
        x = x[:self.n_layers]
        output = self.remap(x)
        output = l2_norm(output)
        pca_output = self.linear_pca(output)
        fc = self.classifier(pca_output)
        return pca_output, fc

def get_decoder(classes, encoder, **kwargs):
    print(kwargs)
    if kwargs["name"] == "linear":
        input_channels = encoder.out_shapes[0]
        decoder = SimpleDecoder(input_channels, classes)
    elif kwargs["name"] == "quarks":
        input_channels = encoder.out_shapes[0]
        decoder = Quarksdecoder(input_channels, classes)
    elif kwargs["name"] == "remap":
        pca_channels = kwargs["pca_channels"]
        img_size = (kwargs["height"], kwargs["width"])
        n_regions = kwargs["n_regions"]
        encoder_name = kwargs["encoder_name"]
        n_layers = kwargs["n_layers"]
        decoder= Remap_decoder(classes, encoder.out_shapes, encoder_name, pca_channels, img_size, n_regions, n_layers)
    else:
        raise NotImplementedError("The following decoder is not implemented")
    return decoder