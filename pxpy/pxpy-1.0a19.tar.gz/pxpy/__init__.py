__all__ = ['GraphType', 'Mode', 'InferenceType', 'SamplerType', 'StatisticsType', 'Optimizer']

import ctypes
import time
import numpy
import itertools
import struct
import sys, os
from sys import platform
from .functions import *

__DEBUG = False
if os.environ.get('PX_DEBUG') is not None:
	__DEBUG = True

class Colors:
	INIT  = '\033[11m'
	TRAIN = '\033[10m'
	OTHER = '\033[94m'
	ENDC  = '\033[0m'
	BOLD  = '\033[1m'
	UNDERLINE = '\033[4m'

from pathlib import Path
path = Path(__file__)

if platform == "linux" or platform == "linux2":
	if not __DEBUG:
		pxpath = str(path.parent / "lib/libpx.so")
	else:
		pxpath = str(path.parent / "lib/libpx_dbg.so")
elif platform == "darwin":
#	pxpath = path.parent / "lib/libpx.dylib"
	raise TypeError('macOS will be supported soon!')
elif platform == "win32":
	pxpath = str(path.parent / "lib/libpx.dll")

example_model_filename = str(path.parent / "data/5_14.mod")
example_data_filename  = str(path.parent / "data/sin44")

class disc_t(ctypes.Structure):
	_fields_ = [("num_intervals", ctypes.c_uint64), ("num_moments", ctypes.c_uint64), ("_intervals", ctypes.POINTER(ctypes.c_double)), ("_moments", ctypes.POINTER(ctypes.c_double))]

	@property
	def intervals(self):
		return numpy.ctypeslib.as_array(self._intervals, shape = (self.num_intervals, 2))

	@property
	def moments(self):
		return numpy.ctypeslib.as_array(self._moments, shape = (self.num_moments, 4))

lib = ctypes.cdll.LoadLibrary(pxpath)

lib.create_ctx.restype = ctypes.c_uint64

lib.version.restype = ctypes.c_uint64

lib.ctx_set_code.restype = ctypes.c_bool

lib.discretize.restype = disc_t
lib.discretize.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64]

lib.discretize_precomputed.restype = None
lib.discretize_precomputed.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, disc_t]

lib.reset_ctx.restype  = ctypes.c_bool
lib.reset_ctx.argtypes = [ctypes.c_uint64]

lib.run_ctx.restype  = ctypes.c_bool
lib.run_ctx.argtypes = [ctypes.c_uint64]

lib.destroy_ctx.restype  = None
lib.destroy_ctx.argtypes = [ctypes.c_uint64]

lib.ctx_write_reg.restype  = ctypes.c_bool
lib.ctx_write_reg.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint64]

lib.ctx_read_reg.restype  = ctypes.c_uint64
lib.ctx_read_reg.argtypes = [ctypes.c_uint64, ctypes.c_char_p]

MISSING_VALUE = 65535

def array_check(a, name, dtype=None):
	if not isinstance(a, numpy.ndarray):
		raise TypeError(name,'must be of type numpy.ndarray')
	if isinstance(a, numpy.ndarray) and not a.flags['C_CONTIGUOUS']:
		raise TypeError(name,'must be a C-style contiguous numpy array')
	if dtype is not None:
		if isinstance(a, numpy.ndarray) and not a.dtype==dtype:
			raise TypeError('type of',a,'must be',str(dtype))

class Graph(ctypes.Structure):
	_fields_ = [("__unused", ctypes.c_uint64), ("__itype", ctypes.c_uint8), ("_nodes", ctypes.c_uint64), ("_edges", ctypes.c_uint64), ("A", ctypes.POINTER(ctypes.c_uint64))]

	__edgelistref = None

	destroyed = False

	@property
	def nodes(self):
		if self.destroyed:
			return 0
		return self._nodes

	@property
	def edges(self):
		if self.destroyed:
			return 0
		return self._edges

	def __len__(self):
		if self.destroyed:
			return 0
		return self.nodes

	def delete(self):
		if not self.destroyed:
			self.destroyed = True
			L = ["GPT "+str(ctypes.addressof(self))+";", "DEL GPT;"]
			recode(L)
			run()

	@property
	def edgelist(self):
		if self.destroyed:
			return numpy.array([])
		res = numpy.ctypeslib.as_array(self.A, shape = (self.edges, 2))
		res.flags.writeable = False
		return res

