import sys;
import unittest;
sys.path.append("../pylib/");
from quantumics import QData, QTUnit, QData;
from qoperator import QOperator


class QDataTest(unittest.TestCase):
	


	def test_qtdata_constructor(self):

		#Test Data Declaration
		x0 = (3, "Hello"); y0 = QData(3, "Hello")
		x1 = (2, 5); y1 = QData(2, 5);
		x2 = (3, (4, 4)); y2 = QData(3, (4, 4))
		x3 = (2, (5, 4, 2)); y3 = QData(2, (5, 4, 2));
		x4 = (complex(2, 5), ((4, 2), 3)); y4 = QData(complex(2, 5), ((4, 2), 3));
		x5 = (2, ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));
		y5 = QData(2, ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));

		print("Checking QTData Constructor");

		#Checking
		self.assertEqual(QData(*x0), y0, "Should be equal")
		self.assertEqual(QData(*x1), y1, "Should be equal")
		self.assertEqual(QData(*x2), y2, "Should be equal")
		self.assertEqual(QData(*x3), y3, "Should be equal")
		self.assertEqual(QData(*x4), y4, "Should be equal")
		self.assertEqual(QData(*x5), y5, "Should be equal")



	def test_qtdata_transpose(self):

		#Test Data Declaration
		x0 = QData(3, "Hello"); y0 = QTData(3, "Hello")
		x1 = QData(complex(2, 4), 5); y1 = QTData(complex(2, -4), 5);
		x2 = QData(complex(3, 3), (4, 4)); y2 = QTData(complex(3, -3), (4, 4))
		x3 = QData(2, (5, 4, 2)); y3 = QTData(2, (5, 4, 2));
		x4 = QData(complex(2, 5), (5, (4, 2), 3)); y4 = QTData(complex(2, -5), (5, (4, 2), 3));
		x5 = QData(complex(4, 7), ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));
		y5 = QTData(complex(4, -7), ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}))

		print("Checking QTData Transpose")

		#Checking
		self.assertEqual(x0.t(), y0)
		self.assertEqual(x1.t(), y1)
		self.assertEqual(x2.t(), y2)
		self.assertEqual(x3.t(), y3)
		self.assertEqual(x4.t(), y4)
		self.assertEqual(x5.t(), y5)



	def test_qtdata_add(self):
		
		#Test Data Declaration
		x0 = QData(complex(3)); y0 = QData(complex(3)); z0 = QData([QData(*(complex(6), None,))]);
		x1 = QData(complex(2), 5); y1 = QData(complex(2), 2); z1 = QData([QData(complex(2), 5), QData(complex(2), 2)]); 
		x2 = QData(complex(3), (4, 4)); y2 = QData(complex(3), (4, 4)); z2 = QData([QData(complex(6), (4, 4))])
		x3 = QData(complex(2), (5, 4, 2)); y3 = QData(complex(2), (5, 4, 1)); 
		z3 = QData([QData(complex(2), (5, 4, 2)), QData(complex(2), (5, 4, 1))]);
		x4 = QData(complex(2), (5, 4, 2, 3)); y4 = QData(complex(2, 6), (5, 4, 2, 3));
		z4 = QData([QData(complex(4, 6), (5, 4, 2, 3))]);
		x5 = QData(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QData(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QData([QData(complex(4, 8), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}))]);
		x6 = QData(complex(1), 5); y6 = QData(complex(3),5); z6 = QData([QData(complex(4),5)]);
		x7 = QData(complex(1), 3); y7 = QData(complex(3),5); z7 = QData([QData(complex(1),3), QData(complex(3),5)]);

		print("Checking QTData Addition")

		#Checking 
		self.assertEqual(x0+y0, z0)
		self.assertEqual(x1+y1, z1)
		self.assertEqual(x2+y2, z2)
		self.assertEqual(x3+y3, z3)
		self.assertEqual(x4+y4, z4)
		self.assertEqual(x5+y5, z5)
		self.assertEqual(x6+y6, z6)
		self.assertEqual(x7+y7, z7)



	def test_qtdata_sub(self):
		#Test Data Declaration
		x0 = QData(complex(3),); y0 = QData(complex(3),); z0 = QData([QData(0,)]);
		x1 = QData(complex(2), 5); y1 = QData(complex(2), 2); z1 = QData([QData(complex(2), 5), QData(complex(-2), 2)]); 
		x2 = QData(complex(3), (4, 4)); y2 = QData(complex(3), (4, 4)); z2 = QData([QData(0, (4, 4))])
		x3 = QData(complex(2), (5, 4, 2)); y3 = QData(complex(2), (5, 4, 1)); 
		z3 = QData([QData(complex(2), (5, 4, 2)), QData(complex(-2), (5, 4, 1))]);
		x4 = QData(complex(2), (5, 4, 2, 3)); y4 = QData(complex(2, 6), (5, 4, 2, 3));
		z4 = QData([QData(complex(0, -6), (5, 4, 2, 3))]);
		x5 = QData(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QData(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QData([QData(complex(0, -2), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}))]);
		x6 = QData(complex(1), 5); y6 = QData(complex(3),5); z6 = QData([QData(complex(-2),5)]);
		x7 = QData(complex(1), 3); y7 = QData(complex(3),5); z7 = QData([QData(complex(1),3), QData(complex(-3),5)]);

		print("Checking QTData Subtraction")		

		#Checking 
		self.assertEqual(x0-y0, z0)
		self.assertEqual(x1-y1, z1)
		self.assertEqual(x2-y2, z2)
		self.assertEqual(x3-y3, z3)
		self.assertEqual(x4-y4, z4)
		self.assertEqual(x5-y5, z5)
		self.assertEqual(x6-y6, z6)
		self.assertEqual(x7-y7, z7)



	def test_qtdata_outer_product(self):

		#Test Data Declaration
		x0 = QData(complex(3), "Hello"); y0 = QTUnit(complex(3), "Hi"); z0 = QOperator(complex(9), "Hello", "Hi")
		x1 = QData(complex(2), 5); y1 = QTUnit(complex(2), 2); z1 = QOperator(complex(4), 5, 2)
		x2 = QData(complex(3), (4, 4)); y2 = QTUnit(3, (4, 4)); z2 = QOperator(complex(9), (4,4), (4,4))
		x3 = QData(complex(2), (5, 4, 2)); y3 = QTUnit(complex(2), (5, 4, 1)); 
		z3 = QOperator(complex(6), (5, 4, 2), (5, 4, 1));
		x4 = QData(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = QOperator(complex(2, 12), (5, 4, 2, 3), (5, 4, 2, 3))
		x5 = QData(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex((2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
		z5 = QOperator(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), 
			(4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		x6 = QData(complex(1),5); y6 = QTUnit(complex(3),5); z6 = QOperator(complex(3), 5, 5)
		x7 = QData(complex(1),3); y7 = QTUnit(complex(3),5); z7 = QOperator(complex(3), 3, 5)

		
		print("Checking QTData Outer Product")


		#Checking 
		self.assertEqual(x0*y0, z0)
		self.assertEqual(x1*y1, z1)
		self.assertEqual(x2*y2, z2)
		self.assertEqual(x3*y3, z3)
		self.assertEqual(x4*y4, z4)
		self.assertEqual(x5*y5, z5)
		self.assertEqual(x6*y6, z6)
		self.assertEqual(x7*y7, z7)



	def test_qtdata_inner_product(self):
		#Test Data Declaration
		x0 = QTUnit(complex(3), "Hello"); y0 = QData(complex(3), "Hello"); z0 = complex(9)
		x1 = QTUnit(complex(2), 5); y1 = QData(complex(2), 2); z1 = 0; 
		x2 = QTUnit(complex(3), (4, 4)); y2 = QData(complex(3), (4, 4)); z2 = 9;
		x3 = QTUnit(complex(2), (5, 4, 2)); y3 = QData(complex(2), (5, 4, 1)); z3 = 0;
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QData(complex(2, 6), (5, 4, 2, 3));
		z4 = complex(4, 12)
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QData(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = complex(-11, 16)
		x6 = QTUnit(complex(1), 5); y6 = QData(3,5); z6 = complex(3)
		x7 = QTUnit(complex(1), 3); y7 = QData(3,5); z7 = complex(0)


		print("Checking QTData Inner Product")

		#Checking
		self.assertEqual(x0*y0, z0)
		self.assertEqual(x1*y1, z1)
		self.assertEqual(x2*y2, z2)
		self.assertEqual(x3*y3, z3)
		self.assertEqual(x4*y4, z4)
		self.assertEqual(x5*y5, z5)
		self.assertEqual(x6*y6, z6)
		self.assertEqual(x7*y7, z7)



	def test_qtdata_tensor_product(self):
		#Test Data Declaration
		x0 = QData(3, "Hello"); y0 = QData(3,"Hi"); z0 = QData(complex(3), ("Hello", "Hi"))
		x1 = QData(2, 5); y1 = QData(2, 2); z1 = QData(complex(4), (5, 2)); 
		x2 = QData(3, (4, 4)); y2 = QData(3, (4, 4)); z2 = QData(complex(9), ((4,4), (4,4)));
		x3 = QData(2, (5, 4, 2)); y3 = QData(2, (5, 4, 1)); 
		z3 = QData(complex(4), ((5,4,2), (5,4,1)));
		x4 = QData(complex(2), (5, 4, 2, 3)); y4 = QData(complex(2, 6), (5, 4, 2, 3));
		z4 = QData([QData((complex(4, 12), (5, 4, 2, 3), (5, 4, 2, 3)))]);
		x5 = QData(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QData(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QData(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		x6 = QData(complex(1), 5); y6 = QData(complex(3), 5); z6 = QData(complex(3), (5, 5));
		x7 = QData(complex(1), 3); y7 = QData(complex(3), 5); z7 = QData(complex(3), (3, 5));

		print("Checking QTData Tensor Product")

		#Checking
		self.assertEqual(x0*y0, z0)
		self.assertEqual(x1*y1, z1)
		self.assertEqual(x2*y2, z2)
		self.assertEqual(x3*y3, z3)
		self.assertEqual(x4*y4, z4)
		self.assertEqual(x5*y5, z5)
		self.assertEqual(x6*y6, z6)
		self.assertEqual(x7*y7, z7)




	def test_qtdata_split(self):
		#Test Data Declaration
		x0 = QData(3, "Hello"); y0 = QData(3, "Hi"); z0 = QData(complex(9), ("Hello","Hi"))
		x1 = QData(2, 5); y1 = QData(2, 2); z1 = QData(complex(4), (5, 2)); 
		x2 = QData(3, (4, 4)); y2 = QData(3, (4, 4)); z2 = QData(complex(9), ((4,4), (4,4)));
		x3 = QData(2, (5, 4, 2)); y3 = QData(2, (5, 4, 1)); 
		z3 = QData(complex(4), ((5,4,2), (5,4,1)));
		x4 = QData(complex(2), (5, 4, 2, 3)); y4 = QData(complex(2, 6), (5, 4, 2, 3));
		z4 = QData([QData(complex(4, 12), (5, 4, 2, 3), (5, 4, 2, 3))]);
		x5 = QData(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QData(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QData(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		x6 = QData(complex(1), 5); y6 = QData((complex(3), 5)); z6 = QData(complex(3), (5, 5));
		x7 = QData(complex(1), 3); y7 = QData((complex(3), 5)); z7 = QData(complex(3), (3, 5));

		print("Checking QTData Split")

		#Checking
		self.assertEqual((x0, y0), z0.split((1, 1)))
		self.assertEqual((x1, y1), z1.split((1, 1)))
		self.assertEqual((x2, y2), z2.split((1, 1)))
		self.assertEqual((x3, y3), z3.split((1,  1)))
		self.assertEqual((x4, y4), z4.split((2, complex(2, 6))))
		self.assertEqual((x5, y5), z5.split((complex(2, 3), complex(2, 5))))
		self.assertEqual((x6, y6), z6.split((1, 3)))
		self.assertEqual((x7, y7), z7.split((1, 3)))





if __name__ == "__main__":
	unittest.main();




