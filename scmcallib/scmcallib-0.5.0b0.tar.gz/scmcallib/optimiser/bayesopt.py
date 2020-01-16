import os.path
from logging import getLogger

import numpy as np
from bayes_opt import BayesianOptimization, JSONLogger
from bayes_opt.event import Events

from .base import BaseOptimiser

logger = getLogger(__name__)


class OptimiserBayesOpt(BaseOptimiser):
    """
    A backend which uses Bayesian Optimisation for finding a set of best-fit parameters.

    This optimiser uses the Bayesian Optimization library `https://github.com/fmfn/BayesianOptimization`
    """
    name = "bayesopt"

    def get_param_bounds(self, parameter_set, include_bounds):
        # TODO: put in utils?
        param_bounds = {}
        for name, p in parameter_set.tune_parameters.items():
            if not include_bounds:
                param_bounds[name] = (-np.inf, np.inf)
                continue

            samples = p.distribution.random(size=10000)
            best_guess = samples.mean()
            param_bounds[name] = (
                p.kwargs.get("lower", best_guess + (best_guess - samples.min()) * 1.05),
                p.kwargs.get("upper", best_guess - (best_guess - samples.max()) * 1.05),
            )

        return param_bounds

    def find_best_fit(
        self, evaluator, parameter_set, include_bounds=True, verbose=0, **kwargs
    ):
        """
        Find parameters for a best fit

        The environment variable "SCMCALLIB_LOGS" is used to determine where the log file containing the steps the bayesian optimiser
        performed is stored.

        Parameters
        ----------
        evaluator
        parameter_set: :obj:`scmcallib.parameterset.ParameterSet`
        include_bounds: bool
            If True, set the parameter maximum and minimum limits, otherwise values are free to go from -inf to inf.
        verbose: bool
        kwargs:
            Additional arguments passed to the baysian optimiser.
            Options include ['init_points', 'init_method', 'n_iter', 'acq', 'xi']

        """
        num_random_samples = kwargs.pop("init_points", 100)
        random_method = kwargs.pop("init_method", "random")
        kwargs.setdefault("n_iter", 10)
        kwargs.setdefault("acq", "ei")
        kwargs.setdefault("xi", 0.02)

        param_bounds = self.get_param_bounds(parameter_set, include_bounds)

        bo = BayesianOptimization(f=evaluator, pbounds=param_bounds, verbose=verbose)

        logs_path = os.path.join(os.environ.get("SCMCALLIB_LOGS", "."), "bayesopt_logs.json")
        bo.logs_path = logs_path
        bo.subscribe(Events.OPTMIZATION_STEP, JSONLogger(path=logs_path))

        # Queue up the random samples (probes)
        logger.info("Starting {} {} samples".format(num_random_samples, random_method))
        samples = evaluator.parameter_set.evaluate(num_random_samples, method=random_method)
        for _, s in samples.iterrows():
            bo.probe(
                s.to_dict(), lazy=False
            )
        logger.info("Finished initial random sampling")
        logger.info("Best result: {}".format(bo.max))
        logger.info("Beginning iterations with settings {}".format(kwargs))
        bo.maximize(init_points=0, **kwargs)

        return self.process_minimisation_results(bo)

    def process_minimisation_results(self, bo):
        # TODO: optionally return the maximal values of the gaussian processes instead of the best sampled point.
        bo.x = bo.max["params"]
        # BayesOpt doesn't converge in the same sense I don't think, need to check
        # with Nick
        bo.success = True

        return bo
