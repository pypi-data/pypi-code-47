from .. import Classifier
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier as DTC
from typing import Tuple


class DecisionTreeClassifier(Classifier):
    def __init__(self, train_data: pd.DataFrame):
        super().__init__(train_data)
        self._model = DTC()
        self._model.fit(self._train_desc, self._train_label)

    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array, np.array]:
        predictions = self._model.predict_proba(descriptors)
        labels = self._model.classes_
        return predictions, labels
