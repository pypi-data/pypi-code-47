from __future__ import absolute_import
import os
import copy
import random
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms

from PIL import Image
from .loader.CaffeLoader import loadCaffemodel, ModelParallel, Flatten

import argparse
parser = argparse.ArgumentParser()
# Basic options
parser.add_argument("-content_image", help="Content target image", default='examples/inputs/tubingen.jpg')
parser.add_argument("-image_size", help="Maximum height / width of generated image", type=int, default=512)
parser.add_argument("-gpu", help="Zero-indexed ID of the GPU to use; for CPU mode set -gpu = c", default=0)

# Optimization options
parser.add_argument("-dream_weight", type=float, default=1000)
parser.add_argument("-normalize_weights", action='store_true')
parser.add_argument("-tv_weight", type=float, default=1e-3)
parser.add_argument("-num_iterations", type=int, default=5)
parser.add_argument("-jitter", type=int, default=32)
parser.add_argument("-init", choices=['random', 'image'], default='image')
parser.add_argument("-init_image", default=None)
parser.add_argument("-optimizer", choices=['lbfgs', 'adam'], default='adam')
parser.add_argument("-learning_rate", type=float, default=0.75)
parser.add_argument("-lbfgs_num_correction", type=int, default=100)
parser.add_argument("-loss_mode", choices=['bce', 'mse', 'mean', 'norm'], default='mean')

# Output options
parser.add_argument("-print_iter", type=int, default=50)
parser.add_argument("-print_octave_iter", type=int, default=0)
parser.add_argument("-save_iter", type=int, default=100)
parser.add_argument("-save_octave_iter", type=int, default=0)
parser.add_argument("-output_image", default='out.png')

# Octave Options
parser.add_argument("-num_octaves", type=int, default=4)
parser.add_argument("-octave_scale", type=float, default=0.25)
parser.add_argument("-octave_iter", type=int, default=100)

# Channel options
parser.add_argument("-channels", type=str, help="channel for DeepDream", default='-1')
parser.add_argument("-channel_mode", choices=['all', 'strong', 'avg', 'weak'], default='all')

# Other options
parser.add_argument("-original_colors", type=int, choices=[0, 1], default=0)
parser.add_argument("-pooling", choices=['avg', 'max'], default='max')
parser.add_argument("-model_file", type=str, default='models/vgg19-d01eb7cb.pth')
parser.add_argument("-model_type", choices=['caffe', 'pytorch'], default='caffe')
parser.add_argument("-disable_check", action='store_true')
parser.add_argument("-backend", choices=['nn', 'cudnn', 'mkl', 'mkldnn', 'openmp', 'mkl,cudnn', 'cudnn,mkl'], default='nn')
parser.add_argument("-cudnn_autotune", action='store_true')
parser.add_argument("-seed", type=int, default=-1)

parser.add_argument("-dream_layers", help="layers for DeepDream", default='relu4_2')

parser.add_argument("-clamp", action='store_true')

parser.add_argument("-multidevice_strategy", default='4,7,29')
params = parser.parse_args()


Image.MAX_IMAGE_PIXELS = 1000000000 # Support gigapixel images


