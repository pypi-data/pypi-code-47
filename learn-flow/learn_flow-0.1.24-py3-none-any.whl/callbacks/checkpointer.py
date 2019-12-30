# -*- coding: utf-8 -*-
"""
module checkpointer.py
--------------------------------
Saves the current tensorflow graph state during learning procedure.
"""
import numpy as np
import tensorflow as tf
import os
import tarfile
import json
from . import ModeEnum
from . import on_batch_begin, on_batch_end, on_epoch_begin, on_epoch_end, on_train_begin, \
    on_train_end, on_validate_begin, on_validate_end


class CheckPointer(object):
    """Save the model after every epoch.

    `filepath` can contain named formatting options,
     which will be filled the value of `epoch` and
     keys in `logs` (passed in `on_epoch_end`).

    For example: if `filepath` is `weights.{epoch:02d}-{val_loss:.2f}.hdf5`,
    then the model checkpoints will be saved with the epoch number and
    the validation loss in the filename.
    """

    def __init__(
            self,
            path,
            monitor='val_loss',
            verbose=0,
            save_best_only=False,
            mode: ModeEnum=ModeEnum.MIN,
            period=1,
            max_to_keep=5,
            restore_sequentially=False,
            save_source_code=True
    ):
        """
        CheckPointer callback initialization.

        :param path: string, path to save the model file.
        :param monitor: quantity to monitor.
        :param verbose: verbosity mode, 0 or 1.
        :param save_best_only: if `save_best_only=True`,
            the latest best model according to
            the quantity monitored will not be overwritten.
        :param mode: one of {auto, min, max}.
            If `save_best_only=True`, the decision
            to overwrite the current save file is made
            based on either the maximization or the
            minimization of the monitored quantity. For `val_acc`,
            this should be `max`, for `val_loss` this should
            be `min`, etc. In `auto` mode, the direction is
            automatically inferred from the name of the monitored quantity.
        :param period: Interval (number of epochs) between checkpoints.
        :param max_to_keep: Maximum number of recent checkpoints to keep. **Defaults** to 5.
        :param restore_sequentially: A Bool, which if true, causes restore of different variables
                                    to happen sequentially within each device.
                                    This can lower memory usage when restoring very large models.
        """

        self.monitor = monitor
        self.verbose = verbose
        self.path = path
        self.save_best_only = save_best_only
        self.period = period
        self.epochs_since_last_save = 0
        self.mode = mode
        self.max_to_keep = max_to_keep
        self.restore_sequentially = restore_sequentially
        if mode is ModeEnum.MIN:
            self.monitor_op = np.less
            self.best = np.Inf
        elif mode is ModeEnum.MAX:
            self.monitor_op = np.greater
            self.best = -np.Inf
        # saver is initialized on_train_begin event
        self.saver = None
        on_epoch_end.connect(self.on_epoch_end, weak=False)

        if save_source_code:
            on_train_begin.connect(self.on_train_begin, weak=False)

    def on_epoch_end(self, sender):
        epoch = sender.current_state["current_epoch"]
        self.epochs_since_last_save += 1
        self._do_checkpoint(epoch, sender)

    def _do_checkpoint(self, epoch, sender):
        if self.epochs_since_last_save >= self.period:
            self.epochs_since_last_save = 0
            filepath = os.path.join(self.path, "model.ckpt")
            current = sender.current_state.get(self.monitor, None)

            if current is None:
                if self.verbose > 0:
                    print('Can save best model only with {} available, '
                                'skipping.'.format(self.monitor))
            else:
                if self.monitor_op(current, self.best):
                    if self.verbose > 0:
                        print(
                            '\nEpoch %05d: %s improved from %0.5f to %0.5f,'
                            ' saving model to %s' % (
                                epoch + 1, self.monitor, self.best,
                                current, filepath
                            )
                        )
                    self.best = current

                    if self.save_best_only:
                        save_path = self.saver.save(tf.get_default_session(), filepath)
                    else:
                        save_path = self.saver.save(
                            sess=tf.get_default_session(),
                            save_path=filepath,
                            global_step=tf.train.get_or_create_global_step()
                        )
                else:
                    if self.verbose > 0:
                        print(
                            '\nEpoch %05d: %s did not improve from %0.5f' %(
                                epoch + 1, self.monitor, self.best
                            )
                        )

    def on_train_begin(self, sender):
        """ On train begin method.
        Compress and saves the whole experiment code withing the model weights.
        :param sender: the learner object.
        """
        # erases the current history.
        self.epochs_since_last_save = 0
        # init tf saver
        self.saver = tf.train.Saver(max_to_keep=self.max_to_keep, restore_sequentially=self.restore_sequentially)

        if self.mode is ModeEnum.MIN:
            self.best = np.Inf
        elif self.mode is ModeEnum.MAX:
            self.best = -np.Inf

        path = os.path.join(self.path, "source_code.tar.gz")
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            assert os.path.exists(self.path)

        with tarfile.open(path, mode="w:gz") as f:
            cwd = os.getcwd()
            # recursively walk through current working path
            for root, _, files in os.walk(cwd):
                if root == cwd:
                    folder = ""
                else:
                    folder = root.replace(cwd+"/", "")

                for file_name in files:
                    # we do not want to add pyc and __pycache__ files to the archive
                    if not file_name.endswith(".pyc"):
                        f.add(os.path.join(root, file_name), os.path.join(folder, file_name))
