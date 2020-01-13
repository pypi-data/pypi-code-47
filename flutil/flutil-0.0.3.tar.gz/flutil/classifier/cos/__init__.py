"""Classifier using cosine similarity."""
from typing import Tuple
from scipy.spatial.distance import cdist
import numpy as np
from .. import Classifier


class CosClassifier(Classifier):
    """Classifier using cosine similarity."""
    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array, np.array]:
        distmat = 1 - cdist(descriptors, self._train_desc,
                            metric='cosine')
        return distmat, self._train_label