def main():
    dtype, multidevice, backward_device = setup_gpu()

    cnn, layerList = loadCaffemodel(params.model_file, params.pooling, params.gpu, params.disable_check, True)

    if params.model_type == 'caffe':
        content_image = preprocess(params.content_image, params.image_size).type(dtype)
        clamp_val = 256
    else:
        content_image = preprocess_pytorch(params.content_image, params.image_size).type(dtype)
        clamp_val = 1       
        
    if params.init_image != None:
        image_size = (content_image.size(2), content_image.size(3))
        init_image = preprocess(params.init_image, image_size).type(dtype)

    
    dream_layers = params.dream_layers.split(',')

    # Set up the net_basework, inserting dream loss modules
    cnn = copy.deepcopy(cnn)
    dream_losses, tv_losses = [], []
    next_dream_idx = 1
    net_base = nn.Sequential()
    c, r, p, l, d = 0, 0, 0, 0, 0

    if params.jitter > 0:
        jitter_mod = Jitter(params.jitter).type(dtype)
        net_base.add_module(str(len(net_base)), jitter_mod)
    if params.tv_weight > 0:
        tv_mod = TVLoss(params.tv_weight).type(dtype)
        net_base.add_module(str(len(net_base)), tv_mod)
        tv_losses.append(tv_mod)

    for i, layer in enumerate(list(cnn), 1):
        if next_dream_idx <= len(dream_layers):
            if isinstance(layer, nn.Conv2d):
                net_base.add_module(str(len(net_base)), layer)

                if layerList['C'][c] in dream_layers:
                    print("Setting up dream layer " + str(i) + ": " + str(layerList['C'][c]))
                    loss_module = DreamLoss(params.loss_mode, params.dream_weight, params.channels, params.channel_mode)
                    net_base.add_module(str(len(net_base)), loss_module)
                    dream_losses.append(loss_module)
                c+=1

            if isinstance(layer, nn.ReLU):
                net_base.add_module(str(len(net_base)), layer)

                if layerList['R'][r] in dream_layers:
                    print("Setting up dream layer " + str(i) + ": " + str(layerList['R'][r]))
                    loss_module = DreamLoss(params.loss_mode, params.dream_weight, params.channels, params.channel_mode)
                    net_base.add_module(str(len(net_base)), loss_module)
                    dream_losses.append(loss_module)
                    next_dream_idx += 1
                r+=1
                            
            if isinstance(layer, nn.MaxPool2d) or isinstance(layer, nn.AvgPool2d):
                net_base.add_module(str(len(net_base)), layer)
				
                if layerList['P'][p] in dream_layers:
                    print("Setting up dream layer " + str(i) + ": " + str(layerList['P'][p]))
                    loss_module = DreamLoss(params.loss_mode, params.dream_weight, params.channels, params.channel_mode)
                    net_base.add_module(str(len(net_base)), loss_module)
                    dream_losses.append(loss_module)
                    next_dream_idx += 1
                p+=1
                
            if isinstance(layer, nn.AdaptiveAvgPool2d) or isinstance(layer, nn.AdaptiveMaxPool2d):
                net_base.add_module(str(len(net_base)), layer)
				
            if isinstance(layer, Flatten):
                flatten_mod = Flatten().type(dtype)
                net_base.add_module(str(len(net_base)), flatten_mod)                               
                
            if isinstance(layer, nn.Linear):
                net_base.add_module(str(len(net_base)), layer)

                if layerList['L'][l] in dream_layers:
                    print("Setting up dream layer " + str(i) + ": " + str(layerList['L'][l]))
                    loss_module = DreamLoss(params.loss_mode, params.dream_weight, params.channels, params.channel_mode)
                    net_base.add_module(str(len(net_base)), loss_module)
                    dream_losses.append(loss_module)
                    next_dream_idx += 1
                l+=1
				
            if isinstance(layer, nn.Dropout):
                net_base.add_module(str(len(net_base)), layer)
				
                if layerList['D'][d] in dream_layers:
                    print("Setting up dream layer " + str(i) + ": " + str(layerList['D'][d]))
                    loss_module = DreamLoss(params.loss_mode, params.dream_weight, params.channels, params.channel_mode)
                    net_base.add_module(str(len(net_base)), loss_module)
                    dream_losses.append(loss_module)
                    next_dream_idx += 1
                d+=1
                
                
    if multidevice:
        net_base = setup_multi_device(net_base)
        
    print_torch(net_base, multidevice)
    
    
    # Initialize the image
    if params.seed >= 0:
        torch.manual_seed(params.seed)
        torch.cuda.manual_seed_all(params.seed)
        torch.backends.cudnn.deterministic=True
        random.seed(params.seed)
    if params.init == 'random':
        B, C, H, W = content_image.size()
        base_img = torch.randn(C, H, W).mul(0.001).unsqueeze(0).type(dtype)
    elif params.init == 'image':
        if params.init_image != None:
            base_img = init_image.clone()
        else:
            base_img = content_image.clone()

            
    if params.optimizer == 'lbfgs':
        print("Running optimization with L-BFGS")
    else:
        print("Running optimization with ADAM") 
             
        
    for i in dream_losses:
        i.mode = 'capture'
    net_base(base_img.clone())
    
    if params.channels != '-1' or params.channel_mode != 'all' and params.channels != '-1':
        print_channels(dream_losses, dream_layers)
        
    for i in dream_losses:
        i.mode = 'None'   
        
       
    current_img = new_img(base_img, -1)
    h, w = current_img.size(2),current_img.size(3)  
    print_octave_sizes((h,w), params.octave_scale, params.num_octaves)
    total_dream_losses, total_loss = [], [0]
    
    for iter in range(params.num_iterations):
        for octave in range(1, params.num_octaves+1):
            net = copy.deepcopy(net_base)
            dream_losses, tv_losses = [], []  
            for i, layer in enumerate(net):   
                if isinstance(layer, TVLoss):                 
                    tv_losses.append(layer)      
                elif isinstance(layer, DreamLoss):                 
                    dream_losses.append(layer)
                    
            scale_factor = params.octave_scale * octave
            img = new_img(current_img.clone(), scale_factor)

            net(img)
            for i in dream_losses:
                i.mode = 'loss'
                
        
            # Maybe normalize dream weight
            if params.normalize_weights:
                normalize_weights(dream_losses)
        
            # Freeze the net_basework in order to prevent
            # unnecessary gradient calculations
            for param in net.parameters():
                param.requires_grad = False
                    

            # Function to evaluate loss and gradient. We run the net_base forward and
            # backward to get the gradient, and sum up losses from the loss modules.
            # optim.lbfgs internally handles iteration and calls this function many
            # times, so we manually count the number of iterations to handle printing
            # and saving intermediate results.
            num_calls = [0]
            def feval():
                num_calls[0] += 1
                optimizer.zero_grad()               
                net(img)
                loss = 0
                
                for mod in dream_losses:
                    loss += -mod.loss.to(backward_device)
                if params.tv_weight > 0:
                    for mod in tv_losses:
                        loss += mod.loss.to(backward_device)
                    
                if params.clamp:
                     img.clamp(0,clamp_val)
                     
                total_loss[0] += loss.item()   
                   
                loss.backward()      

                maybe_print_octave_iter(num_calls[0], octave, params.octave_iter, dream_losses)
                maybe_save_octave(iter+1, num_calls[0], octave, img, content_image)
        
                return loss
        
            optimizer, loopVal = setup_optimizer(img)
            while num_calls[0] <= params.octave_iter:
                optimizer.step(feval)
                
            if octave == 1:     
                for mod in dream_losses:
                    total_dream_losses.append(mod.loss.item())
            else:
                for d_loss, mod in enumerate(dream_losses):
                    total_dream_losses[d_loss] += mod.loss.item()
                                  
            current_img = resize_tensor(img.clone(), (h,w))
            
        maybe_print(iter+1, total_loss[0], total_dream_losses)       
        maybe_save(iter+1, current_img, content_image)
        total_dream_losses, total_loss = [], [0]                
    

