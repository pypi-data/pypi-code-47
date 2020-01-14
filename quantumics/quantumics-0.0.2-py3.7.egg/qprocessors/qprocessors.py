import dwavebinarycsp as dbc;
from qiskit import ClassicalRegister as CR, QuantumRegister as QR, QuantumCircuit as QC
import math;
from dwave.system.samplers import DWaveSampler;
from qiskit import IBMQ, backends;
import theano.tensor as T;
from hybrid import State, States;
from pymongo import MongoClient;
import numpy as np;
import sklearn as skl;
#import qsharp
from ..qoperators import QOperator;
from ..core import QUnit, QTUnit, QData, QTData;
from ..qmaps import QMap;
from ..qdatabases import QDatabase;
#import Microsoft.Samples as ms



DWAVE_MODE_TEST = "DWAVE SIMULATED ANNEALER";
DWAVE_MODE_EXACT = "DWAVE EXACT SOLVER";
DWAVE_MODE_1000Q = "DWAVE 1OOOQPU SAMPLER";
DWAVE_MODE_2000Q = "DWAVE 2000QPU SAMPLER";
DWAVE_MODE_2000XQ = "DWAVE 2000XQPU SAMPLER";






class QProcessor():

	def __init__(self, mins=[0,0,0,0], database=QDatabase('mongodb://localhost:7000'), 
		maxs=[16, 16, 16, 16], delayed=False):
		self.delayed = delayed
		self.maxs = maxs;
		self.mins = mins;
		self.database = database;




	def __mul__(self, a, b):
		return self.dot(a,  b);



	def __add__(self, a, b):
		return self.add(a, b);



	def __sub__(self, a, b):
		return self.sub(a, b);



	def __eq__(self, a, b):
		return self.equal(a, b);



	def equal(self, a, b):
		if type(a) == QUnit or type(a) == QTUnit:
			return (type(a) == type(b)) and (a.amplitude == b.amplitude) and (a.state == b.state)
		elif type(a) == QData or type(b) == QTData:
			return (type(a) == type(b)) and (a.states == b.states)
		elif type(a) == QMap and type(b) == QMap:
			return dict(a) == dict(b);


	def dot(self, qa, qb):
		"""
		Use Optimization Problem approach with DWave System.
		"""
		if (type(qa)== QUnit or type(qa) == QTUnit) and (type(qb)== QUnit or type(qb) == QTUnit):
			return self.unit_mul(qa, qb);
		elif (type(qa)== QData or type(qa) == QTData) and (type(qb)== QData or type(qb) == QTData):
			return self.data_mul(qa, qb);
		elif type(qa)== QOperator and type(qb)==QUnit:
			return self.operator_qunit(qa, qb);
		elif type(qa)== QOperator and type(qb)==QOperator:
			return self.operator_mul(qa, qb);
		elif type(qa)== QTUnit and type(qb)==QOperator:
			return self.qtunit_operator(qa, qb);
		elif type(qa)== QOperator and type(qb)==QData:
			return self.operator_qdata(qa, qb);
		elif type(qa)== QTData and type(qb)==QOperator:
			return self.qtdata_operator(qa, qb);
		elif (type(qa) == QMap or issubclass(type(qa), QMap))  and type(qb) == QUnit:
			return self.qmap_qunit_mul(qa, qb);
		elif (type(qb) == QMap or issubclass(type(qb), QMap)) and type(qa) == QTUnit:
			return self.qtunit_qmap_mul(qa, qb);
		elif (type(qa) == QMap or issubclass(type(qa), QMap)) and type(qb) == QData:
			return self.qmap_qdata_mul(qa, qb);
		elif (type(qb) == QMap or issubclass(type(qb), QMap)) and type(qa) == QTData:
			return self.qtdata_qmap_mul(qa, qb);




	def div(self, qa, qb):
		"""
		Use Optimization Problem approach with DWave System.
		"""
		if type(qa)== QUnit and type(qb)==QUnit:
			return self.qunit_mul(qa, qb);
		elif type(qa)== Operator and type(qb)==QUnit:
			return self.operator_qunit(qa, qb);
		elif type(qa)== Operator and type(qb)==Operator:
			return self.operator_mul(qa, qb);
		elif type(qa)== QTUnit and type(qb)==Operator:
			return self.qtunit_operator(qa, qb);
		elif type(qa)== QTUnit and type(qb)==QTUnit:
			return self.qtunit_mul(qa, qb);
		elif type(qa)== QTUnit and type(qb)==QUnit:
			return self.qtunit_qunit(qa, qb);
		elif type(qa)== QUnit and type(qb)==QTUnit:
			return self.qunit_qtunit(qa, qb);
		elif type(qa)== QData and type(qb)==QData:
			return self.qdata_mul(qa, qb);
		elif type(qa)== Operator and type(qb)==QData:
			return self.operator_qdata(qa, qb);
		elif type(qa)== QTData and type(qb)==Operator:
			return self.qtdata_operator(qa, qb);
		elif type(qa)== QTData and type(qb)==QTData:
			return self.qtdata_mul(qa, qb);
		elif type(qa)== QTData and type(qb)==QData:
			return self.qtdata_qdata(qa, qb);
		elif type(qa)== QData and type(qb)==QTData:
			return self.qdata_qtdata(qa, qb);



	def add(self, qa, qb):
		"""
		Use Optimization Problem approach with DWave System.
		"""
		if type(qa) != type(qb):
			if type(qa) == QData and type(qb) == QUnit:
				return self.qdata_qunit_add(qa, qb);
			elif type(qb) == QData and type(qa) == QUnit:
				return self.qdata_qunit_add(qb, qa);
			elif type(qa) == QTData and type(qb) == QTUnit:
				return self.qtdata_qtunit_add(qb, qa);
			elif type(qb) == QTData and type(qa) == QTUnit:
				return self.qtdata_qtunit_add(qb, qa);
		elif type(qa) == type(qb):
			if type(qa) == QOperator:
				return self.operator_add(qa, qb);
			elif type(qa) == QUnit or type(qa) == QTUnit:
				return self.unit_add(qa, qb);
			elif type(qa) == QData or type(qa) == QTData and type(qa)==type(qb):
				return self.data_add(qa, qb);
			elif type(qa) == Quantumic(qa, qb):
				return self.quantumic_add(qa, qb);
			elif type(qa) == QEntangle or type(qa) == QBind:
				return self.qentangle_add(qa, qb);
			elif type(qa) == QSystem(qa, qb):
				return self.qsystem_add(qa, qb);
			elif type(qa) == Quantumics(qa, qb):
				return self.quantumics_add(qa, qb);



	def sub(self, qa, qb):
		"""
		Use Optimization Problem approach with DWave System.
		"""
		if type(qa) != type(qb):
			raise Exception();
		elif type(qa) == type(qb):
			if type(qa) == QOperator:
				return self.operator_sub(qa, qb);
			elif type(qa) == QUnit or type(qa) == QTUnit:
				return self.unit_sub(qa, qb);
			elif type(qa) == QData(qa, qb) or type(qa) == QTData:
				return self.data_sub(qa, qb);
			elif type(qa) == Quantumic(qa, qb):
				return self.quantumic_sub(qa, qb);
			elif type(qa) == QEntangle or type(qa) == QBind:
				return self.qentangle_sub(qa, qb);
			elif type(qa) == QSystem(qa, qb):
				return self.qsystem_sub(qa, qb);
			elif type(qa) == Quantumics(qa, qb):
				return self.quantumics_sub(qa, qb);


	def train(self, *args, **kwargs):
		return self.hamiltonian(*args, **kwargs)



	def fit(self, *args, **kwargs):
		return self.hamiltonian(*args, **kwargs);




	def eval(self, a):
		pass



	def hamiltonian(self, operator, matrix=None, qdata=None, processor=None, dataset=None, energy_function=None, file=None):
		if energy_function != None:
			self.energy_function = energy_function if energy_function!=None else self.energy_function;
			self.bqm = dbc.dimod.BinaryQuadraticModel().from_function(self.energy_function, quantumic.labels);
		if dataset != None:
			self.from_values(dataset);
		return operator;




	def save(self, database=None, name=None):
		if database == None:
			database = self.database
		return self.database.save(self, name=name);



	def fft(self, *args, **kwargs):
		pass



	def pow(self, *args, **kwargs):
		pass



	def exp(self, *args, **kwargs):
		pass



	def svd(self, *args, **kwargs):
		pass


	def min(self, *args, **kwargs):
		pass



	def max(self, *args, **kwargs):
		pass




	def pca(self, *args, **kwargs):
		pass




	def identity(self,n_qbits=None):
		"""
		Find Identity BQM
		"""
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np.identity(n_qbits))
		return self.processor.identity(n_qbits=n_qbits);




	def hammard(self, n_qbits=None):
		"""
		"""
		self.bqm = None
		return self



	def multiply(self, qa, qb):
		pass


	def divide(self, qa, qb):
		pass



	def qand(self, qa, qb):
		pass




	def qor(self, qa, qb, n_qbits=None):
		pass




	def cnot(self, qa, qb, n_qbits=None):
		pass






