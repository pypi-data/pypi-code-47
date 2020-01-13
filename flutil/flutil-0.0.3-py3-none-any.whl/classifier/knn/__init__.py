from .. import Classifier
import numpy as np
import pandas as pd
from typing import Tuple
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


class KNNClassifier(Classifier):
    def __init__(self, train_data: pd.DataFrame, *args, **kwargs):
        """
        :param args: args passed to sklearn KNN
        :param kwargs: kwargs passed to sklearn KNN
        """
        super().__init__(train_data)
        self._model = KNeighborsClassifier(**kwargs)

        # Scale the data
        self._scaler = StandardScaler().fit(self._train_desc)
        self._model.fit(self._scaler.transform(self._train_desc),
                        self._train_label)

    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array, np.array]:
        # Decide on scaled version of the data
        predictions = self._model.predict_proba(self._scaler
                                                .transform(descriptors))
        labels = self._model.classes_
        return predictions, labels