def maybe_save(t, save_img, content_image):
    should_save = params.save_iter > 0 and t % params.save_iter == 0
    should_save = should_save or t == params.num_iterations
    if should_save:
        output_filename, file_extension = os.path.splitext(params.output_image)
        if t == params.num_iterations:
            filename = output_filename + str(file_extension)
        else:
            filename = str(output_filename) + "_" + str(t) + str(file_extension)
        if params.model_type == 'caffe':       
            disp = deprocess(save_img.clone())
        else:
            disp = deprocess_pytorch(save_img.clone())
            
        # Maybe perform postprocessing for color-independent style transfer
        if params.original_colors == 1:
            disp = original_colors(deprocess(content_image.clone()), disp)

        disp.save(str(filename))
        
        
def maybe_save_octave(t, n, o, save_img, content_image):
    should_save = params.save_octave_iter > 0 and n % params.save_octave_iter == 0
    should_save = should_save or n == params.octave_iter and t % params.save_iter != 0
    if should_save:
        output_filename, file_extension = os.path.splitext(params.output_image)
        if t == params.num_iterations:
            filename = output_filename + str(file_extension)
        else:
            filename = str(output_filename) + "_" + str(t) + "_" + str(o) + "_" + str(n) + str(file_extension)
        if params.model_type == 'caffe':       
            disp = deprocess(save_img.clone())
        else:
            disp = deprocess_pytorch(save_img.clone())
            
        # Maybe perform postprocessing for color-independent style transfer
        if params.original_colors == 1:
            disp = original_colors(deprocess(content_image.clone()), disp)

        disp.save(str(filename))
        