class STGraph(ctypes.Structure):
	_fields_ = [("__unused", ctypes.c_uint64), ("__itype", ctypes.c_uint8), ("T", ctypes.c_uint64), ("base0", ctypes.c_uint64), ("Tm1inv", ctypes.c_float)]

	__LOCAL_G = None

	@property
	def base(self):
		if self.__LOCAL_G is None:
			#print("CONSTRUCTING LOCAL_G IN STGraph.base()")
			self.__LOCAL_G = ctypes.cast(self.base0, ctypes.POINTER(Graph))
		return self.__LOCAL_G.contents

	destroyed = False

	def delete(self):
		if not self.destroyed:
			self.base.delete()

	@property
	def nodes(self):
		return self.base.nodes * self.T

	def __len__(self):
		return self.nodes

	@property
	def edges(self):
		return self.base.edges * self.T + (self.T-1) * ( self.base.nodes + 2 * self.base.edges )

	@property
	def edgelist(self):
		if not hasattr(self, 'E'):
			self.E = numpy.zeros((self.edges, 2), dtype = numpy.uint64)

			for v in range(self.base.nodes):
				for t in range(self.T-1):
					e = v * (self.T-1) + t
					self.E[e][0] = t * self.base.nodes + v
					self.E[e][1] = (t + 1) * self.base.nodes + v

			for f in range(self.base.edges):
				a = self.base.edgelist[f][0]
				b = self.base.edgelist[f][1]
				for t in range(self.T-1):
					e = (self.T-1) * self.base.nodes + f * 3 * (self.T-1) + t * 3
					self.E[e + 0][0] = t * self.base.nodes + a
					self.E[e + 0][1] = t * self.base.nodes + b
					self.E[e + 1][0] = t * self.base.nodes + a
					self.E[e + 1][1] = (t + 1) * self.base.nodes + b
					self.E[e + 2][0] = (t + 1) * self.base.nodes + a
					self.E[e + 2][1] = t * self.base.nodes + b

				e = (self.T-1) * self.base.nodes + (self.T-1) * 3 * self.base.edges + f
				self.E[e][0] = (self.T-1) * self.base.nodes + a
				self.E[e][1] = (self.T-1) * self.base.nodes + b

			self.E.flags.writeable = False

		return self.E

	def spatial_vertex(self, v):
		return v % self.base.nodes

	def time(self, v):
		return (v-self.spatial_vertex(v)) / self.base.nodes

	def is_spatial_edge(self, e):
		return self.time(self.edgelist[e][0]) == self.time(self.edgelist[e][1])

