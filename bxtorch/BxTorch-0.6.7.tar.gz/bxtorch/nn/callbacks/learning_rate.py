#
#  nn/callbacks/learning_rate.py
#  bxtorch
#
#  Created by Oliver Borchert on January 08, 2020.
#  Copyright (c) 2020 Oliver Borchert. All rights reserved.
#  

class LearningRateScheduler(TrainingCallback):
    """
    The learning rate scheduler may be used with a PyTorch learning rate scheduler. The callback is
    automatically triggered after the end of every iteration or epoch.
    """

    def __init__(self, scheduler, after_batch=False):
        """
        Initializes a new learning rate scheduler for the given PyTorch scheduler.

        Parameters:
        -----------
        - scheduler: torch.optim.lr_scheduler
            The PyTorch scheduler.
        - after_batch: bool, default: False
            Whether to call the scheduler after every batch or after every epoch.
        """
        self.after_batch = after_batch
        self.scheduler = scheduler

    def after_batch(self, train_loss):
        if self.after_batch:
            self.scheduler.step()

    def after_epoch(self, metrics):
        if not self.after_batch:
            self.scheduler.step()