def maybe_print(t, loss, dream_losses):
    if params.print_iter > 0 and t % params.print_iter == 0:
        print("Iteration " + str(t) + " / "+ str(params.num_iterations))
        for i, loss_module in enumerate(dream_losses):
            print("  DeepDream " + str(i+1) + " loss: " + str(loss_module))
        print("  Total loss: " + str(abs(loss)))

        
def maybe_print_octave_iter(t, n, total, dream_losses):
    if params.print_octave_iter > 0 and t % params.print_octave_iter == 0:
        print("Octave iter "+str(n) +" iteration " + str(t) + " / "+ str(total))
        for i, loss_module in enumerate(dream_losses):
            print("  DeepDream " + str(i+1) + " loss: " + str(loss_module.loss.item()))


def print_channels(dream_losses, layers):
    print('\nSelected Layer Channels:')
    for i, l in enumerate(dream_losses):
        print('  ' + layers[i] + ': ', l.dream.channel_loss.channels)
		
		
# Configure the optimizer
def setup_optimizer(img):
    if params.optimizer == 'lbfgs':
        optim_state = {
            'max_iter': params.num_iterations,
            'tolerance_change': -1,
            'tolerance_grad': -1,
        }
        if params.lbfgs_num_correction != 100:
            optim_state['history_size'] = params.lbfgs_num_correction
        optimizer = optim.LBFGS([img], **optim_state)
        loopVal = 1
    elif params.optimizer == 'adam':
        optimizer = optim.Adam([img], lr = params.learning_rate)
        loopVal = params.num_iterations - 1
    return optimizer, loopVal


def setup_gpu():
    def setup_cuda():
        if 'cudnn' in params.backend:
            torch.backends.cudnn.enabled = True
            if params.cudnn_autotune:
                torch.backends.cudnn.benchmark = True
        else:
            torch.backends.cudnn.enabled = False

    def setup_cpu():
        if 'mkl' in params.backend and 'mkldnn' not in params.backend:
            torch.backends.mkl.enabled = True
        elif 'mkldnn' in params.backend:
            raise ValueError("MKL-DNN is not supported yet.")
        elif 'openmp' in params.backend:
            torch.backends.openmp.enabled = True

    multidevice = False
    if "," in str(params.gpu):
        devices = params.gpu.split(',')
        multidevice = True

        if 'c' in str(devices[0]).lower():
            backward_device = "cpu"
            setup_cuda(), setup_cpu()
        else:
            backward_device = "cuda:" + devices[0]
            setup_cuda()
        dtype = torch.FloatTensor

    elif "c" not in str(params.gpu).lower():
        setup_cuda()
        dtype, backward_device = torch.cuda.FloatTensor, "cuda:" + str(params.gpu)
    else:
        setup_cpu()
        dtype, backward_device = torch.FloatTensor, "cpu"
    return dtype, multidevice, backward_device


def setup_multi_device(net_base):
    assert len(params.gpu.split(',')) - 1 == len(params.multidevice_strategy.split(',')), \
      "The number of -multidevice_strategy layer indices minus 1, must be equal to the number of -gpu devices."

    new_net_base = ModelParallel(net_base, params.gpu, params.multidevice_strategy)
    return new_net_base


