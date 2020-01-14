import dwavebinarycsp as dbc;
import math;
from pymongo import MongoClient;
import numpy as np;
import pandas as pd;
from hybrid import State, States;
import matplotlib.pyplot as plt;
from echarts import Echart, Legend, Bar, Axis;
#from operators import Operator;


MATPLOTLIB_VISUALIZATION = "matplotlib";
ECHART_VISUALIZATION = "echart";
THREEJS_VISUALIZATION = "threejs";


class QUnit(tuple):


	def __new__(self, *args, **kwargs):
		try:
			some_iterator = iter(*args[1:]);
			return tuple.__new__(self, *args[1:])
		except TypeError as e:
			return tuple.__new__(self, (None,))


	def __init__(self, *args, **kwargs):
		if len(args) == 1 and type(args[0]) == QUnit:
			self.amplitude = args[0].amplitude;
			self.state = args[0].state;
			self.key = args[1] if len(args) > 1 else None;
			self.model = args[0].model;
		elif len(args) >= 1:
			self.amplitude = args[0];
			self.state = args[1:] if len(args) > 1 else None;
			self.key = args[1] if len(args) > 1 else None;
			from qmodel import QModel;
			self.model = kwargs.get("model") if "model" in kwargs else QModel();


	def get_state_string(self):
		state_string = "";
		for s in self.state:
			state_string = state_string + "," + s if len(state_string)>0 else str(s);
		return state_string;



	def set_model(self, model):
		self.model = model;


	def get_model(self):
		return self.model




	def split(self, amplitudes):
		split_index = int(len(self.state)/len(amplitudes));
		partition = sum(list(amplitudes));
		return (QUnit(amplitudes[i], self.state[i*split_index:(i+1)*split_index]) for i in range(len(amplitudes)));


	def to_qdata(self):
		return QData([self]);


	def to_qtdata(self):
		return QTData([self]);



	def __sub__(self, qb):
		return self.model.processor.__sub__(self, qb);


	def __add__(self, qb):
		return self.model.processor.__add__(self, qb);


	def __eq__(self, qb):
		return self.model.processor.__eq__(self, qb);


	def __mul__(self, a):
		return self.model.processor.__mul__(self, a);



	def __repr__(self):
		state_string="";
		if self.state == None:
			return str(self.amplitude)+"|None>";
		else:
			return str(self.amplitude)+"|"+self.get_state_string()+">";



	def copy(self):
		return tuple(list(self).copy());



	def to_tuple(self):
		return tuple(self);



	def to_qubo(self):
		linear = {(self.key, self.key): (self.amplitude.conjugate()*self.amplitude)};
		quadratic = {};
		qubo = dict(linear); qubo.update(quadratic);
		return qubo;




	def transpose(self):
		amplitude = complex(self.amplitude).conjugate();
		return QTUnit(amplitude, *self.state);


	def t(self):
		return self.transpose();




class QTUnit(QUnit):


	def __repr__(self):
		if self.state == None:
			return "<None|"+str(self.amplitude);
		else:
			return "<"+self.get_state_string()+"|"+str(self.amplitude);


	def transpose(self):
		return QUnit(complex(self.amplitude).conjugate(), self.state);



	def to_qtdata(self):
		return QTData([self]);


	def to_qdata(self):
		return QData([self]);




