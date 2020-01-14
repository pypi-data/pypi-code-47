import torch
import logging
from hyperdash import Experiment
from pathlib import Path
from typing import Any, Dict, Optional
import click
import sys
import os

from .utils import get_config, get_model

from quarks2_fractal.utils.metrics import get_metric
from quarks2_fractal.utils.train import TrainEpoch, ValidEpoch
from quarks2_fractal.classifier import ClsModel
from quarks2_fractal.utils.cls_losses import get_losses
from quarks2_fractal.utils.optims import get_optim
from quarks2_fractal.datasets import get_dataloader
from quarks2_fractal.utils.scheduler import get_scheduler

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def hyperdash_params(*, exp, params: dict) -> None:
    [exp.param(param, params[param]) for param in params]

def hyperdash_metrics(*, exp, metrics: Dict[str, float]) -> None:
    [exp.metric(metric, metrics[metric]) for metric in metrics]

def add_hyperdash_metrics(*, exp, all_metrics: Dict[str, Dict[str, float]]):
    for metric_type, metrics in all_metrics.items():
        params = {
            f"{metric_type}_{metric_label}": value
            for metric_label, value in metrics.items()
        }
        hyperdash_metrics(exp=exp, metrics=params)

def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def checkpoint_model(*, model, work_dir,  label, metric: float, epoch: int):
    model_path = Path(f"{label}_{epoch:0>2d}_{metric:.3f}")
    torch.save(model.state_dict(), work_dir+"/"+str(model_path))

def load_checkpoint(model, loc):
    weights = torch.load(loc, map_location="cpu")
    model.load_state_dict(weights)
    return int(loc.rsplit("_")[-2])

def setup_logger(name, save_dir, filename="log.txt"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # don't log results for the non-master process
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if save_dir:
        fh = logging.FileHandler(os.path.join(save_dir, filename))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def train(config:dict):
    start_epochs = 1
    logger = setup_logger("quarks2", config.work_dir)
    logger.info("Running with config:\n{}".format(config))
    exp = Experiment(config.exp_name)
    hyperdash_params(exp=exp, params=config)
    train_dl, val_dl = get_dataloader(config)
    model = get_model(config)
    if config.fine_tune:
        logger.info("loading checkpint from :{}".format(config.fine_tune))
        start_epochs = load_checkpoint(model, config.fine_tune)
        start_epochs+=1

    metrics = get_metric(config)
    optimizer = get_optim(config, model)
    loss = get_losses(config)
    scheduler = get_scheduler(config, optimizer)

    train_epoch = TrainEpoch(model, loss=loss, metrics=metrics, optimizer=optimizer, device=get_device(), verbose=True, schedular=scheduler)
    valid_epoch = ValidEpoch(model, loss=loss, metrics=metrics, device=get_device(), verbose=True)
    
    max_score = 0

    for ep in range(start_epochs, config.epochs + 1):
        logger.info(f"Running epoch: {ep}")
        train_logs = train_epoch.run(train_dl)
        val_logs = valid_epoch.run(val_dl)
        add_hyperdash_metrics(
            exp=exp, all_metrics={"train": train_logs, "val": val_logs}
        )
        metric_label = config["metrics"][0]
        logger.info("train logs:\n{}".format(train_logs))
        logger.info("val logs:\n{}".format(val_logs))
        if max_score < val_logs[metric_label]:
            max_score = val_logs[metric_label]
            checkpoint_model(label=config.exp_name, work_dir=config.work_dir, model=model, metric=max_score, epoch=ep)

@click.command()
@click.option("-c", "--config_path", required=True, help="Path to config file")
def main(config_path: str):
    from easydict import EasyDict as edict 
    config = get_config(config_path)
    train(config=config)

if __name__ == "__main__":
    main()