# Preprocess an image before passing it to a model.
# We need to rescale from [0, 1] to [0, 255], convert from RGB to BGR,
# and subtract the mean pixel.
def preprocess(image_name, image_size):
    image = Image.open(image_name).convert('RGB')
    if type(image_size) is not tuple:
        image_size = tuple([int((float(image_size) / max(image.size))*x) for x in (image.height, image.width)])
    Loader = transforms.Compose([transforms.Resize(image_size), transforms.ToTensor()])
    rgb2bgr = transforms.Compose([transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])])])
    Normalize = transforms.Compose([transforms.Normalize(mean=[103.939, 116.779, 123.68], std=[1,1,1])])
    tensor = Normalize(rgb2bgr(Loader(image) * 256)).unsqueeze(0)
    return tensor


# Undo the above preprocessing.
def deprocess(output_tensor):
    Normalize = transforms.Compose([transforms.Normalize(mean=[-103.939, -116.779, -123.68], std=[1,1,1])])
    bgr2rgb = transforms.Compose([transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])])])
    output_tensor = bgr2rgb(Normalize(output_tensor.squeeze(0).cpu())) / 256
    output_tensor.clamp_(0, 1)
    Image2PIL = transforms.ToPILImage()
    image = Image2PIL(output_tensor.cpu())
    return image


# Preprocess an image before passing it to a model.
# We need to subtract the mean pixel.    
def preprocess_pytorch(image_name, image_size):
    Normalize = transforms.Compose([transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[1,1,1])])
    image = Image.open(image_name).convert('RGB')
    if type(image_size) is not tuple:
        image_size = tuple([int((float(image_size) / max(image.size))*x) for x in (image.height, image.width)])
    Loader = transforms.Compose([transforms.Resize(image_size), transforms.ToTensor()])
    tensor = Normalize(Loader(image)).unsqueeze(0)
    return tensor

    
# Undo the above preprocessing.
def deprocess_pytorch(output_tensor):
    Normalize = transforms.Compose([transforms.Normalize(mean=[-0.485, -0.456, -0.406], std=[1,1,1])])
    output_tensor = Normalize(output_tensor.squeeze(0).cpu())
    output_tensor.clamp_(0, 1)
    Image2PIL = transforms.ToPILImage()
    image = Image2PIL(output_tensor.cpu())
    return image
    

# Combine the Y channel of the generated image and the UV/CbCr channels of the
# content image to perform color-independent style transfer.
def original_colors(content, generated):
    content_channels = list(content.convert('YCbCr').split())
    generated_channels = list(generated.convert('YCbCr').split())
    content_channels[0] = generated_channels[0]
    return Image.merge('YCbCr', content_channels).convert('RGB')


# Print like Lua/Torch7
def print_torch(net_base, multidevice):
    if multidevice:
        return
    simplelist = ""
    for i, layer in enumerate(net_base, 1):
        simplelist = simplelist + "(" + str(i) + ") -> "
    print("nn.Sequential ( \n  [input -> " + simplelist + "output]")

    def strip(x):
        return str(x).replace(", ",',').replace("(",'').replace(")",'') + ", "
    def n():
        return "  (" + str(i) + "): " + "nn." + str(l).split("(", 1)[0]

    for i, l in enumerate(net_base, 1):
         if "2d" in str(l):
             if "AdaptiveAvgPool2d" not in str(l) and "AdaptiveMaxPool2d" not in str(l):
                 ks, st, pd = strip(l.kernel_size), strip(l.stride), strip(l.padding)
             if "Conv2d" in str(l):
                 ch = str(l.in_channels) + " -> " + str(l.out_channels)
                 print(n() + "(" + ch + ", " + (ks).replace(",",'x', 1) + st + pd.replace(", ",')'))
             elif "AdaptiveAvgPool2d" in str(l) or "AdaptiveMaxPool2d" in str(l):
                 print(n())
             elif "Pool2d" in str(l):
                 st = st.replace("  ",' ') + st.replace(", ",')')
                 print(n() + "(" + ((ks).replace(",",'x' + ks, 1) + st).replace(", ",','))
         else:
             print(n())
    print(")")


