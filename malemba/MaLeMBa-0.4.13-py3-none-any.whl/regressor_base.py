import numbers
from abc import abstractmethod, ABCMeta
from copy import deepcopy

import numpy as np


class RegressorBase(object, metaclass=ABCMeta):

    def __init__(self, params=None, **kwargs):
        self.params = params
        if self.params is None:
            self.params = dict()
        self._features = dict()
        self._feature_types = dict()
        self._labels = dict()
        self._str_features_topf = dict()
        self.topf = 0.5
        self.low_memory = kwargs.get('low_memory', False)

    @abstractmethod
    def fit(self, X, Y, **kwargs):
        self._features = dict()
        self._feature_types = dict()
        self._labels = dict()
        self._str_features_topf = dict()

    @abstractmethod
    def predict(self, X, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def _convert_str_to_factors():
        """
        Set if char type features must be converted into factors
        :return: bool
        """
        return bool()

    @abstractmethod
    def str_to_factors(self, X):
        pass

    @abstractmethod
    def validate(self, X_test, Y_test, **kwargs):
        pass

    @classmethod
    def optimize_params(cls,
                        X,
                        Y,
                        X_test,
                        Y_test,
                        var_params_grid,
                        constant_params=None):

        best_params = dict((param, var_params_grid[param].pop(0)) for param in var_params_grid)
        if constant_params is not None:
            best_params.update(constant_params)
        model_0 = cls(params=deepcopy(best_params))
        if cls._convert_str_to_factors():
            X_eval = np.array(list(model_0.str_to_factors(X=X)))
            X_test = np.array(list(model_0.str_to_factors(X=X_test)))
        else:
            X_eval = np.array(list(X))
            X_test = np.array(list(X_test))
        str_features_topf = model_0._str_features_topf
        Y_eval = np.array(list(Y))
        Y_test = np.array(list(Y_test))
        model_0.fit(X=X_eval, Y=Y_eval)
        scores = cls.number_to_iterable(model_0.validate(X_test=X_test, Y_test=Y_test))
        best_score = sum(scores)
        for param in var_params_grid:
            print("'%s' parameter optimization started" % str(param))
            curr_params = deepcopy(best_params)
            for param_v in var_params_grid[param]:
                curr_params[param] = param_v
                model = cls(params=deepcopy(curr_params))
                model._str_features_topf = str_features_topf
                model.fit(X=X_eval, Y=Y_eval)
                scores = cls.number_to_iterable(model.validate(X_test=X_test, Y_test=Y_test))
                score = sum(scores)
                if score > best_score:
                    best_score = score
                    best_params[param] = param_v
            print("'%s' parameter optimization finished - optimal value: %s" % (str(param),
                                                                                str(best_params[param])))
        return best_params, best_score

    @staticmethod
    def number_to_iterable(v):
        if isinstance(v, numbers.Number):
            return (v,)
        else:
            return v

    @abstractmethod
    def dump(self, scheme_path, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def load(cls, scheme_path, params=None, **kwargs):
        pass

    @property
    @abstractmethod
    def num_threads(self):
        return

    @abstractmethod
    def get_features(self, X):
        pass

    @property
    @abstractmethod
    def features(self):
        return list(map(lambda f: f[0], sorted(self._features.items(), key=lambda f: f[1])))

    @property
    @abstractmethod
    def feature_types(self):
        return self._feature_types

    @property
    @abstractmethod
    def labels(self):
        return list(map(lambda l: l[0], sorted(self._labels.items(), key=lambda l: l[1])))
