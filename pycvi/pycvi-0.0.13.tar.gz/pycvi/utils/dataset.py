from .labels import Labels
from .features import Features


class DataSet(Features, Labels):
    def __init__(self, X, y=None):
        if y is not None:
            Labels.__init__(self, y)
        else:
            self.labels = None
        Features.__init__(self, X)

        assert self.labels.shape[0] == self.X.shape[0],\
            "Expected features and targets to have the same number of elements, got {} and {}".format(
                self.X.shape[0], self.labels.shape[0]
            )