# Print planned octave image sizes
def print_octave_sizes(bsize, octave_scale, num_octaves):
    print('\nPerforming ' + str(num_octaves) + ' octaves with the following image sizes:')
    for o in range(1, num_octaves+1):
        print('  Octave ' + str(o) + ' image size: ' + \
        str( int(bsize[0]*(o*octave_scale))) +'x'+ str(int(bsize[1]*(o*octave_scale))) )
    print()
        
        
# Divide weights by channel size
def normalize_weights(dream_losses):
    for n, i in enumerate(dream_losses):
        i.strength = i.strength / max(i.target_size)


# Rescale tensor
def rescale_tensor(tensor, sf, mode='bilinear'):
    return torch.nn.functional.interpolate(tensor.clone(), scale_factor=(sf,sf), mode=mode, align_corners=True)

 
# Resize tensor
def resize_tensor(tensor, size, mode='bilinear'):
    return torch.nn.functional.interpolate(tensor.clone(), size=size, mode=mode, align_corners=True)

    
# Prepare input image
def new_img(input_image, scale_factor, mode='bilinear'):
    img = input_image.clone()
    if scale_factor != -1:
        img = rescale_tensor(img, scale_factor, mode)
    img = nn.Parameter(img) 
    return img

   
# Shift tensor, possibly randomly. 
def roll_tensor(tensor, h_shift=None, w_shift=None):
    if h_shift == None:
        h_shift = random.randint(-params.jitter, params.jitter)
    if w_shift == None:
        w_shift = random.randint(-params.jitter, params.jitter)
    tensor = torch.roll(torch.roll(tensor, shifts=h_shift, dims=2), shifts=w_shift, dims=3)
    return tensor, hs, ws

    
# Apply pixel jitter 
def pixel_jitter(tensor, jit_val=5):
    jit_tensor = torch.randn_like(tensor) * jit_val
    return tensor + jit_tensor
        
        
# Define an nn Module to rank channels based on activation strength
class RankChannels(torch.nn.Module):

    def __init__(self, channels, channel_mode):
        super(RankChannels, self).__init__()
        self.channels = channels
        self.channel_mode = channel_mode  

    def sort_channels(self, input):
        channel_list = []
        for i in range(input.size(1)):         
            channel_list.append(torch.mean(input.clone().squeeze(0).narrow(0,i,1)).item())        
        return sorted((c,v) for v,c in enumerate(channel_list)) 

    def get_middle(self, sequence):
        num = int(self.channels[0])
        m = (len(sequence) - 1)//2 - num//2
        return sequence[m:m+num]

    def rank_channel_list(self, input):
        top_channels = int(self.channels[0])
        channel_list = self.sort_channels(input)
    
        if 'strong' in self.channel_mode:
            channel_list.reverse()
        elif 'avg' in self.channel_mode:
            channel_list = self.get_middle(channel_list)
            
        channels = []   
        for i in range(top_channels):
            channels.append(channel_list[i][1])
        return channels
        
    def create_mask(self, input, cl=None):
        mask = torch.zeros_like(input)
        if cl == None:
            masked_vals = self.rank_channel_list(input)
        else:
            masked_vals = cl        
        for c in range(input.size(1)):
            if c in masked_vals:
                mask[0, c] = 1
            else: 
                mask[0, c] = 0          
        return mask

    def forward(self, input):
        if '-1' not in self.channels:
            channel_list = self.rank_channel_list(input)
        else:
            channel_list = self.channels    
        return channel_list
        

