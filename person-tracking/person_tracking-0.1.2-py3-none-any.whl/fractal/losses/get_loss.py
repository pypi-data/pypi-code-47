import torch
from fractal.losses.yolov3_loss import Yolov3_loss

def get_loss(loss_type):
    if loss_type == "yolov3_loss":
        print("Using yolov3 loss model")
        return Yolov3_loss
    else:
        raise NotImplementedError("We haven't implemented these Loss function yet. Please raise a pull request if it is useful")