class Model(ctypes.Structure):
	"""
	Parameters
	----------
	weights : :class:`numpy.ndarray`
		Model weights
	graph : :py:class:`Graph`
		Undirected graph, representing the conditional independence structure
	states : Integer or 1-dimensional :class:`numpy.ndarray` of length at least :any:`graph.nodes`
		Vertex statespace sizes. Desired output data-type.
	stats : :class:`StatisticsType`, optional
		Determines wether the model's sufficient statistic is minimal or overcomplete (default). 
		For now, setting stats=StatisticsType.minimal requires states=2. 

	See Also
	--------
	:meth:`pxpy.train`, :meth:`pxpy.load_model`, :class:`StatisticsType`
	
	Notes
	-----
	The number of variables in the model is determinded by the number of nodes
	in the :any:`graph` (:any:`Graph.nodes`). Each variables's statespace size is controlled 
	via :any:`states`. If :any:`states` is an integer, all variables will have state spaces
	of that size. In case :any:`states` is a numpy.ndarray, statespace sizes for each variable
	are read from that array. This requires the user to manually set all the values in the array. 
	All numpy array which are passed to pxpy routines must be C-style contiguous. 
	
	Examples
	--------
	>>> import pxpy as px
	>>> import numpy as np
	>>> G = px.create_graph(px.GraphType.chain,nodes=32) # chain graph with 32 nodes
	>>> w = np.random.normal(size=G.nodes+G.edges) # random weight vector
	>>> P = px.Model(w, 2, G, StatisticsType.minimal)
	>>> P.predict()
	"""
	_fields_ = [("itype", ctypes.c_uint8), ("vtype", ctypes.c_uint8), ("from_file", ctypes.c_bool), ("from_python", ctypes.c_bool), ("G", ctypes.c_uint64), ("H", ctypes.c_uint64), ("w", ctypes.POINTER(ctypes.c_double)), ("empirical_stats", ctypes.POINTER(ctypes.c_double)), ("Y", ctypes.POINTER(ctypes.c_uint64)), ("__Ynames", ctypes.POINTER(ctypes.c_uint64)), ("__Xnames", ctypes.POINTER(ctypes.c_uint64)), ("dimension", ctypes.c_uint64), ("gtype", ctypes.c_uint64), ("T", ctypes.c_uint64), ("reparam", ctypes.c_uint64), ("K", ctypes.c_uint64), ("num_instances", ctypes.c_uint64), ("llist", ctypes.c_uint64), ("clist", ctypes.c_uint64)]

	__A         = None
	__observed  = None
	__marginals = None
	__woff      = None
	__voff      = None

	__ysum      = 0

	__weightsref = None
	__statesref  = None

	tree = False

	def __len__(self):
		if self.destroyed:
			return 0
		return self.dimension

	destroyed = False

	def delete(self):
		if not self.destroyed:
			self.__set_ctx_state()
			self.destroyed = True
			L = ["MPT"+str(ctypes.addressof(self))+";", "DEL MPT;"]
			recode(L)
			run()

	def __init__(self, weights, graph, states, stats = StatisticsType.overcomplete):

		super().__init__()

		if not isinstance(graph, Graph):
			raise TypeError('graph must be an instance of Graph')

		array_check(weights, "weights")

		if isinstance(states, numpy.ndarray):
			array_check(states, "states", numpy.uint64)
			if len(states) < graph.nodes:
				raise TypeError('states must contain one statespace size for each variable in the model')
		elif not isinstance(states, int):
			raise TypeError('states must be an int or of type numpy.ndarray with dtype uint64')

		if not isinstance(stats, StatisticsType):
			raise TypeError('model must have either covercomplete or minimal sufficient statistics')

		if stats == StatisticsType.minimal and ((isinstance(states, int) and states != 2) or (isinstance(states, numpy.ndarray) and not (np.unique(S)[0]==2 or len(np.unique(S))==1) )):
			raise TypeError('models with minimal sufficient statistics are only supported with 2 states per variable')

		self.itype = 3
		self.vtype = 5
		self.from_file = False
		self.from_python = True
		self.G = ctypes.addressof(graph)
		self.H = 0

		if isinstance(states, numpy.ndarray):
			self.Y = ctypes.cast(states.ctypes.data, ctypes.POINTER(ctypes.c_uint64))
			self.__statesref = states
		else:
			temp1 = states * numpy.ones(graph.nodes, dtype = numpy.uint64)
			self.Y = ctypes.cast(temp1.ctypes.data, ctypes.POINTER(ctypes.c_uint64))
			self.__statesref = temp1

		self._Model__Ynames = None
		self._Model__Xnames = None

		d = 0
		for e in range(graph.edges):
			d += self.states[graph.edgelist[e][0]] * self.states[graph.edgelist[e][1]]
		self.dimension = int(d)

		if stats == StatisticsType.minimal:
			self.reparam = 12
		else:
			self.reparam = 0

		if len(weights) < d:
			weights.resize(int(d), refcheck = False)
		self.w = ctypes.cast(weights.ctypes.data, ctypes.POINTER(ctypes.c_double))
		self.empirical_stats = None
		self.gtype = int(GraphType.other)
		#self.tree = is_tree
		self.T = 1
		self.K = 0
		self.num_instances = 1
		self.llist = 0
		self.clist = 0

		self.__A         = None
		self.__observed  = None
		self.__marginals = None

		self.__weightsref = weights # IMPORTANT! INCREASES REFCOUNT!

		self.prepare()

	def __set_ctx_state(self):
		write_register("MPT", ctypes.addressof(self))
		write_register("GPT", ctypes.addressof(self.graph))
		write_register("REP", self.reparam)
		write_register("GRA", self.gtype)
		if self.tree:
			write_register("TREE", 1)
		else:
			write_register("TREE", 0)

	def prepare(self):
		offset = 0
		self.obj = 0

		self.__woff = []
		for e in range(self.graph.edges):
			L = self.states[self.graph.edgelist[e][0]] * self.states[self.graph.edgelist[e][1]]
			self.__woff.append(offset)
			offset = offset + L
		self.__woff.append(offset)

		self.__voff = []
		for v in range(self.graph.nodes):
			self.__voff.append(offset)
			offset = offset + self.states[v]
			self.__ysum += self.states[v]
		self.__voff.append(offset)

	@property
	def dim(self):
		if self.destroyed:
			return 0
		if self.reparam == 12:
			return self.graph.nodes + self.graph.edges
		else:
			return self.dimension

	@property
	def time_frames(self):
		if self.destroyed:
			return 0
		return self.T

	@property
	def weights(self):
		if self.destroyed:
			return numpy.array([])
		if self.vtype == 3:
			return numpy.ctypeslib.as_array(self.w, shape = (self.dim, )).view('uint64')
		else:
			return numpy.ctypeslib.as_array(self.w, shape = (self.dim, ))

	def slice_edge(self, e, A):
		if self.destroyed:
			return numpy.array([])
		#if self.reparam == 12:
		#	raise TypeError('Edge slicing is only supported for overcomplete models')

		array_check(A,"A")

		if len(A) < self.dimension:
			raise TypeError('A must be (at least) ' + str(self.dimension) + ' dimensional')

		return A[int(self.__woff[e]):int(self.__woff[e + 1])]

	def slice_edge_state(self, e, x, y, A):
		if self.destroyed:
			return 0

		array_check(A,"A")

		w = self.slice_edge(e, A)

		s = self.graph.edgelist[e][0]
		t = self.graph.edgelist[e][1]

		idx = int(x * self.states[t] + y)

		return w[idx:(idx + 1)]

	@property
	def statistics(self):
		if self.destroyed:
			return numpy.array([])
		if self.empirical_stats is None:
			return None
		res = 0
		if self.vtype == 3:
			res = numpy.ctypeslib.as_array(self.empirical_stats, shape = (self.dimension, )).view('uint64') / self.num_instances
		else:
			res = numpy.ctypeslib.as_array(self.empirical_stats, shape = (self.dimension, )) / self.num_instances
		res.flags.writeable = False
		return res

	def phi(self, x):
		if self.destroyed:
			return numpy.array([])
		array_check(x,"x")

		if len(x) != self.graph.nodes:
			raise TypeError('x must be ' + str(self.graph.nodes) + ' dimensional')

		phi_x = numpy.zeros(shape = (self.dim, ))

		if self.reparam == 12:
			for v in range(self.graph.nodes):
				if x[v] >= self.states[v]:
					TypeError('Some values of x exceed the state space')

				phi_x[v] = int(x[v])

			for e in range(self.graph.edges):

				s = self.graph.edgelist[e][0]
				t = self.graph.edgelist[e][1]

				if x[s] >= self.states[s] or x[t] >= self.states[t]:
					TypeError('Some values of x exceed the state space')

				phi_x[int(self.graph.nodes + e)] = int(x[s] * x[v])
		else:
			for e in range(self.graph.edges):

				s = self.graph.edgelist[e][0]
				t = self.graph.edgelist[e][1]

				if x[s] >= self.states[s] or x[t] >= self.states[t]:
					TypeError('Some values of x exceed the state space')

				idx = int(self.__woff[e] + x[s] * self.states[t] + x[t])

				phi_x[idx] = 1

		return phi_x

	def score(self, x):
		if self.destroyed:
			return 0
		return numpy.inner(self.weights, self.phi(x))

	def edge_statespace(self, e):
		if self.destroyed:
			return numpy.array([])
		Xs = self.states[self.graph.edgelist[e][0]]
		Xt = self.states[self.graph.edgelist[e][1]]
		return numpy.array(list(itertools.product(range(Xs), range(Xt))))

	def save(self, filename):
		if self.destroyed:
			return
		self.__set_ctx_state()
		write_register("OVW", 1)
		L = []
		L.append("MFN \"" + filename + "\";")
		L.append("STORE MPT;")
		recode(L)
		run()

	def __load_observed(self, observed, L):
		if observed is not None:
			array_check(observed,"observed")
			if len(observed.shape) == 1:
				observed = observed.reshape(1, len(observed))
			if len(observed.shape) != 2:
				raise ValueError('observed must be 1 or 2 dimensional')

		data_ptr = ctypes.c_uint64(observed.ctypes.data)
		L.append("DEL DPT;")
		L.append("EDP " + str(data_ptr.value) + ";")
		L.append("NXX " + str(len(observed)) + ";")
		L.append("GPX " + str(len(observed) * len(observed[0]) * 2) + ";")
		L.append("LDX DPT;")

	def predict(self, observed, progress_hook = 0, iterations = 100):
		if self.destroyed:
			return numpy.array([])
		L = []
		self.__set_ctx_state()

		self.__load_observed(observed, L)

		if progress_hook != 0:
			f3 = prg_func(progress_hook)
			write_register("CBP", ctypes.c_uint64.from_buffer(f3).value)
		else:
			write_register("CBP", 0)

		write_register("PGX", 0)
		write_register("MIL", iterations)
		write_register("INF", int(InferenceType.belief_propagation))

		L.append("PREDICT;")
		
		recode(L)
		run()

		return observed

	def sample(self, observed = None, num_samples = None, sampler = SamplerType.apx_perturb_and_map, progress_hook = 0, iterations = 100, perturbation = 0.1, burn = 100):
		if self.destroyed:
			return numpy.array([])
		if not isinstance(sampler, SamplerType):
			raise TypeError('sampler must be an instance of SamplerType Enum')

		if not ((observed is None) != (num_samples is None)):
			raise ValueError('either observed or num_samples must be set (and not both)')

		L = []
		self.__set_ctx_state()

		if observed is None:
			observed = numpy.full(shape = (num_samples, self.graph.nodes), fill_value = MISSING_VALUE, dtype = numpy.uint16)

		self.__load_observed(observed, L)

		if progress_hook != 0:
			f3 = prg_func(progress_hook)
			write_register("CBP", ctypes.c_uint64.from_buffer(f3).value)
		else:
			write_register("CBP", 0)

		if sampler == SamplerType.apx_perturb_and_map:
			write_register("PAM", integer_from_float(perturbation))
			write_register("MIL", iterations)
			write_register("INF", int(InferenceType.belief_propagation))

		elif sampler == SamplerType.gibbs:
			write_register("PAM", 0)
			write_register("GRE", burn) # unified burn-in and resamplings between two samples

		L.append("SAMPLE;")
		recode(L)
		run()

		return numpy.array(observed)


	def infer(self, observed = None, inference = InferenceType.belief_propagation, iterations = 100, k = 3):
		if self.destroyed:
			return numpy.array([])
		if not isinstance(inference, InferenceType):
			raise TypeError('inference must be an instance of InferenceType Enum')

		L = []
		self.__set_ctx_state()

		if observed is not None:
			self.__load_observed(observed, L)
		else:
			L.append("DEL DPT;")
			L.append("DPT 0;")

		write_register("KXX", k)
		write_register("MIL", iterations)
		write_register("INF", int(inference))

		L.append("INFER;")
		recode(L)
		run()

		P = ctypes.cast(int(read_register("PPT")), ctypes.POINTER(ctypes.c_double))

		res = numpy.array(numpy.ctypeslib.as_array(P, shape = (int(self.dimension + self.__ysum), )))
		#res.flags.writeable = False

		self.__observed  = observed
		self.__marginals = res
		self.__A         = float_from_integer(read_register("LNZ"))

		return self.__marginals, self.__A

	def MAP(self):
		if self.destroyed:
			return numpy.array([])
		x = numpy.full(shape = (1, self.graph.nodes), fill_value = MISSING_VALUE, dtype = numpy.uint16)
		self.predict(x)
		return x

	def BIC(self):
		if self.destroyed:
			return 0
		N = self.num_instances
		k = numpy.linalg.norm(self.weights, ord=0)
		P, A = self.infer()
		lnL = N*(numpy.inner(self.weights, self.statistics)) - A
		return numpy.log(N)*k - 2*lnL

	def AIC(self):
		if self.destroyed:
			return 0
		N = self.num_instances
		k = numpy.linalg.norm(self.weights, ord=0)
		P, A = self.infer()
		lnL = N*(numpy.inner(self.weights, self.statistics)) - A
		return 2*k - 2*lnL

	__LOCAL_G = None

	@property
	def graph(self):
		if self.__LOCAL_G is None:
			#print("CONSTRUCTING LOCAL_G IN Model.graph()")
			if self.gtype == 11:
				self.__LOCAL_G = ctypes.cast(self.G, ctypes.POINTER(STGraph)).contents
			else:
				self.__LOCAL_G = ctypes.cast(self.G, ctypes.POINTER(Graph)).contents
		return self.__LOCAL_G


	@property
	def states(self):
		if self.destroyed:
			return numpy.array([])
		res = numpy.ctypeslib.as_array(self.Y, shape = (self.graph.nodes, ))
		return res

	def probv(self, v, x):
		if self.destroyed:
			return 0
		if self.__marginals is None:
			raise RuntimeError('you must call infer first')

		return self.__marginals[int(self.__voff[v]+x)]

	def prob(self, v, x, w = None, y = None):
		if self.destroyed:
			return 0
		if self.__marginals is None:
			raise RuntimeError('you must call infer first')

		if w is None or y is None:
			return self.probv(v, x)

		a0 = numpy.bincount(numpy.where(self.graph.edgelist==[v,w])[0])
		a1 = numpy.bincount(numpy.where(self.graph.edgelist==[w,v])[0])

		b0 = numpy.max(a0)
		b1 = numpy.max(a1)

		if b0 != 2 and b1 != 2:
			return self.prob(v,x) * self.prob(w,y)

		v0 = v
		v1 = w
		x0 = x
		x1 = y

		if b0 == 2:
			e = numpy.argmax(a0)
		else:
			e = numpy.argmax(a1)
			v0 = w
			v1 = v
			x0 = y
			x1 = x

		return self.__marginals[int(self.__woff[e] + x0 * self.states[x1] + x1)]

