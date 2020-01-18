"""The Callback system"""


class CallBack:
    """Base Class for all the callbacks
    """
    def on_train_begin(self):
        pass

    def on_epoch_begin(self):
        pass

    def on_batch_begin(self):
        pass

    def on_loss_begin(self):
        pass

    def on_loss_end(self):
        pass

    def on_backward_begin(self):
        pass

    def on_backward_end(self):
        pass

    def on_step_begin(self):
        pass

    def on_step_end(self):
        pass

    def on_batch_end(self):
        pass

    def on_epoch_end(self):
        pass

    def on_train_end(self):
        pass

    def reset(self):
        pass

    def get_params(self):
        pass
