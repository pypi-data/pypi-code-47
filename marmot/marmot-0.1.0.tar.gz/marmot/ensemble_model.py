import copy
import pickle
from abc import ABCMeta, abstractmethod
import random

import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from scipy.stats import pearsonr
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
from marmot.base_model import (DartRegCV, GBTRegCV, KernelSVRCV, LassoCV,
                                    LinearSVRCV, RidgeCV, ElasticNetCV)


class BaseEnsembleModel(metaclass=ABCMeta):

    base_model_cls = []

    def __init__(self,
                 n_models=30, col_ratio=0.7, row_ratio=0.7,
                 n_trials=100, metric='mse',
                 scale=True, n_jobs=1):
        self.n_models = n_models
        self.col_size = col_ratio
        self.row_size = row_ratio

        self.n_trials = n_trials
        self.metric = metric

        self.scale = scale
        self.n_jobs = n_jobs

    def fit(self, X, y):
        X, y = self._input_validation(X, y)

        self.models = {}
        self.scalers = {}
        self.masks = {}
        self._rprs_modeling(X, y)

    def predict(self, X, uncertainty=False):
        X = self._input_validation(X)

        df_result = pd.DataFrame()
        for i in range(self.n_models):
            model = self.models[i]
            mask = self.masks[i]
            scaler = self.scalers[i]

            X_ = X.loc[:, mask]
            if scaler:
                X_ = pd.DataFrame(scaler.transform(X_), columns=X_.columns)
            y_pred = model.predict(X_)
            df_result[i] = list(y_pred)

        pred_mean = df_result.mean(1).values
        pred_std = df_result.std(1).values

        if uncertainty:
            return np.vstack([pred_mean, pred_std])
        else:
            return pred_mean

    def predict_proba(self, X):
        return self.predict(X, uncertainty=True)

    def score(self, X, y):
        X, y = self._input_validation(X, y)

        y_true = y.values.flatten()
        y_pred = self.predict(X).flatten()

        return r2_score(y_true, y_pred)

    def valid(self, X, y, test_size=0.3):
        X, y = self._input_validation(X, y)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size)
        self.fit(X_train, y_train)

        print("Tran R2 score", self.score(X_train, y_train))
        print("Test R2 score", self.score(X_test, y_test))

    def _rprs_modeling(self, X, y):
        results = Parallel(n_jobs=self.n_jobs)(
            [delayed(self._train)(X, y, i) for i in range(self.n_models)])

        for i, (mask, model, scaler) in enumerate(results):
            self.masks[i] = mask
            self.models[i] = model
            self.scalers[i] = scaler

    def _train(self, X, y, i):
        while True:
            sample_mask = [bool(np.random.binomial(1, self.row_size))
                           for i in range(X.shape[0])]
            mask = [bool(np.random.binomial(1, self.col_size))
                    for i in range(X.shape[1])]
            if np.any(sample_mask) and np.any(mask):
                break

        X_rprs = copy.deepcopy(X.loc[sample_mask, mask])
        if self.scale:
            scaler = StandardScaler()
            scaler.fit(X_rprs)
            X_rprs = pd.DataFrame(scaler.transform(X_rprs),
                                  index=X_rprs.index, columns=X_rprs.columns)
        else:
            scaler = None

        y_rp = copy.deepcopy(y[sample_mask])

        model = self._get_model()
        model.fit(X_rprs, y_rp)

        mask = copy.deepcopy(mask)
        model = copy.deepcopy(model)
        scaler = copy.deepcopy(scaler)

        return mask, model, scaler

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

    def _get_model(self):
        model_cls = random.choice(self.base_model_cls)
        return model_cls(n_trials=self.n_trials, metric=self.metric)


class EnsembleRidge(BaseEnsembleModel):

    base_model_cls = [RidgeCV]


class EnsembleLinearSVR(BaseEnsembleModel):

    base_model_cls = [LinearSVRCV]


class EnsembleKernelSVR(BaseEnsembleModel):

    base_model_cls = [KernelSVRCV]


class EnsembleDartReg(BaseEnsembleModel):

    base_model_cls = [DartRegCV]


class EnsembleGBTReg(BaseEnsembleModel):

    base_model_cls = [GBTRegCV]


class EnsembleLinearReg(BaseEnsembleModel):

    base_model_cls = [RidgeCV, LassoCV, LinearSVRCV, ElasticNetCV]


if __name__ == '__main__':
    from tests.support import get_df_boston
    args = {"n_models": 3,
            "col_ratio": 0.8,
            "row_ratio": 0.8,
            "n_trials": 10,
            "metric": "mse",
            "scale": True,
            "n_jobs": 2}

    X, y = get_df_boston()
    model = EnsembleLinearReg(**args)
    model.fit(X, y)
    print(model.predict(X).shape)
    print(model.predict_proba(X).shape)
    score = model.score(X, y)
    print(score)
    #model.valid(X, y)
