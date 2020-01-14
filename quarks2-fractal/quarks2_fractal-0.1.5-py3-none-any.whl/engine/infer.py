""" Fractal AI research
"""
import torch
import click 
import cv2 
import glob
import pandas as pd

from tqdm import tqdm  
from typing import List

from .utils import get_config, get_model

from quarks2_fractal.datasets.agu import get_transforms
from quarks2_fractal.datasets.datasets import CSVDataloader, JsonDataloader

def call_dataset(config: dict):
    if config.dataset_type == "csv":
        return CSVDataloader.infer
    if config.dataset_type == "json":
        return JsonDataloader.infer
    else:
        raise ValueError("The following dataloader is not written")


def call_output_activation_func(config: dict):
    if config.activation == "softmax":
        return torch.nn.Softmax(dim=1)
    else:
        raise ValueError("This activation function is not available. please raise an issue or PR if required")

def load_essentials(config: dict, weights: str):
    _, transforms = get_transforms(config)
    read_img = call_dataset(config)
    model = get_model(config)
    if "https://" in weights:
        state_dict = torch.hub.load_state_dict_from_url(weights, map_location=lambda storage, location:storage)
    else:
        state_dict = torch.load(weights,  map_location=lambda storage, location: storage)
    model.load_state_dict(state_dict)
    if torch.cuda.is_available():
        model = model.cuda()
    model = model.eval()
    return read_img, transforms, model

class InferClassification():
    def __init__(self, config_path, weights, labels, verbose=True):
        self.config = get_config(config_path)
        self.verbose = verbose
        self.read_img, self.transforms, self.model = load_essentials(self.config, weights)
        self.labels = [i.strip() for i in open(labels, "r")]

    def predict(self, img_loc):
        with torch.no_grad():
            img, _ = self.read_img(img_loc, self.transforms)
            out = self.model(img)
        out_act = call_output_activation_func(self.config)(out)
        argmax = int(out_act.argmax(1))
        maxi = out_act.max()
        label = self.labels[argmax]
        fout = {"label": label, "prob": float(maxi.cpu())}
        if self.verbose:
            print(fout)
        return fout

def infer_img(config_path: str, img_loc: str, weights: str, verbose: bool=True):
    config = get_config(config_path)
    read_img, transforms, model = load_essentials(config, weights)
    with torch.no_grad():
        img, _ = read_img(img_loc, transforms)
        out = model(img)
    out_act = call_output_activation_func(config)(out)
    labels = [i.strip() for i in open(config.labels, "r")]
    argmax = int(out_act.argmax(1))
    maxi = out_act.max()
    label = labels[argmax]
    fout = {"label": label, "prob": float(maxi.cpu())}
    if verbose:
        print(fout)
    return fout

def infer_many(config_path: str, list_of_imgs: List[str], weights: str):
    output = []
    config = get_config(config_path)
    labels = [i.strip() for i in open(config.labels, "r")]
    read_img, transforms, model = load_essentials(config, weights)
    with torch.no_grad():
        for img_loc in tqdm(list_of_imgs):
            img, _ = read_img(img_loc, transforms)
            out = model(img)
            out_act = call_output_activation_func(config)(out)
            argmax = int(out_act.argmax(1))
            maxi = out_act.max()
            label = labels[argmax]
            output.append([img_loc, label, float(maxi.cpu().numpy())])
    data = pd.DataFrame(output)
    data.columns = ["img_loc", "label", "prob"]
    return data

def infer_video(config_path:dict, video_loc: str, weights: str, save_loc: str="predict.mp4"):
    config = get_config(config_path)
    read_img, transforms, model = load_essentials(config, weights)
    video = cv2.VideoCapture(video_loc) #"/nfs/72_datasets/truth_initiative/title_01_cut_01.mp4"
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    out = cv2.VideoWriter(save_loc,fourcc, video.get(5), (frame_width,frame_height))
    labels = [i.strip() for i in open(config.labels, "r")]
    counter = 0
    output = []
    while True:
        ret, image = video.read()
        if not ret:
            break 
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = transforms(image=image2)["image"]
        with torch.no_grad():
            if torch.cuda.is_available():
                img = img.cuda()
            outx = model(img.unsqueeze(0))
            outx = call_output_activation_func(config)(outx).detach().cpu().numpy()
        argmax = int(outx.argmax(1))
        maxi = outx.max()
        label = labels[argmax]
        text = label+": "+str(round(maxi*100, 2))+"%"
        image = cv2_img_writer(image, text)
        output.append(["frame_{}".format(counter), label, round(maxi*100, 2)])
        counter+=1
        out.write(image)
        # if cv2.waitKey(10) & 0xFF == ord('q'):
        #         break
    video.release()
    out.release()

    data = pd.DataFrame(output)
    data.columns = ["frame_num", "pred_label", "pred_prob"]
    data.to_csv(save_loc.rsplit(".")[0]+".csv", index=False)
    return out, data

def cv2_img_writer(image, text):
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    textOrg = (0, 50)
    cv2.rectangle(image, (textOrg[0] ,textOrg[1] + 100), (textOrg[0]+ 300, textOrg[1]- 20), (0, 0, 0), -1)
    cv2.putText(image, text, textOrg, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.2, (0, 0, 255), 2)
    return image
    
@click.command()
@click.option("-c", "--config_path", required=True, help="Path to config file")
@click.option("-i", "--video_loc", required=True, help="Path to img loc")
@click.option("-m", "--weights", required=True, help="model weights path")
@click.option("-s", "--save_loc", default="predict.mp4", help="loacation to save the output weight file")
def infer_video_click(config_path:dict, video_loc: str, weights: str, save_loc: str="predict.mp4"):
    out = infer_video(config_path, video_loc, weights, save_loc)
    return out

@click.command()
@click.option("-c", "--config_path", required=True, help="Path to config file")
@click.option("-i", "--img_loc", required=True, help="Path to img loc")
@click.option("-m", "--weights", required=True, help="model weights path")
def infer_img_click(config_path: str, img_loc: str, weights: str, verbose: bool=True):
    fout = infer_img(config_path, img_loc, weights, verbose)
    return fout