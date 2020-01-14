""" 
Things to check 
- wheather L2 norm is required or not after roi pooling?
"""
import torch
import numpy as np
import torch.nn as nn
from torchvision.ops import RoIPool


class RemapModule(nn.Module):
    def __init__(self, n_regions, fe_size, output_size=(1, 1)):
        """
        """
        super().__init__()
        self.n_regions = n_regions
        self.fe_size = fe_size # w, h 
        self.bbox = torch.from_numpy(get_regions(self.fe_size[0], self.fe_size[1], self.n_regions)).float()
        self.conv_layer = nn.Conv2d(self.bbox.shape[0], 1, kernel_size=1)
        self.roi_pool = RoIPool(output_size, spatial_scale=1)
    
    def forward(self, x):
        """x is one of the layer output of the encoder network
        """
        batch_size, filters = x.shape[:2]
        if x.is_cuda:
            box = self.bbox.cuda()
        else:
            box = self.bbox
        pooler = self.roi_pool(x, [box for i in range(batch_size)])
        pooler = pooler.squeeze(3).view(batch_size, -1, filters, 1)
        x = self.conv_layer(pooler)
        return x

class Remap(nn.Module):
    def __init__(self, out_channels, output_shapes, n_regions=5):
        '''
        inchannels: sum of the # of feature maps of the output we take from conv layers
        outchannels: dim length after PCA
        n_regions: list of number of regions obtained from each of the output layer
        '''
        super().__init__()
        self.out_channels = out_channels 
        self.output_shapes = output_shapes 
        self.n_regions = n_regions
        assert len(self.out_channels) == len(output_shapes)
        total_layers = len(self.out_channels)
        self.remap = nn.ModuleList()
        for _ in range(total_layers):
            remap_layer = RemapModule(n_regions, self.output_shapes[0])
            self.remap.append(remap_layer)
    
    def forward(self, encoder_output):
        outputs = []
        for num, layer in enumerate(encoder_output):
            out = self.remap[num](layer)
            outputs.append(out.squeeze(3).squeeze(1))
        return torch.cat(outputs, axis=1)
    
def l2_norm(z):
    eps=1e-10
    norm = torch.norm(z, 2, 1, True)
    z = z / (norm + eps) 
    return z
    
def get_regions(W, H, L):
        '''
        Arguments:
            W: width of the output from a specific conv layer
            H: Height of the output from a specific conv layer
            L: Scale which is related to the aspect ratio of the regions. For L=1 we get just one region
        Returns:
            list of lower leftmost corner co-ordinates and the width and height of the regions
        '''
        ovr = 0.4  # desired overlap of neighboring regions
        steps = np.array([2, 3, 4, 5, 6, 7], dtype=np.float)  # possible regions for the long dimension

        w = min(W, H)
        b = (max(H, W) - w) / (steps - 1)
        idx = np.argmin(abs(((w ** 2 - w * b) / w ** 2) - ovr))  # steps(idx) regions for long dimension

        # region overplus per dimension
        Wd, Hd = 0, 0
        if H < W:
            Wd = idx + 1
        elif H > W:
            Hd = idx + 1
        
        regions = []

        for l in range(1, L + 1):
            wl = np.floor(2 * w / (l + 1))
            wl2 = np.floor(wl / 2 - 1)
            b = (W - wl) / (l + Wd - 1)
            if np.isnan(b):  # for the first level
                b = 0
            cenW = np.floor(wl2 + np.arange(0, l + Wd) * b) - wl2  # center coordinates
            b = (H - wl) / (l + Hd - 1)
            if np.isnan(b):  # for the first level
                b = 0
            cenH = np.floor(wl2 + np.arange(0, l + Hd) * b) - wl2  # center coordinates
            for i_ in cenH:
                for j_ in cenW:
                    # R = np.array([i_, j_, wl, wl], dtype=np.int)
                    R = np.array([j_, i_, wl, wl], dtype=np.int)
                    if not min(R[2:]):
                        continue
                    regions.append(R)

        regions = np.asarray(regions)
        return regions