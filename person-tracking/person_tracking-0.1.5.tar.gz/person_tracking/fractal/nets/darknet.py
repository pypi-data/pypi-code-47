import torch
import torch.nn as nn
import torch.nn.init as init
import math

from ..common_utils.img_utils import write_results


def initialize_weights(net):
    for m in net.modules():
        if isinstance(m, nn.Conv2d):
            init.normal(m.weight, mean=0, std=0.01)
            if m.bias is not None:
                init.constant(m.bias, 0)
        elif isinstance(m, nn.BatchNorm2d):
            m.weight.data.fill_(1)
            m.bias.data.zero_()
    return net

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
        return out1, out2, out3
    

class Yolov3_classifier(nn.Module):
    def __init__(self, num_classes = 211):
        super(Yolov3_classifier, self).__init__()
        self.num_classes = num_classes
        self.backend = Darknet53()
        self.avgpool = nn.AvgPool2d(11, stride=1)
        self.classifier = nn.Linear(46080, self.num_classes)
    
    def forward(self, x):
        _, _, x = self.backend(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x 
    
    
    
class Darknet_Dbox(nn.Module):
    def __init__(self, num_classes=80, anchors=9):
        super(Darknet_Dbox, self).__init__()
        self.num_classes = num_classes
        self.anchors = anchors
        self.output_dim = int((self.num_classes+5) * (self.anchors/3))
        self.backend = Darknet53()
        self.conv_block_1 = nn.Sequential(*[
            ConvBlock(1024, 512, 1, 1, 0),
            ConvBlock(512, 1024, 3, 1, 1),
            ConvBlock(1024, 512, 1, 1, 0),
            
        ]) 
        self.yolo1_0 = nn.Sequential(*[
            ConvBlock(512, 1024, 3, 1, 1),
            ConvBlock(1024, 512, 1, 1, 0)
        ]) 
        self.yolo1_1 = nn.Sequential(*[
            ConvBlock(512, 1024, 3, 1, 1),
            nn.Conv2d(1024, self.output_dim, 1, 1, 0)
        ])# mask of [116,90,  156,198,  373,326], classes=80, num=9 jitter=.3, ignore_thresh=.7, thruth_thresh=1, random=1
        
        self.upsample1 = nn.Sequential(*[
            ConvBlock(512, 256, 1, 1, 0),
            nn.Upsample(scale_factor = 2, mode = "nearest"),
        ])
        
        self.conv_block_2 = nn.Sequential(*[
            ConvBlock(768, 256, 1, 1, 0),
            ConvBlock(256, 512, 3, 1, 1),
            ConvBlock(512, 256, 1, 1, 0),            
        ])
        
        self.yolo2_0 = nn.Sequential(*[
            ConvBlock(256, 512, 3, 1, 1),
            ConvBlock(512, 256, 1, 1, 0)
        ])
        self.yolo2_1 = nn.Sequential(*[
            ConvBlock(256, 512, 3, 1, 1),
            nn.Conv2d(512, self.output_dim, 1, 1, 0)
        ])# mask of [ 30,61,  62,45,  59,119], classes=80, num=9 jitter=.3, ignore_thresh=.7, thruth_thresh=1, random=
        
        
        self.upsample2 = nn.Sequential(*[
            ConvBlock(256, 128, 1, 1, 0),
            nn.Upsample(scale_factor = 2, mode = "nearest"),
        ])
        
        self.conv_block_3 = nn.Sequential(*[
            ConvBlock(384, 128, 1, 1, 0),
            ConvBlock(128, 256, 3, 1, 1),
            ConvBlock(256, 128, 1, 1, 0),            
        ])
        self.yolo3_0 = nn.Sequential(*[
            ConvBlock(128, 256, 3, 1, 1),
            ConvBlock(256, 128, 1, 1, 0)
        ])
        self.yolo3_1 = nn.Sequential(*[
            ConvBlock(128, 256, 3, 1, 1),
            nn.Conv2d(256, self.output_dim, 1, 1, 0)
        ])# mask of [ 10,13,  16,30,  33,23], classes=80, num=9 jitter=.3, ignore_thresh=.7, thruth_thresh=1, random=1
        
        self.__init_this_shit(self.yolo1_1)
        self.__init_this_shit(self.yolo2_1)
        self.__init_this_shit(self.yolo3_1)
        
        
    
    def __init_this_shit(self, x, val =0.2):
        for num, m in enumerate(x):
            #print(num, m)
            if isinstance(m, nn.Conv2d):
                torch.nn.init.normal_(m.weight, mean=-0.019, std = 0.05)
                if m.bias is not None:                
                    if num == 1:
                        #print("Bias is using this formula")
                        bias = -1 * math.log((1-val)/val)
                        print(bias)
                        torch.nn.init.constant_(m.bias, -0.05) #mean=-0.5, std=0.12)
                    else:
                        torch.nn.init.constant_(m.bias, 0)
        
    
    def forward(self, x):
        out1, out2, out3 = self.backend(x)
        x = self.conv_block_1(out3)
        x = self.yolo1_0(x)
        yolo1 = self.yolo1_1(x)
        out = self.upsample1(x)
        x = torch.cat((out, out2), 1) #512+256 #
        x = self.conv_block_2(x)
        x = self.yolo2_0(x)
        yolo2 = self.yolo2_1(x)
        out = self.upsample2(x)
        x = torch.cat((out, out1), 1) # 256+128
        x = self.conv_block_3(x)
        x = self.yolo3_0(x)
        yolo3 = self.yolo3_1(x)
        return yolo1, yolo2, yolo3

class Darknet_yolo(nn.Module):
    def __init__(self, num_classes=80, anchors=9, scale=3):
        super(Darknet_yolo, self).__init__()
        self.dpn = Darknet_Dbox(num_classes, anchors)
        self.num_classes = num_classes 
        self.anchors = anchors
        self.scale = scale
        
    def forward(self, x, inference=True):
        if inference:
            batch_size = x.shape[0]
            out = self.dpn(x)
            anchors_per_scale = int(self.anchors/len(out))

            yolo1, yolo2, yolo3 = out
            yolo3_grid_size = int(yolo3.shape[-1])
            yolo2_grid_size = int(yolo2.shape[-1])
            yolo1_grid_size = int(yolo1.shape[-1])

            yolov3_ = yolo3.view(batch_size, (self.num_classes+5) * anchors_per_scale, yolo3_grid_size * yolo3_grid_size).transpose(1, 2).contiguous()
            yolov3_ = yolov3_.view(batch_size, yolo3_grid_size*yolo3_grid_size*anchors_per_scale, (self.num_classes+5))

            yolov2_ = yolo2.view(batch_size, (self.num_classes+5) * anchors_per_scale, yolo2_grid_size * yolo2_grid_size).transpose(1, 2).contiguous()
            yolov2_ = yolov2_.view(batch_size, yolo2_grid_size*yolo2_grid_size*anchors_per_scale, (self.num_classes+5))

            yolov1_ = yolo1.view(batch_size, (self.num_classes+5) * anchors_per_scale, yolo1_grid_size * yolo1_grid_size).transpose(1, 2).contiguous()
            yolov1_ = yolov1_.view(batch_size, yolo1_grid_size*yolo1_grid_size*anchors_per_scale, (self.num_classes+5))
            return torch.cat([yolov1_, yolov2_, yolov3_], 1)
            
        else:
            batch_size = x.shape[0]
            out = self.dpn(x)
            #anchors_per_scale = self.anchors/len(out)

            yolo1, yolo2, yolo3 = out

            if self.scale  <= 3:
                return [yolo1, yolo2, yolo3]
            else:
                raise ValueError("Only 3 scales are available")
    
    def predict(self, img_tensor, anchors, strides, nms_applied=True, conf=0.5, iou=0.4):
        """ Outputs a tensor, along with bbox_coord, cls_label and prob_score.
        Inputs:
        -------
        img_tensor: [Batch_size, C, W, H] 
        anchors: [Batch_size, n_anchors, (self.num_classes+5)] # batchsize is 1 
        strides: [n_anchors]
        
        Returns:
        Torch Tensor [N, 6] --> [x1, y1, x2, y2, label, prob_score]
        
        """
        self.eval()
        torch.set_grad_enabled(False)
        out = self(img_tensor)
        out[:, :, 0] = torch.sigmoid(out[:, :, 0])
        out[:, :, 1] = torch.sigmoid(out[:, :, 1])
        out[:, :, 4] = torch.sigmoid(out[:, :, 4])
        
        out[:, :, :2] += anchors[:, :, :2]
        out[:, :, 2:4] = torch.exp(out[:, :, 2:4]) * anchors[:, :, 2:]
        out[:, :, 5:5+self.num_classes] = torch.sigmoid(out[:, :, 5:5+self.num_classes])
        
        out[:, :, :4] *= strides.view(-1, 1).repeat(1, 4).unsqueeze(0)
        out = write_results(out.cpu(), conf, self.num_classes, nms_applied,  iou)
        torch.set_grad_enabled(True)
        self.train()
        return out
        
        
    def load_weights_manually(self, weight_loc):
        """ Loading weights manually to allow transfer learning
        """
        loaded_weights = torch.load(weight_loc)
        
        if "model" in loaded_weights.keys():
            print("Using pretrained weights....")
            loaded_weights = loaded_weights["model"]
            loaded_weights = {'dpn.'+k: v for k, v in loaded_weights.items()}
            self.load_state_dict(loaded_weights)
        else:
            actual_weights = self.dpn.state_dict()
            output_dim = loaded_weights[list(actual_weights.keys())[-1]].shape[0]
            print(output_dim, self.dpn.output_dim)
            if output_dim != self.dpn.output_dim:
                print("Transfer learning... Transfering all weights except the last layer")
                for name1 in actual_weights.keys():
                    if (name1 in loaded_weights.keys()):
                        if actual_weights[name1].shape == loaded_weights[name1].shape:
                            actual_weights[name1] = loaded_weights[name1]
                            print("transferred weights {} {}".format(name1, name1))
                        else:
                            print("Randomly initialized weights for: {} {}".format(name1, name1))
            else:
                actual_weights = loaded_weights
            self.dpn.load_state_dict(actual_weights)
        return self