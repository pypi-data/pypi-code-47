import sys;
sys.path.append("../lib");
from qmap import QMap, QBinStringMap, QSequenceMap;
from quantumics import QData, QUnit;
from qoperator import QOperator;
import unittest;







class QMapTest(unittest.TestCase):


	def test_qmap_constructor(self):
		mpx0 = ["hello", "hi", "whatever"];
		mpy0 = ["0", "1", "10"];
		MAP0 = QMap(mpx0, mpy0);
		mpx1 = ["hello", "hi", "whatever"];
		mpy1 = lambda k: bin(k)[2:]; 
		MAP1 = QMap(mpx1, mpy1);
		mpx2 = {"hello":"0", "hi":"1", "whatever":"10"};
		MAP2 = QMap(mpx2);
		mpx3 = ["hello", "hi", "whatever"];
		MAP3 = QMap(mpx3);
		MAP4 = QBMap();

		self.assertIsInstance(MAP0, QMap);
		self.assertIsInstance(MAP1, QMap);
		self.assertIsInstance(MAP2, QMap);
		self.assertIsInstance(MAP3, QMap);
		self.assertIsInstance(MAP4, QMap);



	def test_qmap_equal(self):
		mpx0 = ["hello", "hi", "whatever"];
		mpy0 = ["0", "1", "10"];
		MAP0 = QMap(mpx0, mpy0);
		mpx1 = ["hello", "hi", "whatever"];
		mpy1 = lambda k: bin(k)[2:]; 
		MAP1 = QMap(mpx1, mpy1);
		mpx2 = {"hello":"0", "hi":"1", "whatever":"10"};
		MAP2 = QMap(mpx2);
		mpx3 = ["hello", "hi", "whatever"];
		MAP3 = QMap(mpx3);

		self.assertEqual(MAP0, MAP1);
		self.assertEqual(MAP1, MAP2);
		self.assertEqual(MAP2, MAP3);
		self.assertEqual(MAP3, MAP0);




	def test_qmap_transformation(self):
		MAP  = QMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP()*x);




	def test_qmap_condensed_transformation(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.c()()*x);




	def test_qmap_unit_transformation(self):
		MAP = QMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.u()()*x);




	def test_qmap_transpose(self):
		MAP  = QMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.t()()*x);




	def test_qmap_condensed_transpose(self):
		MAP = QMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.ct()()*x);




	def test_qmap_unit_transpose(self):
		MAP = QMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.ut()()*x);




	def test_qmap_transposed_condense(self):
		MAP = QMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.tc()()*x);




	def test_qmap_transposed_unit(self):
		MAP = QMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.tu()()*x);







class QSequenceMapTest(unittest.TestCase):



	def test_qsequencemap_constructor(self):
		MAP = QSequenceMap();
		self.assertIsInstance(MAP, QBinStringMap);



	def test_qsequencemap_transformation(self):
		MAP  = QSequenceMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP()*x);



	def test_qsequencemap_condensed_transformation(self):
		MAP = QSequenceMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.c()()*x);



	def test_qsequencemap_unit_transformation(self):
		MAP = QSequenceMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.u()()*x);



	def test_qsequencemap_transpose(self):
		MAP  = QSequenceMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.t()()*x);



	def test_qsequencemap_condensed_transpose(self):
		MAP = QSequenceMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.ct()()*x);



	def test_qsequencemap_unit_transpose(self):
		MAP = QSequenceMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.ut()()*x);




	def test_qsequencemap_transposed_condense(self):
		MAP = QSequenceMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.tc()()*x);



	def test_qsequencemap_transposed_unit(self):
		MAP = QSequenceMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.tu()()*x);







class QBinStringMapTest(unittest.TestCase):



	def test_qbinstringmap_constructor(self):
		MAP = QBinStringMap();
		self.assertIsInstance(MAP, QBinStringMap);


	def test_qbinstringmap_transformation(self):
		pass




	def test_qbinstringmap_transformation(self):
		MAP  = QBinStringMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP()*x);



	def test_qbinstringmap_condensed_transformation(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.c()()*x);



	def test_qbinstringmap_unit_transformation(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.u()()*x);



	def test_qbinstringmap_transpose(self):
		MAP  = QBinStringMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.t()()*x);



	def test_qbinstringmap_condensed_transpose(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.ct()()*x);



	def test_qbinstringmap_unit_transpose(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.ut()()*x);




	def test_qbinstringmap_transposed_condense(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QData();
		self.assertEqual(y, MAP.tc()()*x);



	def test_qbinstringmap_transposed_unit(self):
		MAP = QBinStringMap();
		x = QUnit();
		y = QUnit();
		self.assertEqual(y, MAP.tu()()*x);





if "__main__" == __name__:
	x = QData([(4, "hello"), (4, "whatever")]);
	y = QUnit(1, "quantum")
	z = x[0];
	MAP = QBinStringMap();
	print(x);
	print(MAP);
	mx= MAP*x;
	mz = MAP*z
	my = MAP*y
	mtx = MAP.t()*mx;
	mty = MAP.t()*my;
	mtz = MAP.t()*mz;


	print(x);
	print(mx);
	print(mtx);
	print(z);
	print(mz);
	print(mtz);
	print(y);
	print(my);
	print(mty);