class QData(list):

	def __init__(self, states, **kwargs):
		if type(states) == tuple:
			states = list(states);
		if type(states) != list:
			states = [states];
		if len(states) > 0:
			if type(states[0]) == tuple or type(states[0]) == list:
				states = [QUnit(*v) for v in states];
				super(QData, self).__init__(states);
			elif type(states[0]) == QUnit:
				super(QData, self).__init__(states);
			else:
				states = [QUnit(1, v) for v in states]
				super(QData, self).__init__(states);
		self.states = states;
		self.keys = [s.key for s in states];
		from qmodel import QModel;
		self.model = kwargs.get("model") if "model" in kwargs else QModel();




	def __getitem__(self, key):
		if type(key) == str:
			return QData([(x.amplitude, *x.state) for x in self.states if x.key == key]);
		elif type(key) == int:
			return super(QData, self).__getitem__(key);
		else:
			return QData(super(QData, self).__getitem__(key));


	def get_state_string(self, k):
		state_string = "";
		for s in self.states[k].state:
			state_string = state_string + "," + s if len(state_string)>0 else str(s);
		return state_string;


	def __len__(self):
		return len(self.states);


	def __repr__(self):
		rep = ""
		m = 1;
		for k in range(self.states.__len__()):
			if self.states[k].amplitude < 1:
				if k > 0 and rep[-1:] != "\n":
					rep = rep[:-2] + "- ";
				else: 
					rep ="-";
			if k != len(self.states)-1:
				rep = rep+str(abs(self.states[k].amplitude))+"|"+self.get_state_string(k)+"> + ";
				if (len(rep)-2*m+2)/(70*m) > 1:
					rep = rep + "\n";
					m = m + 1;
			else:
				rep = rep+str(abs(self.states[k].amplitude))+"|"+self.get_state_string(k)+">"
		return rep;


	def __mul__(self, a):
		return self.model.processor.__mul__(self, a);


	def __add__(self, a):
		return self.model.processor.__add__(self, a);



	def __sub__(self, a):
		return self.model.processor.__sub__(self, a);


	def __eq__(self, qb):
		return self.model.processor.__eq__(self, qb);


	def condense(self):
		return self.model.processor.condense(self);



	def plot(self, backend=None):
		labels = self.keys;
		st_labels = [x.state for x in self.states];
		amplitudes = [ self[label].states[0].amplitude for label in labels]
		if backend == None or backend == MATPLOTLIB_VISUALIZATION:
			x_pos = np.arange(len(labels))
			plt.bar(x_pos, amplitudes, width=0.2, align='center', alpha=0.8);
			plt.xticks(x_pos, labels);
			plt.xlabel("States");
			plt.ylabel("Amplitude");
			plt.title("QData Spectrum");
			return plt;
		elif backend == ECHART_VISUALIZATION:
			pass
		elif backend == THREEJS_VISUALIZATION:
			pass


	def set_model(self, model):
		self.model = model;


	def get_model(self):
		return model



	def transpose(self):
		return QTData([x.transpose() for x in self]);




	def t(self):
		return self.transpose();



	def condense(self):
		set([state for state in self.states])
		return self;


	def expand(self):
		return self;



	def to_qubo(self):
		linear = {(key, key): self.states[key].amplitude for key in keys};
		quadratic = {(keys[i], keys[j]): (self.states[keys[i]].amplitude.conjugate()*self.states[keys[j]].amplitude + 
			self.states[keys[j]].amplitude.conjugate()*self.states[keys[i]].amplitude) for i in range(len(keys)) for j in range(len(keys)) if i > j}
		qubo = dict(linear); qubo.update(quadratic);
		return qubo;




class QTData(QData):


	def __init__(self, states, **kwargs):
		if type(states) == tuple:
			states = list(states);
		if type(states) != list:
			states = [states];
		if len(states) > 0:
			if type(states[0]) == tuple or type(states[0]) == list:
				states = [QTUnit(*v) for v in states];
				super(QTData, self).__init__(states);
			elif type(states[0]) == QTUnit:
				super(QTData, self).__init__(states);
			else:
				states = [QTUnit(1, v) for v in states]
				super(QTData, self).__init__(states);
		self.states = states;
		self.keys = [s.key for s in states];
		from qmodel import QModel;
		self.model = kwargs.get("model") if "model" in kwargs else QModel();






	def __repr__(self):
		rep = ""
		m = 1;
		for k in range(self.states.__len__()):
			if self.states[k].amplitude < 1:
				if k > 0 and rep[-1:] != "\n":
					rep = rep[:-2] + "- ";
				else: 
					rep ="-";
			if k != len(self.states)-1:
				rep = rep+"<"+self.get_state_string(k)+"|"+str(abs(self.states[k].amplitude))+" + ";
				if (len(rep)-2*m+2)/(70*m) > 1:
					rep = rep + "\n";
					m = m + 1;
			else:
				rep = rep+"<"+self.get_state_string(k)+"|"+str(abs(self.states[k].amplitude));
		return rep;


	def transpose(self):
		return QData([x.transpose() for x in self.states]);




