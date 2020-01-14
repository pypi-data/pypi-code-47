import torch
import math

def get_scheduler(config, optimizer):
    if config.scheduler_name == "sgdr":
        scheduler = SGDR(
            optimizer,
            iterations_per_epoch= config.iterations_per_epoch,
            t_actual= config.t_actual,
            t_mul= config.t_mul,
            lr_max= config.lr_max,
            lr_min= config.lr_min,
            decay= config.decay
        )
    else:
        raise NotImplementedError("This scheduler is not implemented")
    return scheduler

class SGDR(torch.optim.lr_scheduler._LRScheduler):
    def __init__(
        self,
        optimizer,
        iterations_per_epoch, 
        t_actual,
        t_mul, 
        lr_max, 
        lr_min,
        decay,
        last_epoch=-1):
        self.iterations_per_epoch = iterations_per_epoch
        self.t_actual = t_actual
        self.t_mul = t_mul
        self.lr_max = lr_max
        self.lr_min = lr_min
        self.decay = decay
        self.last_epoch = last_epoch
        super(SGDR, self).__init__(optimizer, last_epoch)

    def get_lr(self):
        iteration = float(self.last_epoch)
        restart_period = self.iterations_per_epoch * self.t_actual
        lr_max = float(self.lr_max)
        while iteration/restart_period > 1.:
            iteration = iteration - restart_period
            restart_period = restart_period * self.t_mul
            lr_max = lr_max/self.decay

        cosine_value = math.cos(math.pi*(iteration/restart_period))
        new_lr = self.lr_min + (0.5 * (self.lr_max - self.lr_min) * (1+cosine_value))
        return [new_lr for base_lr in self.base_lrs]