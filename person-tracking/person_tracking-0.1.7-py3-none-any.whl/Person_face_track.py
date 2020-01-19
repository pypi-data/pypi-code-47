import time
import torch 
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2 
from person_tracking.fractal.nets.darknet import Darknet_yolo
# from fractal.nets.darknet import Darknet_yolo
import random 
import argparse
import pickle as pkl
import torchvision.transforms as transforms
import json
import os
from person_tracking.fractal.anchors import get_anchors
from person_tracking.infer_utils import Inference, Classification, split_video_to_frames_ffmpeg, get_file_list, save_text_preds, fram_to_vid
# from fractal.anchors import get_anchors
# from infer_utils import Inference, Classification, split_video_to_frames_ffmpeg, get_file_list, save_text_preds, fram_to_vid

from person_tracking.fractal.deep_sort import preprocessing
from person_tracking.fractal.deep_sort import nn_matching
from person_tracking.fractal.deep_sort.detection import Detection
from person_tracking.fractal.deep_sort.tracker import Tracker
from person_tracking.fractal.deep_sort.detection import Detection as ddet
from person_tracking.fractal.deep_sort.feature_extractor import Extractor
# from fractal.deep_sort import preprocessing
# from fractal.deep_sort import nn_matching
# from fractal.deep_sort.detection import Detection
# from fractal.deep_sort.tracker import Tracker
# from fractal.deep_sort.detection import Detection as ddet
# from fractal.deep_sort.feature_extractor import Extractor

parser = argparse.ArgumentParser(description="Inference on image/list of images")
parser.add_argument("-cfg", "--cfg", default="cfgs/coco.json")
parser.add_argument("-vloc", "--video_location", help="Video location", default=None)
parser.add_argument("-sii", "--save_predictions_img", help="The folder where predicted image with bounding box will be saved ", default='../tmp_pred/')
parser.add_argument("-save", "--save_video_loc", default = "result.mp4")
args = parser.parse_args()

def Model(cfg_path: str):
    with open(cfg_path) as fp:
        cfg = json.load(fp)

    extractor = Extractor(cfg["tracking"]["weights_loc"], use_cuda=True)

    metric = nn_matching.NearestNeighborDistanceMetric(cfg["tracking"]["metric"], cfg["tracking"]["max_cosine_distance"], cfg["tracking"]["nn_budget"])
    tracker = Tracker(metric, max_iou_distance=cfg["tracking"]["max_iou_distance"], max_age=cfg["tracking"]["max_age"], n_init=cfg["tracking"]["n_init"])

    if cfg["classification"]["classify"]:
        classifier = Classification(cfg)
    else:
        classifier=None

    model = Inference(cfg, tracker, extractor, heatmap=cfg["heatmap"], classifier=classifier)
    return model

'''
model = Model(args.cfg)
start = time.time()

vid_root = args.video_location
fram_root = '../tmp/'
if not os.path.exists(fram_root):
    os.mkdir(fram_root)
# split_video_to_frames_ffmpeg(vid_root, fram_root, name_template='img_%05d.png')
fnames = get_file_list(fram_root)
model.infer_img_list(fram_root, fnames, save_folder=args.save_predictions_img)
print ("Dwell times for individual ID's of frames: ", model.dwell_time)

fram_to_vid(args.save_predictions_img, args.save_video_loc, name_template = 'img_%05d.png')
print (time.time()-start)
'''

'''
for vid in os.listdir('chunks'):
    vid_root = 'chunks/' + vid
    fram_root = './tmp/'
    if not os.path.exists(fram_root):
        os.mkdir(fram_root)
    split_video_to_frames_ffmpeg(vid_root, fram_root, name_template='img_%05d.png')
    fnames = get_file_list(fram_root)
    model.infer_img_list(fram_root, fnames, save_folder=args.save_predictions_img)

#fram_to_vid(args.save_predictions_img, args.save_video_loc, name_template = 'img_%05d.png')
print (time.time()-start)
'''