class QSystem():



	def __init__(self, qT, H, q, model=None):
		self.qT=qT;
		self.H = H;
		self.q =q;
		from qmodel import QModel;
		self.model = model if model != None else self.H.get_model();



	def __repr__(self, a):
		"""
			< q | A | q > 

			< q | A | q > = expected value of A
			< q | I | q > = probability of state | q >

			processor: [Processor Representation]
			individual_processors:[ list of Processor Representation]

		"""
		return self.qT.__repr__()+self.H.__repr__()+self.q.__repr__()+"\n"+self.processor.__repr__();



	def __mul__(self, a):
		return self.model.processor.__mul__(self, a);



	def __add__(self, a):
		return self.model.processor.__add__(self, a);



	def __sub__(self, a):
		return self.model.processor.__sub__(self, a);



	def __div__(self, a):
		return self.model.rocessor.__div__(self, a);



	def __add__(self, a):
		return self.model.processor.__add__(self, a);



	def __mod__(self, a):
		return self.model.processor.__mod__(self, a);


	def __eq__(self, qb):
		return self.model.processor.__eq__(self, qb);



	def eval(self, sampler):
		return sampler.sample(bqm);



	def find_entanglements(self):
		pass



	def find_bindings(self):
		return self.find_entanglements();




class QEntangle(QData):


	def __init(self):
		pass
 
	def __init__(self, value):
		super(QEntangle, self).__init__();
		self.value = __check_value_is_valid__(value);



	def __repr__(self):
		"""
		['a=b'];
		['a=b']+['c=d']
		['a=b']*['c=d']
		['a=b']/['c=d']
		['a=b']//['c=d']
		['a=b']%['c=d']
		['a=b']%%['c=d']
		['a=b=c']
		['a=b=c']+[d=e]
		['a=b=c']*[d=e]
		['a=b=c']+[d=e]
		['a=b=c']/[d=e]
		['a=b=c']//[d=e]
		['a=b=c']%[d=e]
		['a=b=c']%%[d=e]
		"""
		return str([x for x in self.value]);


	def __check_value_is_valid__(self, value):
		try:
			return value;
		except Exception as e:
			raise e;




class QBind(QEntangle):
	"""docstring for QBind"""
	def __init__(self, arg):
		super(QBind, self).__init__()
		




