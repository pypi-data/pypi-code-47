import math;
from quantumics import QUnit, QTUnit;


class Space(QUnit):

	def __init__(self, qvalue):
		self.qvalue = qvalue


class State(QUnit):

	def __init__(self, qvalue):
		self.qvalue = qvalue




class PSpace(Space):

	def __repr__(self):
		qclass = type(self.qvalue)
		if  qclass == QUnit or qclass == QTUnit:
			return qclass([self.qvalue.types[i](self.qvalue.values[i]) for i in range(len(self.qvalue.values))]).__repr__();





class HPSpace(Space):

	def __repr__(self):
		qclass = type(self.qvalue)
		if  qclass == QUnit or qclass == QTUnit:
			return qclass([self.qvalue.types[i](self.qvalue.values[i]) for i  in range(2,len(self.qvalue.values)) ]).__repr__();






class BSpace(Space):

	def __repr__(self):
		qclass = type(self.qvalue)
		if  qclass == QUnit or qclass == QTUnit:
			return qclass([str(math.ceil(math.log2(self.qvalue.processor.maxs[i]))-len(bin(self.qvalue.values[i])[2:]))+bin(self.qvalue.values[i])[2:] for i in range(len(self.qvalue.values))]).__repr__();




class HBSpace(Space):

	def __repr__(self):
		qclass = type(self.qvalue)
		if  qclass == QUnit or qclass == QTUnit:
			return qclass([str(math.ceil(math.log2(self.qvalue.processor.maxs[i]))-len(bin(self.qvalue.values[i])[2:]))+bin(self.qvalue.values[i])[2:] for i in range(2, len(self.qvalue.values))]).__repr__();





class GSpace(Space):

	def __repr__(self):
		pass





class PState(State):


	def __repr__(self):
		pstate_value = str(tuple(self.values))
		if type(self.values) == QUnit:
			return "|"+pstate_value+">";
		if type(self.values) == QTUnit:
			return "<"+pstate_value+"|";



class BState(State):


	def __repr__(self):
		bstate_value = self.values.to_bin()
		if type(self.values) == QUnit:
			return "|"+bstate_value+">";
		if type(self.values) == QTUnit:
			return "<"+bstate_value+"|";




class GState(State):

	def __init__(self):
		pass