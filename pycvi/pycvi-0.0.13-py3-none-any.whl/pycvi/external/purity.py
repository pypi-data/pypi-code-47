import numpy as np

from sklearn import metrics
from ..utils.labels import Labels


class Purity:
    """"""

    def __init__(self, y_true, y_pred):
        self.y_true, self.y_pred = Labels(y_true), Labels(y_pred)
        self.purity = None
        self.fit()

    def fit(self):
        """
        compute the purity score of a clustering

        Returns: float
                purity score.

        """

        # if no value was past to clusters, use the last clustering

        # compute contingency matrix (also called confusion matrix)
        contingency_matrix = metrics.cluster.contingency_matrix(self.y_true.labels, self.y_pred.labels)

        self.purity = np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)
