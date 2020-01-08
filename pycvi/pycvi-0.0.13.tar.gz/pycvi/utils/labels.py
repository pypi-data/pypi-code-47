import numpy as np


class Labels:
    """
        # TODO: add docstring
    """

    def __init__(self, y):
        """

        Args:
            y: iterable

        """

        self.labels = np.array(y)

        # if one-hot, transform to labels
        if self.labels.ndim > 1:
            self.labels = self.labels.argmax(axis=1)

        # test that there are at least two classes
        assert len(set(self.labels.ravel())) >= 2,\
            "Labels should have at least two distinct observations, got {}".format(set(self.labels.ravel()))
