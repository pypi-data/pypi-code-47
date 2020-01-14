import numpy as np;



class QMetric():

	def __init__(self, a, b):
		self.right_ket=a;
		self.left_ket=b;


	def __repr__(self):
		return "|"+str(self.right_ket)+"><"+str(self.left_ket)+"|";








class QOperatorMetrics(np.matrix):

	def __new__(self, *args, **kwargs):
		self.left_states = kwargs.get("left_states") if "left_states" in kwargs else [];
		self.right_states = kwargs.get("right_states") if "right_states" in kwargs else [];
		self.shape = (len(self.left_states), len(self.right_states));
		return np.matrix.__new__(self, *args) if len(args) != 0 else np.matrix.__new__(self, np.identity(self.shape[0] if self.shape[0] > self.shape[1] else self.shape[1]));


	def __init__(self, *args, left_states=None, right_states=None, inner_products=None, dataset=None, model=None, path_function=None, energy_function=None, optimizer=None, jacobian=None):
		if args != None or len(args)  != 0:
			self.scalar_product = inner_products if inner_products != None else energy_function if energy_function != None else jacobian;
		else:
			self.scalar_product = np.asmatrix(args[0])




	def __repr__(self):
		return super(QOperatorMetrics, self).__repr__()+ str([QMetric(self.left_states[i], self.right_states[k]) for i in range(self.shape[0]) for k in range(self.shape[1]) if i + k < 5]);










class QOperator(QOperatorMetrics):


	def __new__(self, *args, **kwargs):
		if "model" in kwargs:
			self.model = kwargs.get("model");
		else:
			from qmodel import QModel;
			self.model = QModel();
		return QOperatorMetrics.__new__(self, *args, **kwargs);


	def __init__(self, *args, **kwargs):
		QOperatorMetrics.__init__(self, *args, **kwargs);
		if args != None and len(args) != 0:
			if (type(args[0]) == list or type(args[0]) == np.ndarray):
				self.phases = np.asmatrix(args[0]);


	def __call__(self, *args, **kwargs):
		return QOperator(self.tolist(), left_states=self.left_states, right_states=self.right_states);



	def get_model(self,):
		return self.model;


	def get_path_function(self):
		return self.path_function;


	def get_optimizer(self):
		return self.optimizer;



	def set_model(self, model):
		self.model = model;




	def index(self, key):
		pass



	def __eq__(self, qb):
		return self.model.processor.__eq__(self, qb)



	def __sub__(self, qb):
		return self.model.processor.__sub__(self, qb);



	def __add__(self, qb):
		return self.model.processor.__add__(self, qb);



	def __mul__(self, a):
		return self.model.processor.__mul__(self, a);


	def transform(self, a):
		pass




	def get_linear(self):
		return np.asarray([self.value[i,i] for i in range(len(self.value))]);




	def get_quadratic(self):
		return np.asarray([[self.phases[i, j] for i in range(len(self.phases))  if i > j] for j in range(len(self.phases))])




	def save(self, database=None, name=None):
		if database == None:
			database = self.database;
		return database.save(self, name=name);




	def identity(self, *args, **kwargs):
		return self.model.processor.identity(*args, **kwargs);




	def hammard(self, *args, **kwargs):
		return self.model.processor.hammard(*args, **kwargs);




	def fft(self, *args, **kwargs):
		return self.model.processor.fft(*args, **kwargs);




	def svd(self, *args, **kwargs):
		return self.model.processor.svd(*args, **kwargs);




	def pca(self, *args, **kwargs):
		return self.model.processor.pca(*args, **kwargs);




	def exp(self, *args, **kwargs):
		return self.model.processor.exp(*args, **kwargs);




	def pow(self, *args, **kwargs):
		return self.model.processor.pow(*args, **kwargs);




	def hamiltonian(self, *args, **kwargs):
		return self.model.processor.hamiltonian(*args, **kwargs);




	def train(self, *args, **kwargs):
		return self.model.processor.hamiltonian(*args, **kwargs);




	def multiply(self, *args, **kwargs):
		return self.model.processor.multiplier(*args, **kwargs);




	def divide(self, *args, **kwargs):
		return self.model.processor.divide(**args, **kwargs);




	def qand(self, *args, **kwargs):
		return self.model.processor.qand(*args, **kwargs);




	def qor(self, *args, **kwargs):
		return self.model.processor.qor(*args, **kwargs);




	def cnot(self, *args, **kwargs):
		return self.model.processor.cnot(*args, **kwargs);






