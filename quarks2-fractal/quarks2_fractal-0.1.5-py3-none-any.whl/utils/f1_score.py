import click 
import torch
from tqdm import tqdm  
from sklearn.metrics import fbeta_score
from quarks2_fractal.engine.utils import get_config, get_model
from quarks2_fractal.engine.infer import call_output_activation_func
from quarks2_fractal.datasets.agu import get_transforms
from quarks2_fractal.datasets.datasets import JsonDataloader

@click.command()
@click.option("-c", "--config_path", required=True, help="Path to config file")
@click.option("-w", "--weights", required=True, help="Path to weight file")
def f1_score(config_path: str, weights: str):
    config = get_config(config_path)
    _, val_transforms = get_transforms(config)
    val_dl = JsonDataloader(ann_file=config.val_loc, img_root=config.val_images_loc, transforms=val_transforms)
    val_dataloader = torch.utils.data.DataLoader(val_dl, batch_size=config.batch_size, shuffle=False, num_workers=config.num_workers)
    model = get_model(config)
    if "https://" in weights:
        state_dict = torch.hub.load_state_dict_from_url(weights, map_location=lambda storage, location:storage)
    else:
        state_dict = torch.load(weights,  map_location=lambda storage, location: storage)
    model.load_state_dict(state_dict)
    if torch.cuda.is_available():
        model = model.cuda()
    model = model.eval()
    y_t = []
    y_p = []
    with tqdm(val_dataloader) as iterator:
        for x, y in iterator:
            x = x.to("cuda")
            pred = model(x).cpu().detach().numpy()
            [y_p.append(int(ind.argmax())) for ind in pred]
            [y_t.append(int(k)) for k in y.squeeze(1).numpy()]

    print("Weighted F1 Score: {}".format(fbeta_score(y_t, y_p, average='weighted', beta=1)))