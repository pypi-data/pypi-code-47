from .. import Classifier
from typing import Tuple
from scipy.spatial.distance import cdist
import numpy as np
import pandas as pd


class EuclideanClassifier(Classifier):
    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array, np.array]:
        distmat = cdist(descriptors, self._train_desc)

        # Keep the smallest distance per label
        u, indices = np.unique(self._train_label, return_inverse=True)
        filt_distmat = np.array([
            [np.min(row[indices == idx]) for idx in range(len(u))]
            for row in distmat
        ])
        return -filt_distmat, u


class EuclideanAvgClassifier(EuclideanClassifier):
    def __init__(self, train_data: pd.DataFrame):
        if any(train_data.descriptor.isna()):
            raise ValueError('Training data should not contain NaN '
                             'descriptors')
        train_data = (train_data.groupby('label')
                      .apply(lambda x: x['descriptor'].mean())
                      .reset_index()
                      .rename(columns={0: 'descriptor'}))

        super().__init__(train_data)