class progress_t(ctypes.Structure):
	_fields_ = [("_obj", ctypes.c_double), ("norm", ctypes.c_double), ("stepsize", ctypes.c_double), ("min_stepsize", ctypes.c_double), ("lam", ctypes.c_double), ("iteration", ctypes.c_uint64), ("max_iterations", ctypes.c_uint64), ("dim", ctypes.c_uint64), ("_w", ctypes.POINTER(ctypes.c_double)), ("_g", ctypes.POINTER(ctypes.c_double)), ("_e", ctypes.POINTER(ctypes.c_double)), ("is_int", ctypes.c_bool), ("_best_obj", ctypes.c_double), ("best_norm", ctypes.c_double), ("_best_w", ctypes.POINTER(ctypes.c_double)), ("value_bytes", ctypes.c_uint64), ("_model", ctypes.POINTER(Model))]

	@property
	def obj(self):
		if self.is_int != 0:
			return self._obj / 255.0
		else:
			return self._obj

	@property
	def best_obj(self):
		if self.is_int != 0:
			return self._best_obj / 255.0
		else:
			return self._best_obj

	@property
	def model(self):
		mod = self._model.contents
		mod.prepare()
		mod.obj = self.obj
		return mod

	@property
	def weights(self):
		if self.is_int != 0:
			return numpy.ctypeslib.as_array(self._w, shape = (self.dim, )).view('uint64')
		else:
			return numpy.ctypeslib.as_array(self._w, shape = (self.dim, ))

	@property
	def weights_extrapolation(self):
		if self.is_int != 0:
			return numpy.ctypeslib.as_array(self._e, shape = (self.dim, )).view('uint64')
		else:
			return numpy.ctypeslib.as_array(self._e, shape = (self.dim, ))

	@property
	def best_weights(self):
		if self.is_int != 0:
			return numpy.ctypeslib.as_array(self._best_w, shape = (self.dim, )).view('uint64')
		else:
			return numpy.ctypeslib.as_array(self._best_w, shape = (self.dim, ))

	@property
	def gradient(self):
		if self.is_int != 0:
			return numpy.ctypeslib.as_array(self._g, shape = (self.dim, )).view('uint64')
		else:
			return numpy.ctypeslib.as_array(self._g, shape = (self.dim, ))

