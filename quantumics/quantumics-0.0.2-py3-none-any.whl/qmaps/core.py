import binascii;
from ..core import QUnit, QData, QTUnit, QTData;
from ..qoperators import QOperator;





class QMap(QOperator):


	def __init__(self, *args, **kwargs):
		if len(args) == 1 and type(args[0]) == list:
			super(QMap, self).__init__({ args[0][k]: bin(k)[2:]  for k in range(len(args[0]))})
		elif len(args) == 2 and type(args[0]) == list and type(args[1]) == list and len(args[0]) == len(args[1]):
			super(QMap, self).__init__({args[0][i]: args[1][i] for i in range(len(args[0]))});
		elif len(args) == 2 and type(args[0]) and callable(args[1]):
			super(QMap, self).__init__({ args[0][k]: args[1](k)  for k in range(len(args[0]))})
		elif len(args) == 1 and type(args[0]) == dict:
			super(QMap, self).__init__(args[0]);
		QOperator.__init__(self, *args, **kwargs);


	def __call__(self, *args, **kwargs):
		return self;



	def __mul__(self, a):
		return self.model.processor.__mul__(self, a);


	def __div__(self, a):
		return self.model.processor.__div__(self, a);


	def __add__(self, a):
		return self.model.processor.__add__(self, a);


	def __eq__(self, a):
		return self.model.processor.__eq__(self, a);


	def __sub__(self, a):
		return self.model.processor.__sub__(self, a);



	def transpose(self):
		return QMap({self.get(key):key for key in self.keys()})



	def t(self):
		return self.transpose();



	def transform(self):
		pass






class QSequenceMap(QMap):


	def __new__(self, *args, length=2):
		self.length = 2;
		return QMap.__new__(self, *args);


	def transponse(self):
		pass



	def transform(self):
		pass







class QBinStringMap(QMap):


	def __new__(self, *args, **kwargs):
		return QMap.__new__(self, *args, **kwargs);


	def __init__(self, *args, **kwargs):
		self.right_states = ["a", "b", "c",];
		self.left_states = [self.object_to_bitstate(x) for x in self.right_states];
		self.forward_transformation = True;
		QMap.__init__(self, *args, **kwargs);



	def __get__(self, key):
		return self.text_to_bits(str(key));

	def __call__(self, *args, **kwargs):
		return self;

	def transpose(self):
		qmap_transpose = QBinStringMap();
		qmap_transpose.forward_transformation = False;
		return qmap_transpose;




	def transform(self, obj):
		if self.forward_transformation == True:
			return self.object_to_bitstate(obj);
		else:
			return self.bits_to_objectstate(obj);





	def object_to_bits(self, obj):
		to_bits = lambda obj: [value[2:] for value in map(bin,bytearray(str(obj),'utf8'))];
		return to_bits(obj);





	def object_to_bitstate(self, obj):
		if type(obj) == QUnit:
			return QData([(obj.amplitude, x) for x in self.object_to_bits(obj.state)]);
		elif type(obj) == QTUnit:
			return QTData([(obj.amplitude, x) for x in self.object_to_bits(obj.state)]);
		elif type(obj) == QData:
			return QData([ (qunit.amplitude, x) for qunit in obj.states for x in self.object_to_bits(qunit.state) ]);
		elif type(obj) == QTData:
			return QTData([ (qtunit.amplitude, x) for x in self.object_to_bits(qtunit.state) for qtunit in obj.states ]);
		else:
			return QData([(1, x) for x in self.object_to_bits(obj)]);




	def bits_to_object(self, bits, encoding='utf-8', errors='surrogatepass'):
		w = ""
		if bits == list:
			for bit in bits:
				w = w + bit;
			bits = w;
		n = int(bits, 2)
		objstr = self.int2bytes(n).decode(encoding, errors);
		try:
			return eval(objstr);
		except Exception as e:
			return objstr;






	def bits_to_objectstate(self, bits):
	    if type(bits) == QUnit:
	    	return QData([(bits.amplitude, self.bits_to_object(bits.state))]);
	    elif type(bits) == QTUnit:
	    	return QTData([(bits.amplitude, self.bits_to_object(bits.state))]);
	    elif type(bits) == QData:
	    	return QData([ (qunit.amplitude, self.bits_to_object(qunit.state)) for qunit in bits.states ]);
	    elif type(bits) == QTData:
	    	return QTData([ (qtunit.amplitude, self.bits_to_object(qtunit.state)) for qtunit in bits.states ]);
	    else:
	    	return QData([(1, self.bits_to_object(bits))]);





	def int2bytes(self, i):
	    hex_string = '%x' % i
	    n = len(hex_string)
	    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))





