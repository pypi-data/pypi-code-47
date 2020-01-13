from .. import Classifier
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from typing import Tuple
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


class SVMClassifier(Classifier):
    def __init__(self, train_data: pd.DataFrame, scale=False,
                 **kwargs):
        """
        :param args: args passed to sklearn SVC
        :param kwargs: kwargs passed to sklearn SVC
        """
        super().__init__(train_data)
        self._model = SVC(**kwargs)

        # Scale the data
        if scale:
            self._scaler = StandardScaler().fit(self._train_desc)
            self._model.fit(self._scaler.transform(self._train_desc),
                            self._train_label)
        else:
            self._scaler = None
            self._model.fit(self._train_desc, self._train_label)

    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array, np.array]:
        # Decide on scaled version of the data
        if self._scaler is not None:
            predictions = (self._model
                           .decision_function(self._scaler
                                              .transform(descriptors)))
        else:
            predictions = self._model.decision_function(descriptors)
        labels = self._model.classes_
        return predictions, labels

    @staticmethod
    def grid_search(train_data: pd.DataFrame, param_grid: dict,
                    **kwargs):
        """Return a DataFrame with the grid search results.

        :param pd.DataFrame train_data: `pd.DataFrame` with columns
        'descriptor' and 'label'. The 'descriptor' column contains \$m_A\$
        arrays of dimension \$n\$; the 'label' column contains the respective
        labels.
        :param dict param_grid: the parameter values for the grid.
        :param kwargs: kwargs passed to `sklearn.model_selection.GridSearchCV`
        """
        X = np.vstack(train_data['descriptor'].values)
        y = train_data['label'].values
        clf = GridSearchCV(SVC(), param_grid, return_train_score=False,
                           **kwargs)
        clf.fit(X, y)
        return pd.DataFrame(clf.cv_results_)


class SVMNormalized(SVMClassifier):
    """SVM classifier that divides the prediction scores with the number of
    unique labels.
    """
    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array, np.array]:
        preds, labs = super()._get_score_mat(descriptors)
        return preds / len(labs), labs