if platform == "win32":
	opt_func = ctypes.WINFUNCTYPE(None, ctypes.POINTER(progress_t))
	prg_func = ctypes.WINFUNCTYPE(None, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_char_p)
else:
	opt_func = ctypes.CFUNCTYPE(None, ctypes.POINTER(progress_t))
	prg_func = ctypes.CFUNCTYPE(None, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_char_p)


ctx = ctypes.c_uint64(lib.create_ctx())

def write_register(name, val):
	l = len(name)
	buff = ctypes.create_string_buffer(l + 1)
	buff.value = name.encode('utf-8')
	ptr = (ctypes.c_char_p)(ctypes.addressof(buff))
	return lib.ctx_write_reg(ctx, ptr, val)

write_register("SEED", int(round(time.time() * 1000)))

def squared_l2_regularization(state_p):
	state = state_p.contents
	lam = 0.1
	numpy.copyto(state.gradient, state.gradient + 2.0 * lam * state.weights)
	state.norm = numpy.linalg.norm(state.gradient, ord=numpy.inf)

	if state.iteration == 1:
		state.min_stepsize = 1.0/(1.0/state.min_stepsize + 2.0 * lam)

def prox_l1(state_p):
	state = state_p.contents
	l = state.lam * state.stepsize

	x = state.weights_extrapolation - state.stepsize * state.gradient

	numpy.copyto(state.weights, 0, where=numpy.absolute(x)<l)
	numpy.copyto(state.weights, x-l, where=x>l)
	numpy.copyto(state.weights, x+l, where=-x>l)

