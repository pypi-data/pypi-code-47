import torch
from person_tracking.fractal.anchors.anchors_generator import Yolov3
# from fractal.anchors.anchors_generator import Yolov3

def get_anchors(model_name):
    if model_name == "yolov3":
        print("Using yolov3 model")
        return Yolov3
    else:
        raise NotImplementedError("We haven't implemented these anchor boxes yet. Please raise a pull request if it is useful")