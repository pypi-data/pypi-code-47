from abc import abstractmethod, ABCMeta

import numpy as np
import pandas as pd

from marmot.ml.config import BaseModelConfig
from marmot.ml.adapter import DatasetAdapter
from marmot.ml.ensemble_model import (EnsembleKernelSVR, EnsembleLinearSVR,
                                      EnsembleRidge, EnsembleLinearReg)


class Model:

    def __init__(self, adapter=None, model_config=None):
        self.adapter = adapter
        self.model_config = model_config

    def fit(self, X, y):
        X, y = self._input_validation(X, y)

        if not self.adapter:
            print("No adapter config found: Create config")
            self.adapter = DatasetAdapter(X, y)
        if not self.model_config:
            print("No model config found: Use BaseModelConfig")
            self.model_config = BaseModelConfig()

        print(X, y)

    def predict(self, X, uncertainty=False):
        X = self._input_validation(X)
        pass

    def predict_proba(self):
        pass

    def score(self, X, y):
        X, y = self._input_validation(X, y)
        pass

    def show_config(self):
        pass

    def _input_validation(self, *args, **kwargs):
        if len(args) >= 1:
            X = args[0]
            if isinstance(X, pd.Series):
                X = pd.DataFrame(X).T
            assert isinstance(X, pd.DataFrame), 'X must be DataFrame'

            if len(args) >= 2:
                y = args[1]
                if isinstance(y, pd.Series):
                    y = pd.DataFrame(y, columns=[y.name])
                assert isinstance(y, pd.DataFrame), 'y must be DataFrame'
                return X, y
            else:
                return X
        else:
            raise Exception("Unexpected input")

    @classmethod
    def load_json(cls, adapter_config_path=None, model_config_path=None):
        adapter = DatasetAdapter.load_json(adapter_config_path)
        model_config = None
        return cls(adapter=adapter, model_config=model_config)


class AutoModel(Model, metaclass=ABCMeta):

    ensemblelayer_candidates = []

    def fit(self, X, y):
        self.config = self._optimize(X, y)
        super().fit(X, y)

    def _optimize(self, X, y):
        config = BaseModelConfig()
        model = Model(config=config)
        model.fit(X, y)

        best_config = None
        return best_config

    def _evaluate(self, X, y):
        raise NotImplementedError()


class AutoRegressionModel(AutoModel):

    ensemblelayer_candidates = [EnsembleRidge, EnsembleLinearReg,
                                EnsembleLinearSVR, EnsembleKernelSVR]



if __name__ == '__main__':
    from tests.support import get_df_boston
    from sklearn.model_selection import train_test_split
    args = {"n_models": 3,
            "col_ratio": 0.8,
            "row_ratio": 0.8,
            "n_trials": 10,
            "metric": "mse",
            "scale": True,
            "n_jobs": 2}

    X, y = get_df_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    model = Model()
    model.fit(X_train, y_train)
    print(model.predidct(X_test))
    print(model.score(X_test, y_test))