def version():
	return lib.version()

def discretize(data, num_states = None, targets = None, discretization = None):
	array_check(data,"data")

	if num_states is None and discretization is None:
		raise ValueError('either a desired number of states or a precomputed discretization must be provided')

	columns = len(data[0])

	R = numpy.zeros(shape = (len(data), columns), dtype = numpy.uint16)
	M = []

	if targets is None:
		targets = range(columns)

	for col in range(columns):
		col_data = numpy.ascontiguousarray(data[:, col])
		distinct = len(numpy.unique(col_data))
		if col in targets and (num_states is not None and distinct > num_states):
			result = numpy.zeros(shape = (len(data), ), dtype = numpy.uint16)

			if discretization is None:
				disc_info = lib.discretize(ctypes.c_uint64(result.ctypes.data), ctypes.c_uint64(col_data.ctypes.data), ctypes.c_uint64(len(data)), ctypes.c_uint64(num_states))

			else:
				disc_info = discretization[col]
				lib.discretize_precomputed(ctypes.c_uint64(result.ctypes.data), ctypes.c_uint64(col_data.ctypes.data), ctypes.c_uint64(len(data)), disc_info)
				
			M.append(disc_info)
			R[:, col] = result
		else:
			M.append(None)
			R[:, col] = col_data
	return R, M

def undiscretize(data, M):
	array_check(data,"data")

	R = numpy.zeros(shape = (len(data), len(data[0])))

	with numpy.nditer(data, flags = ['multi_index']) as it:
		while not it.finished:
			row = it.multi_index[0]
			col = it.multi_index[1]
			R[row, col] = M[col].moments[it[0]][0]
			it.iternext()
	return R

def run():
	if ctx is None:
		assert False
	lib.run_ctx(ctx)

def destroy():
	if ctx is None:
		assert False
	lib.destroy_ctx(ctx)

def read_register(name):
	l = len(name)
	buff = ctypes.create_string_buffer(l + 1)
	buff.value = name.encode('utf-8')
	ptr = (ctypes.c_char_p)(ctypes.addressof(buff))
	return lib.ctx_read_reg(ctx, ptr)

