"""Optimizer for Blueqat VQE"""
import random
import warnings
from itertools import product
import numpy as np
from scipy.optimize import minimize as _scipy_minimizer

def get_scipy_minimizer(**kwargs):
    """Get minimizer which uses `scipy.optimize.minimize`"""
    def minimizer(objective, n_params):
        params = [random.random() for _ in range(n_params)]
        result = _scipy_minimizer(objective, params, **kwargs)
        return result.x
    return minimizer

class GridSearchOptimizer:
    def __init__(self, param_ranges, endpoint=True, n_jobs=1):
        """
        Args:
            param_ranges[(start, stop, num)|(stop, num)|num]: Parameter ranges.
            endpoint: If True, include `stop` value.
            n_jobs: (Unimplemented.) Number of jobs for parallel calculation.
        """
        self.param_ranges = [self.__parse_param_range(r) for r in param_ranges]
        self.endpoint = endpoint
        self.n_jobs = n_jobs
        if n_jobs > 1:
            warnings.warn("n_jobs is unimplemented.")

    DEFAULT_START = 0.0
    DEFAULT_STOP = 1.0
    def __parse_param_range(self, param_range):
        try:
            n = len(param_range)
        except TypeError:
            return np.linspace(self.DEFAULT_START, self.DEFAULT_STOP, param_range, self.endpoint)
        if n == 3:
            return np.linspace(*param_range, self.endpoint)
        if n == 2:
            return np.linspace(self.DEFAULT_START, *param_range, self.endpoint)
        if n == 1:
            return np.linspace(self.DEFAULT_START, self.DEFAULT_STOP, *param_range, self.endpoint)
        raise ValueError(f"Invalid param_range: {param_range}")

    def get_minimizer(self):
        def minimizer(objective, n_params):
            pass
        return minimizer
