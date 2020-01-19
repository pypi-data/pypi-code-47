import torch
from torchvision import transforms
from person_tracking.fractal.loaders import ListDataset
from person_tracking.fractal.vis_lib.vis_utils import save_img_with_labels
from person_tracking.fractal.common_utils.img_utils import reframe_bboxes_for_actual_image, clamper
from person_tracking.fractal.nets.darknet import Darknet_yolo
from person_tracking.fractal.anchors import get_anchors
# from fractal.loaders import ListDataset
# from fractal.vis_lib.vis_utils import save_img_with_labels
# from fractal.common_utils.img_utils import reframe_bboxes_for_actual_image, clamper
# from fractal.nets.darknet import Darknet_yolo
# from fractal.anchors import get_anchors
import os
import warnings
import numpy as np
warnings.filterwarnings('ignore')
import time
from PIL import Image
import cv2
import progressbar
import sys
# import dlib
import matplotlib.pyplot as plt
# from heatmappy import Heatmapper
#pip install heatmappy

from fractal.deep_sort import preprocessing
from fractal.deep_sort import nn_matching
from fractal.deep_sort.detection import Detection
from fractal.deep_sort.tracker import Tracker
from fractal.deep_sort.detection import Detection as ddet
from fractal.deep_sort.feature_extractor import Extractor

from fractal.superai.Nets.resnets import resnet18

