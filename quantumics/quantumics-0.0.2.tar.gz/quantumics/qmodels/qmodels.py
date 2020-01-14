from processors import CPUQProcessor
from qserver import QServer
from qdatabase import QDatabase
from qhilbertspace import QHilbertspace;


class QMetric(dict):

	def __init__(self, value):
		dict.__init__(self, value);




class QModel():


	def __init__(self, processor=CPUQProcessor(), metric=QMetric({}), server=QServer(), database=QDatabase(), hilbertspace=QHilbertspace()):
		self.processor = processor;
		self.metric = metric
		self.server = server;
		self.database = database;
		self.hilbertspace = hilbertspace;


	def get_metric(self, qa_state, qb_state):
		if self.metric.keys().__len__() == 0:
			if qa_state == qb_state:
				return 1;
			else :
				return 0;
		else:
			return self.metric[qa_state][qb_state];



	def get_processor(self):
		return self.processor;


	def get_server(self):
		return self.server;



	def get_database(self):
		return self.database;


	def get_hilbertspace(self):
		return self.hilbertspace;


	def set_processor(self, processor):
		self.processor =  processor;


	def set_metric(self, metric):
		self.metric = metric;


	def set_server(self, server):
		self.server = server;


	def set_database(self, database):
		self.database = database;


	def set_hilbertspace(self, hilbertspace):
		self.hilbertspace = hilbertspace;


