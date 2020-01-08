import torch

from torch import tensor
from functools import partial

import matplotlib.pyplot as plt

import math

#export
class TimeSeriesDataset():
    def __init__(self, x, y, d): self.x,self.y,self.d = x,y,d
    def __len__(self): return len(self.x)
    def __getitem__(self, i): return self.x[i],self.y[i],self.d[i]


class TimeSeriesDataLoader():
        def __init__(self, ds, n, s): self.ds, self.n, self.s = ds, n, s
        def __iter__(self):
            for i in range(0, len(self.ds), self.n): yield self.ds[i:i + self.n]
        def __len__(self):
            return len(range(0, len(self.ds), self.n))

class Learner():
    def __init__(self, model, opt, loss_func, dl):
        self.model,self.opt,self.loss_func,self.dl = model,opt,loss_func,dl

class Runner():
    def __init__(self, cbs=None, cb_funcs=None):
        cbs = listify(cbs)
        for cbf in listify(cb_funcs):
            cb = cbf()
            setattr(self, cb.name, cb)
            cbs.append(cb)
        self.stop, self.cbs = False, [TrainEvalCallback()] + cbs

    @property
    def opt(self):
        return self.learn.opt

    @property
    def model(self):
        return self.learn.model

    @property
    def loss_func(self):
        return self.learn.loss_func

    @property
    def dl(self):
        return self.learn.dl

    def one_batch(self, xb, yb, db):
        self.xb, self.yb, self.db = xb, yb, db
        if self.handle_callback('begin_batch'): return
        self.pred = self.model(self.xb)
        if self.handle_callback('after_pred'): return
        self.loss = self.loss_func(self.pred, self.yb)
        if self.handle_callback('after_loss') or not self.in_train: return
        self.loss.backward()
        if self.handle_callback('after_backward'): return
        self.opt.step()
        if self.handle_callback('after_step'): return
        self.opt.zero_grad()

    def all_batches(self, dl):
        self.iters = len(dl)
        for xb, yb, db in dl:
            if self.stop: break
            self.one_batch(xb, yb, db)
            self.handle_callback('after_batch')
        self.stop = False

    def fit(self, epochs, learn):
        self.epochs, self.learn = epochs, learn

        try:
            for cb in self.cbs: cb.set_runner(self)
            if self.handle_callback('begin_fit'): return
            for epoch in range(epochs):
                self.epoch = epoch
                if not self.handle_callback('begin_epoch'):
                    self.all_batches(self.dl)

                with torch.no_grad():
                    if not self.handle_callback('begin_validate'): self.all_batches(self.dl)
                if self.handle_callback('after_epoch'): break

        finally:
            self.handle_callback('after_fit')
            self.learn = None

    def handle_callback(self, cb_name):
        for cb in sorted(self.cbs, key=lambda x: x._order):
            f = getattr(cb, cb_name, None)
            if f and f(): return True
        return False


from typing import *

def listify(o):
    if o is None: return []
    if isinstance(o, list): return o
    if isinstance(o, str): return [o]
    if isinstance(o, Iterable): return list(o)
    return [o]

import re

_camel_re1 = re.compile('(.)([A-Z][a-z]+)')
_camel_re2 = re.compile('([a-z0-9])([A-Z])')
def camel2snake(name):
    s1 = re.sub(_camel_re1, r'\1_\2', name)
    return re.sub(_camel_re2, r'\1_\2', s1).lower()

class Callback():
    _order=0
    def set_runner(self, run): self.run=run
    def __getattr__(self, k): return getattr(self.run, k)
    @property
    def name(self):
        name = re.sub(r'Callback$', '', self.__class__.__name__)
        return camel2snake(name or 'callback')

# export
class TrainEvalCallback(Callback):
    def begin_fit(self):
        self.run.n_epochs = 0.
        self.run.n_iter = 0
    def after_batch(self):
        if not self.in_train: return
        self.run.n_epochs += 1. / self.iters
        self.run.n_iter += 1
    # def begin_epoch(self):
    #     self.run.n_epochs = self.epoch
    #     self.model.train()
    #     self.run.in_train = True
    # def begin_validate(self):
    #     self.model.eval()
    #     self.run.in_train = False

class AvgStats():
    def __init__(self, metrics, in_train):
        self.metrics, self.in_train = listify(metrics), in_train

    def reset(self):
        self.tot_loss, self.count = 0., 0
        self.tot_mets = [0.] * len(self.metrics)

    @property
    def all_stats(self):
        return [self.tot_loss.item()] + self.tot_mets

    @property
    def avg_stats(self):
        return [o / self.count for o in self.all_stats]

    def __repr__(self):
        if not self.count: return ""
        return f"{'train' if self.in_train else 'valid'}: {self.avg_stats}"

    def accumulate(self, run):
        bn = run.xb.shape[0]
        self.tot_loss += run.loss * bn
        self.count += bn
        for i, m in enumerate(self.metrics):
            self.tot_mets[i] += m(run.pred, run.yb) * bn


class AvgStatsCallback(Callback):
    def __init__(self, metrics):
        self.train_stats, self.valid_stats = AvgStats(metrics, True), AvgStats(metrics, False)

    def begin_epoch(self):
        self.train_stats.reset()
        self.valid_stats.reset()

    def after_loss(self):
        stats = self.train_stats if self.in_train else self.valid_stats
        with torch.no_grad(): stats.accumulate(self.run)

    def after_epoch(self):
        print(self.train_stats)
        print(self.valid_stats)


# export
class Recorder(Callback):
    def begin_fit(self):
        self.lrs, self.losses = [], []

    def after_batch(self):
        if not self.in_train: return
        self.lrs.append(self.optimizer.param_groups[-1]['lr'])
        self.losses.append(self.loss.detach().cpu())

    def plot_lr(self): plt.plot(self.lrs)

    def plot_loss(self): plt.plot(self.losses)


class ParamScheduler(Callback):
    _order = 1
    def __init__(self, pname, sched_func):
        self.pname, self.sched_func = pname, sched_func

    def set_param(self):
        for pg in self.optimizer.param_groups:
            pg[self.pname] = self.sched_func(self.n_epochs / self.epochs)

    def begin_batch(self):
        if self.in_train: self.set_param()


def annealer(f):
    def _inner(start, end): return partial(f, start, end)
    return _inner

@annealer
def sched_lin(start, end, pos): return start + pos*(end-start)

@annealer
def sched_cos(start, end, pos): return start + (1 + math.cos(math.pi*(1-pos))) * (end-start) / 2

@annealer
def sched_no(start, end, pos):  return start

@annealer
def sched_exp(start, end, pos): return start * (end/start) ** pos

def cos_1cycle_anneal(start, high, end):
    return [sched_cos(start, high), sched_cos(high, end)]


def combine_scheds(pcts, scheds):
    assert sum(pcts) == 1.
    pcts = tensor([0] + listify(pcts))
    assert torch.all(pcts >= 0)
    pcts = torch.cumsum(pcts, 0)
    def _inner(pos):
        idx = (pos >= pcts).nonzero().max()
        actual_pos = (pos-pcts[idx]) / (pcts[idx+1]-pcts[idx])
        return scheds[idx](actual_pos)
    return _inner

def create_standard_annealing_profile(start_lr = 0.01, upper_lr = 0.1, end_lr = 0.001, size_beginning_up_period = 0.3, size_ending_down_period = 0.7):
    return combine_scheds([size_beginning_up_period, size_ending_down_period], [sched_cos(start_lr,upper_lr), sched_cos(upper_lr, end_lr)])

