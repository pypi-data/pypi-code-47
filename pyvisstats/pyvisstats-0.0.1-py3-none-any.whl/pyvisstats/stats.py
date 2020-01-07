import numpy as np
import pandas as pd
from scipy import stats
import scikit_posthocs as sp
from scipy import optimize as sop

import inspect

from typing import Sequence

__all__ = ['kruskal_wallis', 'fit']


def kruskal_wallis(data, posthoc_test: str = None, names: Sequence[str]=[], **kwargs):
    """Kruskal-Wallis one-way ANOVA analysis on data.

    Args:
        data: a list of same-length 1D ndarrays or a DataFrame (#experiments x #samples)
                    i.e. for Dataframe, each row is a different experiment
        posthoc_test (str): A posthoc test to use with Kruskal-Wallis one-way ANOVA.
            One of the following: `'dunn'`, `'nemenyi'`, `'conover'`.
        names (Sequence[str])
        **kwargs: Keywords for given posthoc test.

    Returns:
        dict: Dictionary of:

            - 'f': f-value from Kruskal-Wallis test
            - 'p': p-value from Kruskal-Wallis test
            - 'results': DataFrame of significance results from posthoc test.
    """
    supported_posthoc_funcs = {'dunn': sp.posthoc_dunn,
                               'nemenyi': sp.posthoc_nemenyi,
                               'conover': sp.posthoc_conover}

    arg_names = names

    if type(data) not in [list, pd.DataFrame]:
        raise TypeError('Data must of type `list[np.ndarray]` or `pd.DataFrame`')

    if type(data) is list and type(data[0]) not in [np.ndarray, list]:
        print(type(data[0]))
        raise TypeError('Data must of type `list[np.ndarray]` or `pd.DataFrame`')

    names = None
    if type(data) is list and not arg_names:
        names = ['%d' % i for i in range(len(data))]

    # Separate panda dataframe into list of arrays, with each array corresponding to results from each experiment.
    if type(data) is pd.DataFrame:
        names = data.index.tolist()
        num_experiments = len(names)
        temp_data = []
        for i in range(num_experiments):
            temp_data.append(np.asarray(data)[i, :])
        data = temp_data

    if arg_names:
        names = arg_names

    if len(data) != len(names):
        raise ValueError('Data contains %d experiments. But only %d names provided' % (len(data),
                                                                                       len(names)))

    results = dict()
    f, p = stats.kruskal(*data)

    results['f'] = f
    results['p'] = p

    if not posthoc_test:
        return results

    # determine kwargs for posthoc_funcs
    posthoc_func = supported_posthoc_funcs[posthoc_test]
    posthoc_test_defaults = {}
    posthoc_func_args = inspect.getfullargspec(posthoc_func).args
    for k in posthoc_func_args:
        if k in kwargs:
            posthoc_test_defaults[k] = kwargs.get(k)

    ph_results = posthoc_func(data, **posthoc_test_defaults)
    if isinstance(ph_results, pd.DataFrame):
        ph_results = np.asarray(ph_results)
    df = pd.DataFrame(ph_results, columns=names, index=names)

    results[posthoc_test] = df

    return results


def __print_results__(data, **kwargs):
    alpha = kwargs.get('alpha') if 'alpha' in kwargs else 0.05

    print('===================')
    print('F-value: %0.4f' % data['f'])
    print('p-value: %0.4f' % data['p'])

    def highlight_significant(val):
        """
        Takes a scalar and returns a string with
        the css property `'color: red'` for negative
        strings, black otherwise.
        """
        bg_color = 'yellow' if abs(val) < alpha else ''
        return 'background-color: %s' % bg_color

    if data['dunn'] is not None:
        print('Dunn: ')
        s = data['dunn'].style.applymap(highlight_significant)
        display(s)


def fit(x, y, func, p0, **kwargs):
    maxfev = kwargs.get('maxfev') if 'maxfev' in kwargs else 3000

    popt, _ = sop.curve_fit(func, x, y, p0=p0, maxfev=maxfev)

    residuals = y - func(x, *popt)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    print(ss_res)
    print(ss_tot)

    r_squared = 1 - (ss_res / (ss_tot + 1e-8))

    return popt, r_squared