class ChannelLoss(torch.nn.Module):

    def __init__(self, channels, channel_mode):
        super(ChannelLoss, self).__init__()
        self.get_channels = RankChannels(channels, channel_mode)
        self.channel_mode = channel_mode
        self.channels = channels       
        
    def capture_channels(self, input):
        if 'all' not in self.channel_mode: 
            self.channels = self.get_channels(input)               
        elif '-1' not in self.channels: 
            self.channels = [int(c) for c in self.channels]
        else:
            self.channels = None
            
        
# Define an nn Module to compute DeepDream loss
class DreamLossType(torch.nn.Module):

    def __init__(self, loss_mode):
        super(DreamLossType, self).__init__()
        self.get_mode(loss_mode)
               
    def get_mode(self, loss_mode):
        self.loss_mode_string = loss_mode
        if loss_mode.lower() == 'norm':
           self.loss_mode = self.norm_loss
        elif loss_mode.lower() == 'mean':
           self.loss_mode = self.mean_loss
        elif loss_mode.lower() == 'mse':
           self.crit = torch.nn.MSELoss()
           self.loss_mode = self.crit_loss
        elif loss_mode.lower() == 'bce':
           self.crit = torch.nn.BCEWithLogitsLoss()
           self.loss_mode = self.crit_loss
           
    def norm_loss(self, input):
        return input.norm()
        
    def mean_loss(self, input):
        return input.mean()
        
    def crit_loss(self, input, target):   
        return self.crit(input, target)

    def forward(self, input):
        if self.loss_mode_string != 'bce' or self.loss_mode_string != 'mse':
            loss = self.loss_mode(input) 
        else: 
            target = torch.zeros_like(input.detach())
            self.crit_loss(input, target)           
        return loss
        

# Define an nn Module for DeepDream
class DeepDream(torch.nn.Module):

    def __init__(self, loss_mode, channels='-1', channel_mode='strong'):
        super(DeepDream, self).__init__()
        self.get_loss = DreamLossType(loss_mode)
        self.channel_loss = ChannelLoss(channels.split(','), channel_mode)
        
    def capture(self, input):
        self.channel_loss.capture_channels(input)
    
    def get_channel_loss(self, input):
        loss = 0
        for c in self.channel_loss.channels:  
            if input.dim() > 0:     
                if int(c) < input.size(1):
                    loss += self.get_loss(input[0, int(c)])
        return loss 
        
    def forward(self, input):
        if self.channel_loss.channels==None: 
            loss = self.get_loss(input)
        else:
            loss = self.get_channel_loss(input)
        return loss

        
# Define an nn Module to collect DeepDream loss 
class DreamLoss(torch.nn.Module):

    def __init__(self, loss_mode, strength, channels, channel_mode):
        super(DreamLoss, self).__init__()
        self.dream = DeepDream(loss_mode, channels, channel_mode)
        self.strength = strength
        self.mode = 'None'
        
    def forward(self, input):
        if self.mode == 'loss':
            self.loss = self.dream(input) * self.strength                
        elif self.mode == 'capture':
            self.target_size = input.size()
            self.dream.capture(input)
        return input


class TVLoss(nn.Module):

    def __init__(self, strength):
        super(TVLoss, self).__init__()
        self.strength = strength

    def forward(self, input):
        self.x_diff = input[:,:,1:,:] - input[:,:,:-1,:]
        self.y_diff = input[:,:,:,1:] - input[:,:,:,:-1]
        self.loss = self.strength * (torch.sum(torch.abs(self.x_diff)) + torch.sum(torch.abs(self.y_diff)))
        return input


# Define an nn Module to apply jitter 
class Jitter(torch.nn.Module):

    def __init__(self, jitter_val):
        super(Jitter, self).__init__()
        self.jitter_val = jitter_val 

    def roll_tensor(self, input):
        h_shift = random.randint(-self.jitter_val, self.jitter_val)
        w_shift = random.randint(-self.jitter_val, self.jitter_val)
        return torch.roll(torch.roll(input, shifts=h_shift, dims=2), shifts=w_shift, dims=3)        
        
    def forward(self, input):   
        input = self.roll_tensor(input)
        return input



if __name__ == "__main__":
    main()