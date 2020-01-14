import unittest;
import sys;
sys.path.append("../pylib");
from qmap import QBinStringMap;
from operators import MEASURE, MIN, MAX, SUM, A, At, EXP, LOG, POW, FFT, SVD, PCA, SIGMOID, LOGIT;
from operators import GRAD, HESSIAN, I, H, PauliX, PauliY, PauliZ, R, Z, S, CNOT, TOFFOLI, SWAP, AND, OR;




class OperatorsTest(unittest.TestCase):


	def test_operator_MEASURE(self):
		MEASURE = MEASURE();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MEASURE*MAP*x;



	def test_operator_MIN(self):
		MIN = MIN();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MEASURE*MAP*x;



	def test_operator_MAX(self):
		MAX = MAX();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MAX*MAP*x;




	def test_operator_SUM(self):
		SUM = SUM();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = SUM*MAP*x;



	def test_operator_A(self):
		A = A();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = A*MAP*x;


	def test_operator_At(self):
		At = At();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = At*MAP*x;



	def test_operator_EXP(self):
		EXP = EXP();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = EXP*MAP*x;



	def test_operator_LOG(self):
		LOG = LOG();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MEASURE*MAP*x;



	def test_operator_POW(self):
		POW = POW();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MEASURE*MAP*x;



	def test_operator_FFT(self):
		FFT = FFT();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MEASURE*MAP*x;



	def test_operator_SVD(self):
		SVD = SVD();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = MEASURE*MAP*x;



	def test_operator_PCA(self):
		PCA = PCA();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = PCA*MAP*x;



	def test_operator_SIGMOID(self):
		SIGMOID = SIGMOID();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = SIGMOID*MAP*x;



	def test_operator_LOGIT(self):
		LOGIT = LOGIT();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = LOGIT*MAP*x;



	def test_operator_GRAD(self):
		GRAD = GRAD();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = GRAD*MAP*x;




	def test_operator_HESSIAN(self):
		HESSIAN = HESSIAN();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = HESSIAN*MAP*x;



	def test_operator_I(self):
		I = I();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = I*MAP*x;



	def test_operator_H(self):
		H = H();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = H*MAP*x;



	def test_operator_R(self):
		R = R(math.pi/4);
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = R*MAP*x;



	def test_operator_Z(self):
		Z = Z();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = Z*MAP*x;



	def test_operator_PauliX(self):
		PauliX = PauliX();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = PauliX*MAP*x;



	def test_operator_PauliY(self):
		PauliY = PauliY();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = PauliY*MAP*x;



	def test_operator_PauliZ(self):
		PauliZ = PauliZ();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = PauliZ*MAP*x;



	def test_operator_S(self):
		S = S();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = S*MAP*x;




	def test_operator_CNOT(self):
		CNOT = CNOT()
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = CNOT*MAP*x;




	def test_operator_TOFFOLI(self):
		TOFFOLI = TOFFOLI();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = TOFFOLI*MAP*x;





	def test_operator_SWAP(self):
		SWAP = SWAP();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = SWAP*MAP*x;





	def test_operator_AND(self):
		AND = AND();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = AND*MAP*x;




	def test_operator_OR(self):
		OR = OR();
		MAP = QBinStringMap();
		x = QUnit(3, "hello");
		y = OR*MAP*x;