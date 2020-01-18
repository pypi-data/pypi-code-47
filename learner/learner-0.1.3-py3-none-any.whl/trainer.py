"""Trainer can help the leaner to update model based on data"""
from collections import defaultdict

import pandas as pd
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from . import metrics

OPTIMS = {
    'asgd':     optim.ASGD,
    'adadelta': optim.Adadelta,
    'adagrad':  optim.Adagrad,
    'adam':     optim.Adam,
    'rmsprop':  optim.RMSprop,
    'sgd':      optim.SGD
}

LOSSES = {
    'bce_loss':                     nn.modules.loss.BCELoss,
    'bce_with_logits_loss':         nn.modules.loss.BCEWithLogitsLoss,
    'ctc_loss':                     nn.modules.loss.CTCLoss,
    'cosine_embedding_loss':        nn.modules.loss.CosineEmbeddingLoss,
    'cross_entropy_loss':           nn.modules.loss.CrossEntropyLoss,
    'hinge_embedding_loss':         nn.modules.loss.HingeEmbeddingLoss,
    'kl_div_loss':                  nn.modules.loss.KLDivLoss,
    'l1_loss':                      nn.modules.loss.L1Loss,
    'mse_loss':                     nn.modules.loss.MSELoss,
    'margin_ranking_loss':          nn.modules.loss.MarginRankingLoss,
    'multi_label_margin_loss':      nn.modules.loss.MultiLabelMarginLoss,
    'multi_label_soft_margin_loss': nn.modules.loss.MultiLabelSoftMarginLoss,
    'multi_margin_loss':            nn.modules.loss.MultiMarginLoss,
    'nll_loss':                     nn.modules.loss.NLLLoss,
    'poisson_nll_loss':             nn.modules.loss.PoissonNLLLoss,
    'smooth_l1_loss':               nn.modules.loss.SmoothL1Loss,
    'soft_margin_loss':             nn.modules.loss.SoftMarginLoss,
    'triplet_margin_loss':          nn.modules.loss.TripletMarginLoss
}

METRICS = {
    'binary_accuracy':      metrics.binary_accuracy,
    'categorical_accuracy': metrics.categorical_accuracy
}


class TrainHistory(object):
    """Train history of a Neural Network Model
    """

    def __init__(self):
        self._epoches = None
        self._fields = None
        self._history = defaultdict(list)

    @property
    def epoches(self):
        """Return the number of stored epoches
        """
        return self._epoches

    def is_empty(self):
        """Return True if it's an empty History object
        """
        return not bool(self._epoches)

    def add(self, epoch, **record):
        assert isinstance(epoch, int) and (epoch >= 0), 'epoch must be a non-negative integer'
        assert 'loss' in record.keys(), 'loss must be recorded in the history.'
        if self.is_empty():
            assert epoch == 0, "The number of epoch starts from 0."
            if not self._fields:
                self._fields = list(record.keys())
        else:
            assert epoch == (self.epoches + 1), "The epoch must be increased one by one"
            assert set(self._fields) == set(record.keys())
        self._history['epoch'].append(epoch)
        for field in self._fields:
            self._history[field].append(record[field])

    @property
    def history(self):
        """Return the history in pandas.DataFrame format
        """
        return pd.DataFrame(self._history).set_index('epoch')

    def __repr__(self):
        if "epoch" in self._history:
            return "TrainHistory(epoches={})".format(self.epoches)
        else:
            return "<Empty TrainHistory object>"


class Trainer:
    """Base Class for Trainer"""

    def __init__(self):
        pass

    def train_model(self, model, data):
        raise NotImplementedError


class SGDTrainer(Trainer):
    """A general trainer based on SGD"""

    def __init__(self, criterion=None, optimizer=None):
        super().__init__()
        self.criterion = criterion
        self.optimizer = optimizer

    def train_model(self, model: nn.Module, dataloader: DataLoader):
        for x, y in dataloader:
            self.optimizer.zero_grad()
            out = model(x)
            loss = self.criterion(out, y)
            loss.backward()
            self.optimizer.step()


if __name__ == '__main__':
    pass
