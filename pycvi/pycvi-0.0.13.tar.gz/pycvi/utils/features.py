from . import parse


class Features:
    def __init__(self, X):
        """
        Args:
            X: iterable
                Array containing the features
        """

        self.X = parse.preprocess(X)
