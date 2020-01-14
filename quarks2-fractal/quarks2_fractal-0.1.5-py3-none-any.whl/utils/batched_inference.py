import click 
import torch
from tqdm import tqdm  
from sklearn.metrics import fbeta_score
import pandas as pd
from quarks2_fractal.engine.utils import get_config, get_model
from quarks2_fractal.engine.infer import call_output_activation_func
from quarks2_fractal.datasets.agu import get_transforms
from quarks2_fractal.datasets.datasets import ImageFolder

@click.command()
@click.option("-c", "--config_path", required=True, help="Path to config file")
@click.option("-w", "--weights", required=True, help="Path to weight file")
@click.option("-l", "--labels", required=True, help="Path to labels file")
@click.option("-i", "--img_folder", required=True, help="Path to image folder")
@click.option("-csv", "--csv_path", default="data/val_output.csv", help="path to save csv")

def batched_inference(config_path: str, weights: str, labels: str, img_folder: str, csv_path: str):
    lab = [i.strip() for i in open(labels, "r")]
    config = get_config(config_path)
    _, val_transforms = get_transforms(config)
    dl = ImageFolder(img_root=img_folder, transforms=val_transforms)
    dataloader = torch.utils.data.DataLoader(dl, batch_size=config.batch_size, shuffle=False, num_workers=config.num_workers)
    model = get_model(config)
    if "https://" in weights:
        state_dict = torch.hub.load_state_dict_from_url(weights, map_location=lambda storage, location:storage)
    else:
        state_dict = torch.load(weights,  map_location=lambda storage, location: storage)
    model.load_state_dict(state_dict)
    if torch.cuda.is_available():
        model = model.cuda()
    model = model.eval()
    locs = []
    label_names = []
    labels = []
    probs = []
    with tqdm(dataloader) as iterator:
        for x, loc in iterator:
            x = x.to("cuda")
            pred = model(x)
            out_act = [torch.nn.Softmax()(i) for i in pred]
            argmax = [int(i.argmax()) for i in out_act]
            maxi = [i.max() for i in out_act]
            label = [lab[i] for i in argmax]
            prob = [float(i.cpu().detach().numpy()) for i in maxi]
            [locs.append(i) for i in loc]
            [label_names.append(i) for i in label]
            [labels.append(i) for i in argmax]
            [probs.append(i) for i in prob]

    d = {'img_loc': locs, 'label_name': label_names, 'label': labels, 'probability': probs}
    df = pd.DataFrame(d)
    df.to_csv(csv_path, index=False)