def recode(code):
	n = len(code)
	l = 0
	for stmt in code:
		if len(stmt) > l:
			l = len(stmt)
	buffs = [ctypes.create_string_buffer(l + 1) for i in range(len(code))]
	for index, stmt in enumerate(code):
		buffs[index].value = code[index].encode('utf-8')
	ptrs = (ctypes.c_char_p * n)( * map(ctypes.addressof, buffs))
	lib.ctx_set_code(ctx, ptrs, n)
	return n

def set_seed(s):
	write_register("SEED", s)

def float_from_integer(val):
	return struct.unpack('d', struct.pack('N', val))[0]

def integer_from_float(val):
	return struct.unpack('N', struct.pack('d', val))[0]

def KL(p, q):
	array_check(p,"p")
	array_check(q,"q")

	#if len(p) != len(q):
	#	raise TypeError('p and q must have same length')

	res = 0
	for i in range(min(len(p),len(q))):
		res = res + p[i] * (numpy.log(p[i]) - numpy.log(q[i]))

	return res

def load_model(filename):
	L = []
	L.append("MFN \"" + filename + "\";")
	L.append("LDX MPT;")
	L.append("DEL MFN;")
	L.append("DEL LPT;")
	L.append("DEL IGN;")
	recode(L)
	run()
	mod = ctypes.cast(read_register("MPT"), ctypes.POINTER(Model)).contents
	mod.prepare()
	return mod

def create_graph(G, nodes=None):
	if isinstance(G, numpy.ndarray) and len(G[0]) != 2:
		array_check(G,"G",dtype=numpy.uint64)
	elif isinstance(G, GraphType) and nodes is None:
		raise TypeError('G must be an instance of GraphType or numpy.ndarray with dtype uint64')


	write_register("DPT", 0)
	write_register("MPT", 0)
	write_register("GPT", 0)
	lib.reset_ctx(ctx)

	L = []
	L.append("idx_t UINT64;")
	L.append("val_t FLT64;")

	if isinstance(G, GraphType):
		L.append("GVX " + str(nodes) + ";")
		L.append("GRA " + str(int(G)) + ";")
	else:
		M = numpy.amax(G)
		V = numpy.unique(G)
		n = len(V)
		m = len(G)
		s = numpy.sum(V)

		if (n != M + 1) or (s != (M * (M + 1))/2):
			raise ValueError('provided G is invalid')

		data_ptr = ctypes.c_uint64(G.ctypes.data)

		L.append("EAP " + str(data_ptr.value) + ";")
		L.append("GVX " + str(n) + ";")
		L.append("GEX " + str(m) + ";")
		L.append("GRA " + str(int(GraphType.custom)) + ";")

	L.append("LDX GPT;")
	recode(L)
	run()

	G = ctypes.cast(read_register("GPT"), ctypes.POINTER(Graph)).contents
	G._Graph__edgelistref = G # IMPORTANT! INCREASES REFCOUNT!

	return G

