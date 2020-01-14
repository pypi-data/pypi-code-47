from enum import IntEnum

__all__ = ['GraphType','Mode','InferenceType','SamplerType','StatisticsType', 'Optimizer']

class StatisticsType(IntEnum):
	overcomplete = 0
	minimal = 1

class GraphType(IntEnum):
	custom = 0
	grid = 2
	full = 5
	chain = 1
	auto_tree = 6
	auto = 7
	other = 8

class InferenceType(IntEnum):
	belief_propagation = 0
	junction_tree = 1
	stochastic_quadrature = 2

class SamplerType(IntEnum):
	gibbs = 0
	apx_perturb_and_map = 1

class Optimizer(IntEnum):
	gradient_descent = 4
	proximal_gradient = 5
	accelerated_proximal_gradient = 6

class Mode(IntEnum):
	mrf = 0
	strf_linear = 1
	strf_quadratic = 2
	strf_cubic = 3
	strf_rational = 4
	strf_exponential = 5
	strf_inv_quadratic = 6
	strf_inv_cubic = 7
	strf_inv_rational = 8
	strf_inv_exponential = 9
	integer = 10
	dbt = 11
	ising = 12

#class Model:
#	def __init__(self, _ptr):
#		self.ptr = _ptr