class CPUQProcessor(QProcessor):


	def __is_theano__(self, *args, **kwargs):
		pass



	def Identity(self, *args, **kwargs):
		if not self.__is_theano__(*args, **kwargs):
			return QOperator(np.identity(2), *args, **kwargs);
		else:
			return QOperator(T.identity(2), *args, **kwargs);





	def Hadamard(self, *args, **kwargs):
		if not self.__is_theano__(*args, **kwargs):
			return QOperator(1/math.sqrt(2) * np.matrix([[1, 1],[1, -1]]), *args, **kwargs);
		else:
			return QOperator(T.tensor(), *args, **kwargs);




	def PauliX(self, *args, **kwargs):
		return QOperator([[0, 1],[1, 0]], *args, **kwargs);




	def PauliY(self, *args, **kwargs):
		return QOperator([[0, complex(0, -1)],[complex(0, 1), 0]], *args, **kwargs);





	def PauliZ(self, *args, **kwargs):
		return QOperator([[1, 0], [0, -1]], *args, **kwargs);




	def Rot(self, theta, *args, **kwargs):
		return QOperator([[1, 0],[0, complex(math.cos(theta), complex(0, 1)*math.sin(theta))]], *args, **kwargs);




	def S(self, *args, **kwargs):
		return self.Rot(math.pi/2, *args, **kwargs);



	def T(self, *args, **kwargs):
		return self.Rot(math.pi/4, *args, **kwargs);





	def train(self, *args, **kwargs):
		return self.hamiltonian(args, kwargs);



	def fit(self, *args, **kwargs):
		return self.hamiltonian(args, kwargs);



	def eval(self, a):
		pass



	def hamiltonian(self, operator=None, model=None, eigenmatrix=None, metric_basis=None, dataset=None, eingenfunction=None, file=None):
		if operator != None:
			return operator;
		if model == None:
			pass
		else:
			return QOperator(model, metric_basis=metric_basis);



	def save(self, database=None, name=None):
		if database == None:
			database = self.database
		return self.database.save(self, name=name);



	def Fft(self, *args, **kwargs):
		pass



	def Pow(self, *args, **kwargs):
		pass



	def Exp(self, *args, **kwargs):
		pass



	def Svd(self, *args, **kwargs):
		pass




	def Pca(self, *args, **kwargs):
		pass



	def Toffoli(self, *args, **kwargs):
		pass



	def multiply(self, qa, qb):
		pass



	def divide(self, qa, qb):
		pass



	def Qand(self, qa, qb):
		pass




	def Qor(self, qa, qb, n_qbits=None):
		pass




	def CNot(self, qa, qb, n_qbits=None):
		pass






	def condense(self, qa):
		typer = type(qa);
		if typer == QData or typer == QTData:
			states = set([ qu.state for qu in qa.states]);
			return typer([(sum(qa[state]), state) for state in states])



	def unit_add(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if qa.state == qb.state :
				dtyper = QData if type(qa) == QUnit else QTData;
				if qb.state == None:
					return dtyper([typer(qa.amplitude + qb.amplitude, None)]);
				else:
					return dtyper([typer(qa.amplitude + qb.amplitude, *qb.state)]);
			else:
				return QData([qa, qb]) if typer == QUnit else QTData([qa, qb]);


	def operator_add(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes + qb.amplitudes, qb.states);



	def unit_sub(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if qa.state == qb.state :
				dtyper = QData if type(qa) == QUnit else QTData;
				return dtyper([typer(amplitude=(qa.amplitude - qb.amplitude), state=qb.state)]);
			else:
				qb.amplitude = - qb.amplitude;
				return QData([qa, qb]) if typer == QUnit else QTData([qa, qb]);



	def operator_sub(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes - qb.amplitudes, qb.states);



	def unit_mul(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if type(qa) == type(qb): 
				return typer(qa.amplitude*qb.amplitude, (qa.state, qb.state))
			elif type(qa) == QUnit and type(qb) == QTUnit:
				a = QUnit(1, qa.state); b = QUnit(1, qb.state);
				return QOperator([[qa.amplitude*qb.amplitude]], metrics=QOperatorMetrics([[(a,b)]]))
			elif type(qa) == QTUnit and type(qb) == QUnit:
				return qa.amplitude*qb.amplitude*qa.model.get_metric(qa.state, qb.state);
			elif (type(qa) != QTUnit and type(qa)) != QUnit and (type(qb) == QTUnit or type(qb) == QUnit):
				return type(qb)(qa*qb.amplitude, qb.state);
			elif (type(qb) != QTUnit and type(qb)) != QUnit and (type(qa) == QTUnit or type(qa) == QUnit):
				return type(qa)(qb*qa.amplitude, qa.state);



	def operator_mul(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes * qb.amplitudes, qb.states);



	def qmap_qunit_mul(self, qa, qb):
		return qa.transform(qb);



	def qtunit_qmap_mul(self, qa, qb):
		return qb.transform(qa);



	def qmap_qdata_mul(self, qa, qb):
		return qa.transform(qb);



	def qtdata_qmap_mul(self, qa, qb):
		return qb.transform(qa);



	def qoperator_qmap_mul(self, qa, qb):
		return qb.transform(qa);


	def qmap_qoperator_mul(self, qa, qb):
		return qa.transform(qb);





	def data_add(self, qa, qb):
		typer = type(qa)
		if typer == QData or typer ==QTData:
			if typer == type(qb):
				keys = qa.keys;
				keys.extend(qb.keys);
				keys = list(set(keys));
				return typer([type(qa[0])( sum([ s.amplitude for s in qa[key].states]) + sum([ w.amplitude for w in qb[key].states]),  *qa[key][0].state ) for key in keys ]);
			else:
				pass;



	def data_sub(self, qa, qb):
		typer = type(qa)
		if typer == QData or typer ==QTData:
			if typer == typer(qb):
				sub_typer = type(qa[0]);
				states = list(set(qa.states.concat(qb.states)));
				return typer([sub_typer(qa.amplitudes[qa.index(k)] - qa.amplitudes[qa.index(k)]) for k in states ]);
			else:
				raise Exception();


	def data_mul(self, qa, qb):
		if type(qa) == QData and type(qb) ==QTData:
			return self.data_outer_product(qa, qb);
		elif type(qa) == QTData and type(qb) ==QData:
			return self.data_inner_product(qa, qb);
		elif (type(qa) == QData and type(qb) ==QData) or (type(qa) == QTData and type(qb) == QTData) :
			return self.data_outer_product(qa, qb);
			


	def data_outer_product(self, qa, qb):
		return QOperator([[],[]],[[],[]])



	def data_inner_product(self, qa, qb):
		pass


	def data_tensor_product(self, qa, qb):
		return QData();


	def qdata_qunit_add(self, qa, qb):
		return qa + QData([qb]);



	def qtdata_qtunit_add(self, qa, qb):
		return qa + QTData([qb]); 







class DWaveQProcessor(QProcessor):



	def __init__(self, *args, **kwargs):
		if "mode" in kwargs:
			self.mode = kwargs.get("mode");
			if self.mode == DWAVE_MODE_TEST:
				self.solver = dbc.dimod.ExactSolver();
			elif self.mode == DWAVE_MODE_EXACT:
				self.solver = dbc.dimod.ExactSolver();
			elif self.mode == DWAVE_MODE_1000Q:
				self.solver = dbc.dimod.DWaveSampler();
			elif self.mode == DWAVE_MODE_2000Q:
				self.solver = dbc.dimod.DWaveSampler();
			else:
				self.solver = dbc.dimod.ExactSolver();
		else:
			self.solver = dbc.dimod.ExactSolver()



	def sample(self, *args, **kwargs):
		if type(args[0]) == QOperator:
			return self.sample_qoperators(args[0]);
		elif type(args[0]) == QData:
			return self.sample_qdata(args[0]);
		




	def sample_qoperators(self, *args, **kwargs):
		if args[0].bqm != 0:
			return QData(solver.sample_bqm(args[0].to_bqm()));
		if args[0].csp != 0:
			return QData(solver.sample_bqm(args[0].to_bqm()));
		elif args[0].ising != 0:
			return QData(solver.sample_ising(args[0].to_dict()));
		elif args[0].qubo != 0:
			return QData(solver.sample_qubo(args[0].to_dict()));
		else:
			return QData(solver.sample(args[0]));





	def sample_qdata(self, *args, **kwargs):
		pass





	def sample_qunit(self, *args, **kwargs):
		pass





	def train(self, *args, **kwargs):
		return self.hamiltonian(args, kwargs);



	def fit(self, *args, **kwargs):
		return self.hamiltonian(args, kwargs);



	def eval(self, operations):
		if type(operations) == QOperator:
			self.sample_bqm(operations);





	def hamiltonian(self, operator=None, model=None, eigenmatrix=None, metric_basis=None, dataset=None, eingenfunction=None, file=None):
		if operator != None:
			return operator;
		if model == None:
			pass
		else:
			return QOperator(model, metric_basis=metric_basis);



	def measure(self, ):
		return None;



	def save(self, database=None, name=None):
		if database == None:
			database = self.database
		return self.database.save(self, name=name);



	def fft(self, *args, **kwargs):
		np_identity_matrix = np.identity(n_qbits)
		bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator(bqm=bqm);





	def svd(self, *args, **kwargs):
		np_identity_matrix = np.identity(n_qbits)
		bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator(bqm=bqm);




	def pca(self, *args, **kwargs):
		np_identity_matrix = np.identity(n_qbits)
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator(bqm=bqm);




	def identity(self,n_qbits=None):
		np_identity_matrix = np.identity(n_qbits)
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator();




	def hammard(self, n_qbits=None):
		hammard_matrix = np.matrix([[], [], []]);
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(hammard_matrix);
		return QOperator();




	def multiply(self, qa, qb):
		np_identity_matrix = np.identity(n_qbits)
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator();




	def divide(self, qa, qb):
		np_identity_matrix = np.identity(n_qbits)
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator();




	def qand(self, qa, qb):
		np_identity_matrix = np.identity(n_qbits)
		self.bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator();




	def qor(self, qa, qb, n_qbits=None):
		np_identity_matrix = np.identity(n_qbits)
		bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator();




	def cnot(self, qa, qb, n_qbits=None):
		np_identity_matrix = np.identity(n_qbits)
		bqm = dbc.dimod.BinaryQuadraticModel().from_numpy_matrix(np_identity_matrix);
		return QOperator();



	def sampleset_to_qdata(self, sampleset):
		return QData([(x.energy, x.state) for x in sampleset]);



	def sampleset_to_qtdata(self, sampleset):
		return QTData([(x.energy, x.state) for x in sampleset]);




	def unit_add(self, qa, qb):
		if type(qa)== QUnit or type(qa) == QTUnit:
			if type(qa) == type(qb):
				h =  {(qa.key, qa.key):(qa.amplitude.conjugate()*qa.amplitude).real, (qb.key, qb.key):(qb.amplitude.conjugate()*qb.amplitude).real};
				J = {(qa.key, qb.key):(qa.amplitude.conjugate()*qb.amplitude + qb.amplitude.conjugate()*qa.amplitude).real};
				Q = dict(h); Q.update(J);
				if type(qa) == QUnit:
					return self.sampleset_to_qdata(self.solver.sample_qubo(Q));
				else:
					return self.sampleset_to_qtdata(self.solver.sample_qubo(Q))
		elif type(qa) == QData and type(qb) == QUnit:
			return self.data_add(qa, QData([qb]));
		elif type(qb) == QData and type(qa) == QUnit:
			return self.data_add(QData([qa]), qb)
		elif type(qa) == QTData and type(qb) == QTUnit:
			return self.data_add(qa, QTData([qb]));
		elif type(qb) == QTData and type(qa) == QTUnit:
			return self.data_add(QTData([qa]), qb);
				






	def operator_add(self, A, B):
		typer1 = type(A);
		typer2 = type(B);
		if typer1 == QOperator and typer2==QOperator:
			bqm = dbc.BinaryQuadraticModel();
			return QOperator(qa.amplitudes + qb.amplitudes, qb.states);







	def unit_sub(self, qa, qb):
		if type(qa)== QUnit or type(qa) == QTUnit:
			if type(qa) == type(qb):
				h =  {(qa.key, qa.key):(qa.amplitude.conjugate()*qa.amplitude).real, (qb.key, qb.key):(qb.amplitude.conjugate()*qb.amplitude).real};
				J = {(qa.key, qb.key):-(qa.amplitude.conjugate()*qb.amplitude + qb.amplitude.conjugate()*qa.amplitude).real};
				Q = dict(h); Q.update(J);
				if type(qa) == QUnit:
					return self.sampleset_to_qdata(self.solver.sample_qubo(Q));
				else:
					return self.sampleset_to_qtdata(self.solver.sample_qubo(Q))
		elif type(qa) == QData and type(qb) == QUnit:
			return self.data_sub(qa, QData([qb]));
		elif type(qb) == QData and type(qa) == QUnit:
			return self.data_sub(QData([qa]), qb)
		elif type(qa) == QTData and type(qb) == QTUnit:
			return self.data_sub(qa, QTData([qb]));
		elif type(qb) == QTData and type(qa) == QTUnit:
			return self.data_sub(QTData([qa]), qb);







	def operator_sub(self, A, B):
		typer1 = type(A);
		typer2 = type(B);
		if typer1 == QOperator and typer2==QOperator:
			bqm = dbc.BinaryQuadraticModel();
			return QOperator(qa.amplitudes + qb.amplitudes, qb.states);






	def unit_mul(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if type(qa) == type(qb): 
				return typer(qa.amplitude*qb.amplitude, (qa.state, qb.state))
			elif type(qa) == QUnit and type(qb) == QTUnit:
				a = QUnit(1, qa.state); b = QUnit(1, qb.state);
				return QOperator([[qa.amplitude*qb.amplitude]], metrics=QOperatorMetrics([[(a,b)]]))
			elif type(qa) == QTUnit and type(qb) == QUnit:
				return qa.amplitude*qb.amplitude*qa.model.get_metric(qa.state, qb.state);
			elif (type(qa) != QTUnit and type(qa)) != QUnit and (type(qb) == QTUnit or type(qb) == QUnit):
				return type(qb)(qa*qb.amplitude, qb.state);
			elif (type(qb) != QTUnit and type(qb)) != QUnit and (type(qa) == QTUnit or type(qa) == QUnit):
				return type(qa)(qb*qa.amplitude, qa.state);







	def operator_mul(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes * qb.amplitudes, qb.states);
		elif typer1 == QMap and typer2==QMap:
			return QMap(qa.amplitudes * qb.amplitudes, qb.states);
		elif typer1 == QOperator and typer2==QMap:
			return QOperator(qa.amplitudes * qb.amplitudes, qb.states);
		elif typer1 == QMap and typer2==QOperator:
			return QOperator(qa.amplitudes * qb.amplitudes, qb.states);
		elif typer1 == QOperator and typer2==QUnit:
			return QData();
		elif typer1 == QTUnit and typer2 == QOperator:
			return QTData();
		elif typer1 == QOperator and typer2==QData:
			return QData();
		elif typer1 == QTData and typer2 == QOperator:
			return QTData();





	def data_add(self, qa, qb):
		typer = type(qa)
		if typer == QData or typer ==QTData:
			Qa = qa.get_qubo();
			Qb = qb.get_qubo();
			quadratic = {(qa.keys[i], qb.keys[j]): qa.states[qa.keys[i]].amplitude.conjugate()*qb.states[qb.keys[j]].amplitude + qb.states[qb.keys[j]].amplitude.conjugate()*qa.states[qa.keys[i]].amplitude for i in range(len(qa.keys)) for j in range(len(qb.keys)) if i > j};
			Qab = dict(Qa); Qab.update(Qb); Qab.update(quadratic);
			return self.sampleset_to_qdata(self.solver.sample_qubo(Qab));






	def data_sub(self, qa, qb):
		typer = type(qa)
		if typer == QData or typer ==QTData:
			Qa = qa.get_qubo();
			Qb = qb.get_qubo();
			quadratic = {(qa.keys[i], qb.keys[j]): -(qa.states[qa.keys[i]].amplitude.conjugate()*qb.states[qb.keys[j]].amplitude + qb.states[qb.keys[j]].amplitude.conjugate()*qa.states[qa.keys[i]].amplitude) for i in range(len(qa.keys)) for j in range(len(qb.keys)) if i > j};
			Qab = dict(Qa); Qab.update(Qb); Qab.update(quadratic);
			return self.sampleset_to_qdata(self.solver.sample_qubo(Qab));





	def data_mul(self, qa, qb):
		if type(qa) == QData and type(qb) ==QTData:
			return self.data_outer_product(qa, qb);
		elif type(qa) == QTData and type(qb) ==QData:
			return self.data_inner_product(qa, qb);
		elif (type(qa) == QData and type(qb) ==QData) or (type(qa) == QTData and type(qb) == QTData) :
			return self.data_outer_product(qa, qb);
			


	def data_outer_product(self, qa, qb):
		return QOperator([[],[]],[[],[]])



	def data_inner_product(self, qa, qb):
		pass


	def data_tensor_product(self, qa, qb):
		return QData();







class IBMQProcessor(QProcessor):



	def UBase(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc._base, *args, **kwargs);



	def U0(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.u0, *args, **kwargs);




	def U1(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.u1, *args, **kwargs);




	def U2(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.u2, *args, **kwargs);




	def U3(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.u3, *args, **kwargs);




	def Identity(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.iden, *args, **kwargs);


	def Measure(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.measure, *args, **kwargs);




	def Hadamard(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.h, *args, **kwargs);




	def PauliX(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.x, *args, **kwargs);




	def PauliY(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.x, *args, **kwargs);





	def PauliZ(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.z, *args, **kwargs);




	def RotX(self, theta, *args, **kwargs):
		qc = QC();
		return QOperator(qc.rx, theta=theta, *args, **kwargs);




	def RotY(self, theta, *args, **kwargs):
		qc = QC();
		return QOperator(qc.ry, theta=theta, *args, **kwargs);




	def RotZ(self, theta, *args, **kwargs):
		qc = QC();
		return QOperator(qc.rz, theta=theta, *args, **kwargs);





	def RotZZ(self, theta, *args, **kwargs):
		qc = QC();
		return QOperator(qc.rzz, theta=theta, *args, **kwargs);





	def S(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.s, *args, **kwargs);




	def SDG(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.sdg, *args, **kwargs);




	def Swap(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.swap, *args, **kwargs);





	def T(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.t, *args, **kwargs);



	def TGD(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.tdg, *args, **kwargs);





	def train(self, *args, **kwargs):
		return self.hamiltonian(args, kwargs);



	def fit(self, *args, **kwargs):
		return self.hamiltonian(args, kwargs);



	def eval(self, a):
		pass



	def hamiltonian(self, operator=None, model=None, eigenmatrix=None, metric_basis=None, dataset=None, eingenfunction=None, file=None):
		if operator != None:
			return operator;
		if model == None:
			pass
		else:
			return QOperator(model, metric_basis=metric_basis);



	def save(self, database=None, name=None):
		if database == None:
			database = self.database
		return self.database.save(self, name=name);



	def Fft(self, *args, **kwargs):
		pass



	def Pow(self, *args, **kwargs):
		pass



	def Exp(self, *args, **kwargs):
		pass



	def Svd(self, *args, **kwargs):
		pass




	def Pca(self, *args, **kwargs):
		pass



	def Toffoli(self, *args, **kwargs):
		pass



	def multiply(self, qa, qb):
		pass



	def divide(self, qa, qb):
		pass



	def Qand(self, qa, qb):
		pass




	def Qor(self, qa, qb, n_qbits=None):
		pass




	def CNot(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.cnot, *args, **kwargs);


	def CX(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.cx,*args, **kwargs);


	def CY(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.cy, *args, **kwargs);



	def CZ(self, *args, **kwargs):
		qc = QC();
		return QOperator(qc.cz, *args, **kwargs);






	def condense(self, qa):
		typer = type(qa);
		if typer == QData or typer == QTData:
			states = set([ qu.state for qu in qa.states]);
			return typer([(sum(qa[state]), state) for state in states])



	def unit_add(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if qa.state == qb.state :
				dtyper = QData if type(qa) == QUnit else QTData;
				return dtyper([typer(qa.amplitude + qb.amplitude, *qb.state)]);
			else:
				return QData([qa, qb]) if typer == QUnit else QTData([qa, qb]);


	def operator_add(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes + qb.amplitudes, qb.states);



	def unit_sub(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if qa.state == qb.state :
				dtyper = QData if type(qa) == QUnit else QTData;
				return dtyper([typer(amplitude=(qa.amplitude - qb.amplitude), state=qb.state)]);
			else:
				qb.amplitude = - qb.amplitude;
				return QData([qa, qb]) if typer == QUnit else QTData([qa, qb]);



	def operator_sub(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes - qb.amplitudes, qb.states);



	def unit_mul(self, qa, qb):
		typer = type(qa)
		if typer == QUnit or typer ==QTUnit:
			if type(qa) == type(qb): 
				return typer(qa.amplitude*qb.amplitude, (qa.state, qb.state))
			elif type(qa) == QUnit and type(qb) == QTUnit:
				a = QUnit(1, qa.state); b = QUnit(1, qb.state);
				return QOperator([[qa.amplitude*qb.amplitude]], metrics=QOperatorMetrics([[(a,b)]]))
			elif type(qa) == QTUnit and type(qb) == QUnit:
				return qa.amplitude*qb.amplitude*qa.model.get_metric(qa.state, qb.state);
			elif (type(qa) != QTUnit and type(qa)) != QUnit and (type(qb) == QTUnit or type(qb) == QUnit):
				return type(qb)(qa*qb.amplitude, qb.state);
			elif (type(qb) != QTUnit and type(qb)) != QUnit and (type(qa) == QTUnit or type(qa) == QUnit):
				return type(qa)(qb*qa.amplitude, qa.state);



	def operator_mul(self, qa, qb):
		typer1 = type(qa);
		typer2 = type(qb);
		if typer1 == QOperator and typer2==QOperator:
			return QOperator(qa.amplitudes * qb.amplitudes, qb.states);



	def qmap_qunit_mul(self, qa, qb):
		return qa.transform(qb);



	def qtunit_qmap_mul(self, qa, qb):
		return qb.transform(qa);



	def qmap_qdata_mul(self, qa, qb):
		return qa.transform(qb);



	def qtdata_qmap_mul(self, qa, qb):
		return qb.transform(qa);



	def qoperator_qmap_mul(self, qa, qb):
		return qb.transform(qa);


	def qmap_qoperator_mul(self, qa, qb):
		return qa.transform(qb);





	def data_add(self, qa, qb):
		typer = type(qa)
		if typer == QData or typer ==QTData:
			if typer == type(qb):
				keys = qa.keys;
				keys.extend(qb.keys);
				keys = list(set(keys));
				return typer([type(qa[0])( sum([ s.amplitude for s in qa[key].states]) + sum([ w.amplitude for w in qb[key].states]),  *qa[key][0].state ) for key in keys ]);
			else:
				pass;



	def data_sub(self, qa, qb):
		typer = type(qa)
		if typer == QData or typer ==QTData:
			if typer == typer(qb):
				sub_typer = type(qa[0]);
				states = list(set(qa.states.concat(qb.states)));
				return typer([sub_typer(qa.amplitudes[qa.index(k)] - qa.amplitudes[qa.index(k)]) for k in states ]);
			else:
				raise Exception();


	def data_mul(self, qa, qb):
		if type(qa) == QData and type(qb) ==QTData:
			return self.data_outer_product(qa, qb);
		elif type(qa) == QTData and type(qb) ==QData:
			return self.data_inner_product(qa, qb);
		elif (type(qa) == QData and type(qb) ==QData) or (type(qa) == QTData and type(qb) == QTData) :
			return self.data_outer_product(qa, qb);
			


	def data_outer_product(self, qa, qb):
		return QOperator([[],[]],[[],[]])



	def data_inner_product(self, qa, qb):
		pass


	def data_tensor_product(self, qa, qb):
		return QData();


	def qdata_qunit_add(self, qa, qb):
		return qa + QData([qb]);



	def qtdata_qtunit_add(self, qa, qb):
		return qa + QTData([qb]); 