class Inference:
    def __init__(self, cfg,tracker=None, extractor=None, iou = 0.5, conf = 0.5, heatmap=False, classifier=None):
        self.cfg = cfg
        self.model_name = cfg["model_stuff"]["model_name"]
        self.strides = cfg["arch"]["strides"]
        self.anchor_ratios = cfg["arch"]["anchor_ratios"]
        self.input_size = cfg["detection"]["input_size"]
        self.num_classes = cfg["data"]["num_classes"]
        self.num_anchors = len(cfg["arch"]["anchor_ratios"]) * len(cfg["arch"]["strides"])
        self.scale = cfg["arch"]["scale"]
        self.model = Darknet_yolo(num_classes=self.num_classes, anchors = self.num_anchors, scale = self.scale)
        self.model_weights = torch.load(cfg["detection"]["use_pretrained_weights_loc"])
        self.model.load_weights_manually(cfg["detection"]["use_pretrained_weights_loc"])

        self.encode = get_anchors(self.model_name)(self.strides,self.anchor_ratios,self.input_size)

        self.enc_anchors = self.encode.all_anchors_ft_scale.unsqueeze(0).clone()
        self.enc_strides = self.encode.all_anchors_strides.clone()
        self.heatmap=heatmap

        if self.cfg["device"]["use_gpu"]:
            self.model = self.model.cuda()
            self.enc_anchors = self.enc_anchors.cuda()
            self.enc_strides = self.enc_strides.cuda()

        self.labels_mapping = self.labels_mapper(cfg["data"]["labels_data"])
        self.iou = iou
        self.conf = conf
        self.tracker = tracker
        self.extractor = extractor
        # self.face_detector =  dlib.get_frontal_face_detector()
        self.face_detector = None
        self.track_list = {}
        self.idx = 0
        self.dwell_time = {}
        self.classifier = classifier
        self.face_detect = cfg["face_detection"]

    def infer_img(self, input_image_loc):
        """
        Extracts image from a given location, predicts it throgh the model and returns the image along with predicted bbox coordinates, 
        probabilities and labels
        """
        orig_img, img_tensor, shape = ListDataset.prep_image(input_image_loc, (self.input_size, self.input_size))
        if self.cfg["device"]["use_gpu"]:
            img_tensor = img_tensor.cuda()
        outputs = self.model.predict(img_tensor.cuda(), self.enc_anchors, self.enc_strides, iou = self.iou, conf=self.conf)
        # Filters to apply for which classes to use. If need all the classes, remove this bit.
        if not isinstance(outputs, int):
            outputs = outputs[outputs[:,7]==0]

        try:
            if not isinstance(outputs, int):
                h, w = shape 
                ow, oh = img_tensor.size()[2:]
                coord = outputs[:, 1:5]
                prob_scores = outputs[:, 6]
                labels  = outputs[:, 7]
                final_coord = reframe_bboxes_for_actual_image([h, w], [oh, ow], coord)
                final_coord = clamper(final_coord, [h, w])
                final_coord = final_coord.cpu().numpy()
                prob_scores = prob_scores.cpu().numpy()
                labels =  labels.cpu().numpy()
                return orig_img,final_coord, prob_scores, labels
            else:
                return orig_img,0,0,0
        except:
            return orig_img,0,0,0

    def infer_img_list(self, images_root, fnames, save_text = None, save_folder=None):
        """
        Infers a list of images, with their paths indicated with images_root and fnames, prints predicitons text file and 
        saves images with bounding boxes.
        """
        if not os.path.exists(save_folder):
           os.makedirs(save_folder)
        
        fnames = sorted(fnames)
        bar = progressbar.ProgressBar(maxval=len(fnames)).start()

        self.track_list ={}

        for num, img in enumerate(fnames):
            orig_img, coord, prob_scores, labels = self.infer_img(images_root+img)

            if isinstance(coord, int):
                if save_folder:
                    img_name = img.strip().split('/')[-1]
                    orig_img.save(save_folder+img_name)
            else:
                if save_folder:
                    img_name = img.strip().split('/')[-1]
                    frame = np.asarray(orig_img)
                    #coord=coord[np.where(prob_scores>0.9)]
                    #labels=labels[np.where(prob_scores>0.9)]
                    #prob_scores=prob_scores[np.where(prob_scores>0.9)]
                    if self.tracker:
                        frame = self.tracking(coord,frame, num, orig_img)
                        im = Image.fromarray(np.uint8(frame))
                        if self.heatmap:
                            im= self.heatmapper(im, coord)
                        im.save(save_folder + img_name)
                    else:
                        save_img_with_labels(orig_img, coord, prob_scores, labels,
                                                self.labels_mapping,
                                                save_loc=save_folder + img_name) 
            bar.update(num)
        bar.finish()       

    def labels_mapper(self,txtfile):
        """
        Reads the labels text file and returns labels against the respective class number in the dictionary.
        """
        labels = [i.split()[0] for i in open(txtfile, "r")]
        mapping = {i: labels.index(i) for i in labels}
        labels_mapping = {v:k for k, v in mapping.items()}
        return labels_mapping

    def tracking(self, coord, frame, frame_num, orig_img):
        boxs = np.empty_like(coord)
        boxs[:, 3] = coord[:,3] - coord[:,1]
        boxs[:, 2] = coord[:,2] - coord[:,0]
        boxs[:,1] = coord[:,1]
        boxs[:,0] = coord[:,0] 
        boxs = boxs.tolist()
        features = _get_features(frame, coord,self.extractor)
        detections = [Detection(bbox, 1.0, feature) for bbox, feature in zip(boxs, features)]               
        self.tracker.predict()
        self.tracker.update(detections)
        if self.face_detect:
            faces = self.face(frame)
        for track in self.tracker.tracks:
            if track.is_confirmed() and track.time_since_update >1 :
                continue                
            bbox = track.to_tlbr()
            if track.track_id in self.dwell_time:
                self.dwell_time[track.track_id][1] = frame_num
            else:
                self.dwell_time[track.track_id] = [frame_num, frame_num]
            # To classify betweek staff and customers
            if self.classifier:
                if track.track_id not in self.track_list :
                    self.track_list[track.track_id] = {}
                    self.track_list[track.track_id]["age"] = 0
                    self.track_list[track.track_id]["category"] = 0
                if self.track_list[track.track_id]["age"] < 25:
                    roi = orig_img.crop((int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])))
                    #roi.save("a.jpg")
                    category = self.classifier.predict_class(roi)
                    self.track_list[track.track_id]["age"] += 1
                    self.track_list[track.track_id]["category"] = category
                if self.track_list[track.track_id]["category"]==0:
                    cv2.putText(frame, str(track.track_id),(int((bbox[0]+bbox[2])/2), int((bbox[1]+bbox[3])/2)),0, 5e-3 * 250, (0,0,0),2)
                else:
                    cv2.putText(frame, str(track.track_id),(int((bbox[0]+bbox[2])/2), int((bbox[1]+bbox[3])/2)),0, 5e-3 * 250, (255,165,0),2)
            else:
                cv2.putText(frame, str(track.track_id),(int((bbox[0]+bbox[2])/2), int((bbox[1]+bbox[3])/2)),0, 5e-3 * 250, (255,165,0),2)
            """
            if track.track_id not in self.track_list:
                self.idx+=1
                print (self.idx)
                roi = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])].copy()
                name = "distinct/%05d.jpg" % (self.idx)
                self.track_list.append(track.track_id)
                cv2.imwrite(name,cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
            
            #cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(255,255,255), 2)

            #cv2.putText(frame, str(track.track_id),(int((bbox[0]+bbox[2])/2), int((bbox[1]+bbox[3])/2)),0, 5e-3 * 250, (0,0,0),2)
            """

        for det in detections:
            bbox = det.to_tlbr()
            #cv2.rectangle(frame,(int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(255,0,0), 2)
        cv2.putText(frame, "Number of people in current frame: %d" %(len(detections)), (20,60), 0, 5e-3 * 250, (255,255,255), 2 )
        if self.face_detect:
            for bbox in faces:
                cv2.rectangle(frame,(int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(0,0,255), 2)
        return frame
    
    def face(self,image):
        dets = self.face_detector(image,1)
        faces = []
        for i, d in enumerate(dets):
            xmin = min(d.left(),d.right())
            xmax = max(d.left(),d.right())
            ymin = min(d.top(), d.bottom())
            ymax = max(d.top(), d.bottom())
            faces.append([xmin,ymin,xmax,ymax])
        return faces

    def heatmapper(self, img, coord):
        points = []
        for crd in coord:
            ymin = min(int(crd[1]), int(crd[3]))
            xmin = min(int(crd[0]), int(crd[2]))
            ymax = max(int(crd[1]), int(crd[3]))
            xmax = max(int(crd[0]), int(crd[2]))
            X = np.arange(xmin - int(0.1*(xmax-xmin)),xmax - int(0.1*(xmax-xmin)) , 200)
            Y = np.arange(ymin,ymax, 200)
            pts = np.array(np.meshgrid(X, Y)).T.reshape(-1,2)
            pts = pts.tolist()
            points += pts
        heatmapper = Heatmapper(point_diameter=600)
        img = heatmapper.heatmap_on_img(points, img)
        return img
    
    def update_track(self, coord, frame, num, orig_img, save_folder):
        if self.tracker:
            frame = self.tracking(coord,frame, num, orig_img)
            im = Image.fromarray(np.uint8(frame))
            im.save(save_folder + img_name)
        else:
            save_img_with_labels(orig_img, coord, prob_scores, labels, labels_mapping, save_loc=save_folder + img_name)

def split_video_to_frames_ffmpeg(video_path, folder_root, name_template='img_%05d.png'):
    """
    splits a particular video into frams and saves the at mentioned folder_root
    """
    print("Splitting video to frames")
    os.system("mkdir -p {}".format(folder_root))
    cmd = 'ffmpeg -loglevel panic  -i {} -b:v 4500k {}/{}'.format(video_path, folder_root, name_template)
    start = time.time()
    os.system(cmd)
    end = time.time()
    print("{}: time: {}".format(os.path.basename(video_path), end - start))

def get_file_list(path):
    """
    gets list of file locations from a text file or folder
    """
    fnames = []
    if os.path.isfile(path):
        with open(path) as f:
            lines = f.readlines()

        for line in lines:
            splited = line.strip().split()
            fnames.append(splited[0])
    else:
        for file in os.listdir(path):
            fnames.append(file)
    return fnames

def save_text_preds(img_name, coord, prob_scores, labels, opener):
    """
    save the predictions of image in a text file. Very IMP change in change of coordinate system
    """
    adder = img_name
    coord = coord[:, [1,0, 3, 2]] ## xyxy to yxyx
    for xyxy, prob, label in zip(coord, prob_scores, labels):
        xyxy = list(xyxy)
        prob = str(float(prob))
        label = str(int(label))
        joiner = " " +" ".join([str(i) for i in xyxy])+ " "+label+ " "+prob
        adder +=joiner
    opener.write("{} \n".format(adder))

def fram_to_vid(pred_frames, destination, name_template):
    """
    recombines frames present in specified folder to a video.
    """
    print ("Recombining video frames to video")
    cmd = 'ffmpeg -loglevel panic -i {}{} -b:v 4500k -y {}'.format(pred_frames, name_template, destination)
    os.system(cmd)

def _get_features(ori_img, bbox_xyxy, extractor):
        features = []
        for box in bbox_xyxy:
            x1,y1,x2,y2 = box
            im = ori_img[int(y1):int(y2),int(x1):int(x2)]
            feature = extractor(im)[0]
            features.append(feature)
        
        if len(features) > 0:
            features = np.stack(features, axis=0)
        
        return features

class Classification:
    def __init__(self, cfg):
        self.model = resnet18(cfg["classification"]["num_classes"], pretrained=True)
        save = torch.load(cfg["classification"]["weights_loc"])
        self.use_gpu = cfg["device"]["use_gpu"]
        if self.use_gpu:
            self.model = self.model.cuda()
        self.model.load_state_dict(save["model_weights"])
        self.model = self.model.eval()
        
        
        self.image_transforms = []
        self.image_transforms.append(transforms.Resize((224,224)))
        self.image_transforms.append(transforms.ToTensor())
        self.image_transforms.append(transforms.Normalize((0.6357,  0.5425,  0.4426), (0.2740,  0.2873,  0.3129)))
        
        self.composed_transforms = transforms.Compose(self.image_transforms)
    
    def predict_class(self, inputs):
        img_tensor = self.composed_transforms(inputs)
        img_tensor = img_tensor.unsqueeze(0)
        if self.use_gpu:
            img_tensor = img_tensor.cuda()
        outputs = self.model(img_tensor)
        outputs = torch.nn.functional.softmax(outputs)
        outputs = outputs.squeeze()
        category = outputs.max(0)[1].item()
        return category