class Quantumic(list, QSystem):
	"""
	QuantumIC is a list or sequence of Quantum Systems(QSystems) which some qubits are binded by quantum entanglement
	"""


	def __init__(self, bin_tuple_array=None, sample=None, state=None, value=[(0,)], n_qbits=(5,), index=[(0,0,0)], labels=({'a':2,'b':2,'c':3},)):
		"""
		bin_tuple_array: [(value in binary 0, concatenated binary indexes 0), (value in binary 1, concatenated binary indexes 1), ... ]
		"""
		self.labels = labels;
		self.sampler = sampler;
		self.value_indexes = list((tuple([value]+index)));
		if bin_tuple_array != None:
			self.from_bin_tuple_array(bin_tuple_array);
			super(Quantumic, self).__init__(bin_tuple_array);
		if sample != None:
			self.from_sample(sample);
		if state != None:
			self.from_state(state);
		else:
			self.state_str = self.value_indexes
			self.n_qbits = n_qbits;
			self.total_n_qbits = tuple([n_qbits[i]+sum([ math.log2(v) for k,v in labels[i].items()]) for i in range(len(n_qbits))])


	def __repr__(self):
		"""
		H | q1 >[ q1[a]=q1[b], q2[a]=q1[c] ]< q2 | G | q3 >

		< q0 | H [ q1[a]=q1[b], q2[a]=q1[c] ] G | q3 >

		< q0 | H | q1 >[ q1[a]=q1[b], q2[a]=q1[c] ]< q2 | G | q3 >

		< q0 | H | q1 >[ q1[a]=q1[b], q2[a]=q1[c] ]< q2 | G | q3 > = energy

		processor = [ Processor Representation]
		"""
		temp = ""
		for value in self.values:
			temp+=values.__repr__();
		return temp


	def __eq__(self, qb):
		return self.processor.__sub__(self, qb);


	def __sub__(self, qb):
		return self.processor.__sub__(self, qb);


	def __add__(self, qb):
		return self.processor.__add__(self, qb);



	def __mul__(self, a):
		return self.processor.__mul__(self, a);




	def __mul__(self, qb):
		product = Quantumic()
		if type(qb) == Quantumic:
			product.value_indexes = self.value_indexes+qb.value_indexes;
			product.state_str = product.value_indexes
			product.labels = self.labels+qb.labels;
			product.n_qbits = self.n_qbits+qb.n_qbits
			product.total_n_qbits = self.total_n_qbits + qb.total_n_qbits;
			return product
		elif type(qb) == Operator:
			return qb.leftDot(self);


	def __add__(self, qb):
		ADD=Operator().ADD;
		if type(qb) == Quantumic:
			addition_state = self*qb;
			return ADD*addition_state;




	def __sub__(self, qb):
		SUB=Operator().SUB;
		if type(qb) == Quantumic:
			addition_state = self*qb;
			return SUB*addition_state;

	

	def save(self, use_db=False):
		pass



	def dot(self, qb):
		#	Use Optimization Problem approach with DWave System.
		if type(qb) == Quantumic():
			def energy_function(qa, qb):
				pass;
			csp = dbc.Constraint(energy_function, self.labels(), dbc.BINARY, 'dot product');
			csp.add_values(self.to_dict());
			csp.add_values(qb.to_dict())
			bqm = dbc.stitch(csp);
			response = self.sampler.sample(bqm);
			response.energy();
		elif type(qb) == Operator():
			qb.leftDot(self);



	def add(self, qb):
		pass



	def fit(self, *args, **kwargs):
		pass



	def predict(self, *args, **kwargs):
		pass



	def evaluate(self, *args, **kwargs):
		pass



	def from_sample(self, sample):
		pass



	def from_state(self, state):
		pass



	def from_bin_tuple_array(self, bin_tuple_array):
		"""
		bin_tuple_array: [(value in binary 0, concatenated binary indexes 0), (value in binary 1, concatenated binary indexes 1), ... ]
		"""
		no_of_composites = len(bin_tuple_array);
		to_float = lambda v: v;
		to_int = lambda v: v;
		self.n_qbits = sum([len(bin_tuple_array[0][0]) for i in range(no_of_composites)]);
		self.value_indexes = list((to_int(bin_tuple_array[i][0]), to_int(bin_tuple_array[i][1])) for i in range(no_of_composites));
		self.total_n_qbits = tuple([len(bin_tuple_array[i][0]) + len(bin_tuple_array[i][1]) for i in range(no_of_composites)])




class Quantumics():

	def __init__(self, qOutputHibertspace, qOperator, qInputHilbertspace, model=None):
		if qInputClass == QSystem:
			self.system = qOutputClass;
		elif qInputClass == Quantumic:
			self.system = qOutputClass;
		elif qOutputClass == QData and qInputClass==QData:
			pass;
		from qmodel import QModel;
		self.model = model if model != None else QModel();



	def set_database(self, database):
		self.model.database = database if type(database) == q.QDatabase else None;




	def set_hilbertspace(self, hilbertspace):
		self.model.database = database if type(database) == q.QDatabase else None;



	def start(self):
		return self.model.server.start();



		