def train(data, graph=None, mode = Mode.mrf, inference = InferenceType.belief_propagation, iters = 1000, seed = 0, k = 3, in_model = None, initial_stepsize = 0.01, opt_progress_hook = 0, progress_hook = 0, opt_regularization_hook = 0, opt_proximal_hook = 0, T = 1, edge_fraction = 0.1, lam = 0, shared_states = False, optimizer = Optimizer.accelerated_proximal_gradient, zero_init=False):
	"""Return a new matrix of given shape and type, without initializing entries.

	Parameters
	----------
	shape : int or tuple of int
		Shape of the empty matrix.
	dtype : data-type, optional
		Desired output data-type.
	order : {'C', 'F'}, optional
		Whether to store multi-dimensional data in row-major
		(C-style) or column-major (Fortran-style) order in
		memory.

	See Also
	--------
	empty_like, zeros

	Notes
	-----
	`empty`, unlike `zeros`, does not set the matrix values to zero, 
	and may therefore be marginally faster. On the other hand, it requires
	the user to manually set all the values in the array, and should be
	used with caution.

	Examples
	--------
	>>> import numpy.matlib
	>>> np.matlib.empty((2, 2))	# filled with random data
	matrix([[  6.76425276e-320,   9.79033856e-307], # random
			[  7.39337286e-309,   3.22135945e-309]])
	>>> np.matlib.empty((2, 2), dtype = int)
	matrix([[ 6600475, 		0], # random
			[ 6586976, 22740995]])

	"""

	if in_model is None and graph is None:
		raise TypeError('either in_model or graph must be defined')


	if graph is not None and (not (isinstance(graph, GraphType) or isinstance(graph, Graph))):
		raise TypeError('graph must be an instance of GraphType enum or Graph class')

	if in_model is not None and not isinstance(in_model, Model):
		raise TypeError('in_model must be an instance of Model Class')

	array_check(data,"data",dtype=numpy.uint16)

	if in_model is not None and data.shape[1] != in_model.graph.nodes:
		raise TypeError('dimension mismatch in data and in_model')

	if not isinstance(mode, Mode):
		raise TypeError('mode must be an instance of ModeType enum')

	if not isinstance(inference, InferenceType):
		raise TypeError('inference must be an instance of InferenceType enum')

	write_register("MPT", 0)
	write_register("GPT", 0)
	lib.reset_ctx(ctx)

	if opt_progress_hook != 0:
		f1 = opt_func(opt_progress_hook)
		write_register("CBO", ctypes.c_uint64.from_buffer(f1).value)
	else:
		write_register("CBO", 0)

	if opt_regularization_hook != 0:
		f2 = opt_func(opt_regularization_hook)
		write_register("CBU", ctypes.c_uint64.from_buffer(f2).value)
	else:
		write_register("CBU", 0)

	if progress_hook != 0:
		f3 = prg_func(progress_hook)
		write_register("CBP", ctypes.c_uint64.from_buffer(f3).value)
	else:
		write_register("CBP", 0)

	if opt_proximal_hook != 0:
		f4 = opt_func(opt_proximal_hook)
		write_register("CPR", ctypes.c_uint64.from_buffer(f4).value)
	else:
		write_register("CPR", 0)

	L = []
	L.append("DEL MPT;");

	if mode == Mode.integer:
		L.append("idx_t UINT64;")
		L.append("val_t UINT64;")
		L.append("ALG IGD;")
	else:
		write_register("STP", integer_from_float(initial_stepsize))
		L.append("idx_t UINT64;")
		L.append("val_t FLT64;")
		L.append("ALG "+str(int(optimizer))+";")

	write_register("KXX", k)
	if seed != 0:
		write_register("SEED", seed)
	write_register("MIS", ord('?'))
	write_register("SEP", ord(','))
	write_register("OVW", 1)
	write_register("HED", 0)
	write_register("LSN", 2)

	write_register("INF", int(inference))
	write_register("MIL", 100)
	write_register("MIO", iters)
	write_register("EPO", 0)
	write_register("LAM", integer_from_float(lam))
	write_register("ELAM", 0)

	if mode >= Mode.strf_linear and mode <= Mode.strf_inv_exponential:
		write_register("TXX", T)
		write_register("YYC", 1)
	else:
		write_register("TXX", 1)
		write_register("YYC", 0)
		write_register("REP", 0)

	if shared_states:
		write_register("YYC", 1)

	data_ptr = ctypes.c_uint64(data.ctypes.data)

	L.append("EDP " + str(data_ptr.value) + ";")
	L.append("NXX " + str(len(data)) + ";")
	L.append("GPX " + str(len(data) * len(data[0]) * 2) + ";")
	L.append("LDX DPT;")

	if in_model is None:
		if isinstance(graph, Graph):
			L.append("GRA " + str(int(GraphType.custom)) + ";")
			L.append("GPT " + str(ctypes.addressof(graph)) + ";")
		else:
			L.append("GRA " + str(int(graph)) + ";")
			#if graph == GraphType.chain or graph == GraphType.auto_tree:
			#	L.append("TREE 1;")				
			#else:
			#	L.append("TREE 0;")
			L.append("TREE 0;")
			L.append("LDX GPT;")

		if not isinstance(graph, Graph)and graph == GraphType.auto:
			L.append("PEL " + str(edge_fraction) + ";")
		L.append("MODEL;")

		if mode == Mode.dbt:
			L.append("DEL MPT;")
			L.append("GRA OTHER;")
			L.append("LSN 8192;")
			L.append("BOLTZMANNTREE;")
			L.append("INITLATENT;")
			L.append("MODEL;")

		elif mode >= Mode.strf_linear and mode <= Mode.strf_inv_exponential and T>1:
			L.append("DEL MPT;")
			L.append("GRA OTHER;")
			L.append("STGRAPH;")
			L.append("TREE 0;")
			L.append("REP " + str(int(mode)) + ";")
			L.append("MODEL;")

		if not zero_init and mode != Mode.integer and opt_regularization_hook == 0 and opt_proximal_hook == 0:
			L.append("CLOSEDFORM;")

	else:
		L.append("MPT " + str(ctypes.addressof(in_model)) + ";")
		L.append("GPT " + str(ctypes.addressof(in_model.graph)) + ";")
		L.append("REP " + str(in_model.reparam) + ";")
		L.append("GRA " + str(in_model.gtype) + ";")
		L.append("STATS;")

	L.append("ESTIMATE;")

	recode(L)
	run()

	mod = ctypes.cast(read_register("MPT"), ctypes.POINTER(Model)).contents
	mod.prepare()

	res = read_register("RES")
	if mode != Mode.integer:
		res = float_from_integer(res)

	mod.obj = res

	return mod
