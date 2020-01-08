"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import bisect

def Mean(t):
	"""Computes the mean of a sequence of numbers.

	Args:
		t: sequence of numbers

	Returns:
		float
	"""
	return float(sum(t)) / len(t)

def MeanVar(t):
	"""Computes the mean and variance of a sequence of numbers.

	Args:
		t: sequence of numbers

	Returns:
		tuple of two floats
	"""
	mu = Mean(t)
	var = Var(t, mu)
	return mu, var

def Trim(t, p=0.01):
	"""Trims the largest and smallest elements of t.

	Args:
		t: sequence of numbers
		p: fraction of values to trim off each end

	Returns:
		sequence of values
	"""
	t.sort()
	n = int(p * len(t))
	t = t[n:-n]
	return t

	
def TrimmedMean(t, p=0.01):
	"""Computes the trimmed mean of a sequence of numbers.

	Side effect: sorts the list.

	Args:
		t: sequence of numbers
		p: fraction of values to trim off each end

	Returns:
		float
	"""
	t = Trim(t, p)
	return Mean(t)


def TrimmedMeanVar(t, p=0.01):
	"""Computes the trimmed mean and variance of a sequence of numbers.

	Side effect: sorts the list.

	Args:
		t: sequence of numbers
		p: fraction of values to trim off each end

	Returns:
		float
	"""
	t = Trim(t, p)
	mu, var = MeanVar(t)
	return mu, var


def Var(t, mu=None):
	"""Computes the variance of a sequence of numbers.

	Args:
		t: sequence of numbers
		mu: value around which to compute the variance; by default,
			computes the mean.

	Returns:
		float
	"""
	if mu is None:
		mu = Mean(t)

	# compute the squared deviations and return their mean.
	dev2 = [(x - mu)**2 for x in t]
	var = Mean(dev2)
	return var


def Binom(n, k, d={}):
	"""Compute the binomial coefficient "n choose k".

	Args:
	  n: number of trials
	  k: number of successes
	  d: map from (n,k) tuples to cached results

	Returns:
	  int
	"""
	if k == 0:
		return 1
	if n == 0:
		return 0

	try:
		return d[n, k]
	except KeyError:
		res = Binom(n-1, k) + Binom(n-1, k-1)
		d[n, k] = res
		return res


class Interpolator(object):
    """Represents a mapping between sorted sequences; performs linear interp.

    Attributes:
        xs: sorted list
        ys: sorted list
    """
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    def Lookup(self, x):
        """Looks up x and returns the corresponding value of y."""
        return self._Bisect(x, self.xs, self.ys)

    def Reverse(self, y):
        """Looks up y and returns the corresponding value of x."""
        return self._Bisect(y, self.ys, self.xs)

    def _Bisect(self, x, xs, ys):
        """Helper function."""
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        i = bisect.bisect(xs, x)
        frac = 1.0 * (x - xs[i-1]) / (xs[i] - xs[i-1])
        y = ys[i-1] + frac * 1.0 * (ys[i] - ys[i-1])
        return y


"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import random

def Cov(xs, ys, mux=None, muy=None):
    """Computes Cov(X, Y).

    Args:
        xs: sequence of values
        ys: sequence of values
        mux: optional float mean of xs
        muy: optional float mean of ys

    Returns:
        Cov(X, Y)
    """
    if mux is None:
        mux = Mean(xs)
    if muy is None:
        muy = Mean(ys)

    total = 0.0
    for x, y in zip(xs, ys):
        total += (x-mux) * (y-muy)

    return total / len(xs)


def Corr(xs, ys):
    """Computes Corr(X, Y).

    Args:
        xs: sequence of values
        ys: sequence of values

    Returns:
        Corr(X, Y)
    """
    xbar, varx = MeanVar(xs)
    ybar, vary = MeanVar(ys)

    corr = Cov(xs, ys, xbar, ybar) / math.sqrt(varx * vary)

    return corr


def SerialCorr(xs):
    """Computes the serial correlation of a sequence."""
    return Corr(xs[:-1], xs[1:])


def SpearmanCorr(xs, ys):
    """Computes Spearman's rank correlation.

    Args:
        xs: sequence of values
        ys: sequence of values

    Returns:
        float Spearman's correlation
    """
    xranks = MapToRanks(xs)
    yranks = MapToRanks(ys)
    return Corr(xranks, yranks)


def LeastSquares(xs, ys):
    """Computes a linear least squares fit for ys as a function of xs.

    Args:
        xs: sequence of values
        ys: sequence of values

    Returns:
        tuple of (intercept, slope)
    """
    xbar, varx = MeanVar(xs)
    ybar, vary = MeanVar(ys)

    slope = Cov(xs, ys, xbar, ybar) / varx
    inter = ybar - slope * xbar

    return inter, slope


def FitLine(xs, inter, slope):
    """Returns the fitted line for the range of xs.

    xs: x values used for the fit
    slope: estimated slope
    inter: estimated intercept
    """
    fxs = min(xs), max(xs)
    fys = [x * slope + inter for x in fxs]
    return fxs, fys


def Residuals(xs, ys, inter, slope):
    """Computes residuals for a linear fit with parameters inter and slope.

    Args:
        xs: independent variable
        ys: dependent variable
        inter: float intercept
        slope: float slope

    Returns:
        list of residuals
    """
    res = [y - inter - slope*x for x, y in zip(xs, ys)]
    return res


def CoefDetermination(ys, res):
    """Computes the coefficient of determination (R^2) for given residuals.

    Args:
        ys: dependent variable
        res: residuals
        
    Returns:
        float coefficient of determination
    """
    ybar, vary = MeanVar(ys)
    resbar, varres = MeanVar(res)
    return 1 - varres / vary


def MapToRanks(t):
    """Returns a list of ranks corresponding to the elements in t.

    Args:
        t: sequence of numbers
    
    Returns:
        list of integer ranks, starting at 1
    """
    # pair up each value with its index
    pairs = enumerate(t)
    
    # sort by value
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1])

    # pair up each pair with its rank
    ranked = enumerate(sorted_pairs)

    # sort by index
    resorted = sorted(ranked, key=lambda trip: trip[1][0])

    # extract the ranks
    ranks = [trip[0]+1 for trip in resorted]
    return ranks


def CorrelatedGenerator(rho):
    """Generates standard normal variates with correlation.

    rho: target coefficient of correlation

    Returns: iterable
    """
    x = random.gauss(0, 1)
    yield x

    sigma = math.sqrt(1 - rho**2);    
    while True:
        x = random.gauss(x * rho, sigma)
        yield x


def CorrelatedNormalGenerator(mu, sigma, rho):
    """Generates normal variates with correlation.

    mu: mean of variate
    sigma: standard deviation of variate
    rho: target coefficient of correlation

    Returns: iterable
    """
    for x in CorrelatedGenerator(rho):
        yield x * sigma + mu


def main():
    pass
    

if __name__ == '__main__':
    main()
