import torch 

def vflip(img):
    return img.flip(-2)

def hflip(img):
    return img.flip(-1)

def normalize(tensor, mean, std):
    dtype = tensor.dtype
    mean = torch.as_tensor(mean, dtype=dtype, device=tensor.device)
    std = torch.as_tensor(std, dtype=dtype, device=tensor.device)
    tensor.sub_(mean[:, None, None]).div_(std[:, None, None])
    return tensor