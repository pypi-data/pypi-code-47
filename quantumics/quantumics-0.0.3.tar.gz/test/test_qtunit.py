import sys;
import unittest;
sys.path.append("../pylib/");
from quantumics import QTUnit, QUnit, QTData;
from qoperator import QOperator


class QTUnitTest(unittest.TestCase):
	


	def test_qtunit_constructor(self):

		#Test Data Declaration
		x0 = (3, "Hello"); y0 = QTUnit(3, "Hello")
		x1 = (2, 5); y1 = QTUnit(2, 5);
		x2 = (3, (4, 4)); y2 = QTUnit(3, (4, 4))
		x3 = (2, (5, 4, 2)); y3 = QTUnit(2, (5, 4, 2));
		x4 = (complex(2, 5), ((4, 2), 3)); y4 = QTUnit(complex(2, 5), ((4, 2), 3));
		x5 = (2, ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(2, ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));

		print("Checking QTUnit Constructor");

		#Checking
		self.assertEqual(QTUnit(*x0), y0, "Should be equal")
		self.assertEqual(QTUnit(*x1), y1, "Should be equal")
		self.assertEqual(QTUnit(*x2), y2, "Should be equal")
		self.assertEqual(QTUnit(*x3), y3, "Should be equal")
		self.assertEqual(QTUnit(*x4), y4, "Should be equal")
		self.assertEqual(QTUnit(*x5), y5, "Should be equal")



	def test_qtunit_transpose(self):

		#Test Data Declaration
		x0 = QTUnit(3, "Hello"); y0 = QTUnit(3, "Hello")
		x1 = QTUnit(complex(2, 4), 5); y1 = QTUnit(complex(2, -4), 5);
		x2 = QTUnit(complex(3, 3), (4, 4)); y2 = QTUnit(complex(3, -3), (4, 4))
		x3 = QTUnit(2, (5, 4, 2)); y3 = QTUnit(2, (5, 4, 2));
		x4 = QTUnit(complex(2, 5), (5, (4, 2), 3)); y4 = QTUnit(complex(2, -5), (5, (4, 2), 3));
		x5 = QTUnit(complex(4, 7), ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex(4, -7), ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}))

		print("Checking QTUnit Transpose")

		#Checking
		self.assertEqual(x0.t(), y0)
		self.assertEqual(x1.t(), y1)
		self.assertEqual(x2.t(), y2)
		self.assertEqual(x3.t(), y3)
		self.assertEqual(x4.t(), y4)
		self.assertEqual(x5.t(), y5)



	def test_qtunit_add(self):
		
		#Test Data Declaration
		x0 = QTUnit(complex(3)); y0 = QTUnit(complex(3)); z0 = QTData([QTUnit(*(complex(6), None,))]);
		x1 = QTUnit(complex(2), 5); y1 = QTUnit(complex(2), 2); z1 = QTData([QTUnit(complex(2), 5), QTUnit(complex(2), 2)]); 
		x2 = QTUnit(complex(3), (4, 4)); y2 = QTUnit(complex(3), (4, 4)); z2 = QTData([QTUnit(complex(6), (4, 4))])
		x3 = QTUnit(complex(2), (5, 4, 2)); y3 = QTUnit(complex(2), (5, 4, 1)); 
		z3 = QTData([QTUnit(complex(2), (5, 4, 2)), QTUnit(complex(2), (5, 4, 1))]);
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = QTData([QTUnit(complex(4, 6), (5, 4, 2, 3))]);
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QTData([QTUnit(complex(4, 8), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}))]);
		x6 = QTUnit(complex(1), 5); y6 = QTUnit(complex(3),5); z6 = QTData([QTUnit(complex(4),5)]);
		x7 = QTUnit(complex(1), 3); y7 = QTUnit(complex(3),5); z7 = QTData([QTUnit(complex(1),3), QTUnit(complex(3),5)]);

		print("Checking QTUnit Addition")

		#Checking 
		self.assertEqual(x0+y0, z0)
		self.assertEqual(x1+y1, z1)
		self.assertEqual(x2+y2, z2)
		self.assertEqual(x3+y3, z3)
		self.assertEqual(x4+y4, z4)
		self.assertEqual(x5+y5, z5)
		self.assertEqual(x6+y6, z6)
		self.assertEqual(x7+y7, z7)



	def test_qtunit_sub(self):
		#Test Data Declaration
		x0 = QTUnit(complex(3),); y0 = QTUnit(complex(3),); z0 = QTData([QTUnit(0,)]);
		x1 = QTUnit(complex(2), 5); y1 = QTUnit(complex(2), 2); z1 = QTData([QTUnit(complex(2), 5), QTUnit(complex(-2), 2)]); 
		x2 = QTUnit(complex(3), (4, 4)); y2 = QTUnit(complex(3), (4, 4)); z2 = QTData([QTUnit(0, (4, 4))])
		x3 = QTUnit(complex(2), (5, 4, 2)); y3 = QTUnit(complex(2), (5, 4, 1)); 
		z3 = QTData([QTUnit(complex(2), (5, 4, 2)), QTUnit(complex(-2), (5, 4, 1))]);
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = QTData([QTUnit(complex(0, -6), (5, 4, 2, 3))]);
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QTData([QTUnit(complex(0, -2), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}))]);
		x6 = QTUnit(complex(1), 5); y6 = QTUnit(complex(3),5); z6 = QTData([QTUnit(complex(-2),5)]);
		x7 = QTUnit(complex(1), 3); y7 = QTUnit(complex(3),5); z7 = QTData([QTUnit(complex(1),3), QTUnit(complex(-3),5)]);

		print("Checking QTUnit Subtraction")		

		#Checking 
		self.assertEqual(x0-y0, z0)
		self.assertEqual(x1-y1, z1)
		self.assertEqual(x2-y2, z2)
		self.assertEqual(x3-y3, z3)
		self.assertEqual(x4-y4, z4)
		self.assertEqual(x5-y5, z5)
		self.assertEqual(x6-y6, z6)
		self.assertEqual(x7-y7, z7)



	def test_qtunit_outer_product(self):

		#Test Data Declaration
		x0 = QTUnit(complex(3), "Hello"); y0 = QTUnit(complex(3), "Hi"); z0 = QOperator(complex(9), "Hello", "Hi")
		x1 = QTUnit(complex(2), 5); y1 = QTUnit(complex(2), 2); z1 = QOperator(complex(4), 5, 2)
		x2 = QTUnit(complex(3), (4, 4)); y2 = QTUnit(3, (4, 4)); z2 = QOperator(complex(9), (4,4), (4,4))
		x3 = QTUnit(complex(2), (5, 4, 2)); y3 = QTUnit(complex(2), (5, 4, 1)); 
		z3 = QOperator(complex(6), (5, 4, 2), (5, 4, 1));
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = QOperator(complex(2, 12), (5, 4, 2, 3), (5, 4, 2, 3))
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex((2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
		z5 = QOperator(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), 
			(4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		x6 = QTUnit(complex(1),5); y6 = QTUnit(complex(3),5); z6 = QOperator(complex(3), 5, 5)
		x7 = QTUnit(complex(1),3); y7 = QTUnit(complex(3),5); z7 = QOperator(complex(3), 3, 5)

		
		print("Checking QTUnit Outer Product")


		#Checking 
		self.assertEqual(x0*y0, z0)
		self.assertEqual(x1*y1, z1)
		self.assertEqual(x2*y2, z2)
		self.assertEqual(x3*y3, z3)
		self.assertEqual(x4*y4, z4)
		self.assertEqual(x5*y5, z5)
		self.assertEqual(x6*y6, z6)
		self.assertEqual(x7*y7, z7)



	def test_qtunit_inner_product(self):
		#Test Data Declaration
		x0 = QTUnit(complex(3), "Hello"); y0 = QTUnit(complex(3), "Hello"); z0 = complex(9)
		x1 = QTUnit(complex(2), 5); y1 = QTUnit(complex(2), 2); z1 = 0; 
		x2 = QTUnit(complex(3), (4, 4)); y2 = QTUnit(complex(3), (4, 4)); z2 = 9;
		x3 = QTUnit(complex(2), (5, 4, 2)); y3 = QTUnit(complex(2), (5, 4, 1)); z3 = 0;
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = complex(4, 12)
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = complex(-11, 16)
		x6 = QTUnit(complex(1), 5); y6 = QTUnit(3,5); z6 = complex(3)
		x7 = QTUnit(complex(1), 3); y7 = QTUnit(3,5); z7 = complex(0)


		print("Checking QTUnit Inner Product")

		#Checking
		self.assertEqual(x0*y0, z0)
		self.assertEqual(x1*y1, z1)
		self.assertEqual(x2*y2, z2)
		self.assertEqual(x3*y3, z3)
		self.assertEqual(x4*y4, z4)
		self.assertEqual(x5*y5, z5)
		self.assertEqual(x6*y6, z6)
		self.assertEqual(x7*y7, z7)



	def test_qtunit_tensor_product(self):
		#Test Data Declaration
		x0 = QTUnit(3, "Hello"); y0 = QTUnit(3,"Hi"); z0 = QTUnit(complex(3), ("Hello", "Hi"))
		x1 = QTUnit(2, 5); y1 = QTUnit(2, 2); z1 = QTUnit(complex(4), (5, 2)); 
		x2 = QTUnit(3, (4, 4)); y2 = QTUnit(3, (4, 4)); z2 = QTUnit(complex(9), ((4,4), (4,4)));
		x3 = QTUnit(2, (5, 4, 2)); y3 = QTUnit(2, (5, 4, 1)); 
		z3 = QTUnit(complex(4), ((5,4,2), (5,4,1)));
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = QTData([QTUnit((complex(4, 12), (5, 4, 2, 3), (5, 4, 2, 3)))]);
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QTUnit(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		x6 = QTUnit(complex(1), 5); y6 = QTUnit(complex(3), 5); z6 = QTUnit(complex(3), (5, 5));
		x7 = QTUnit(complex(1), 3); y7 = QTUnit(complex(3), 5); z7 = QTUnit(complex(3), (3, 5));

		print("Checking QTUnit Tensor Product")

		#Checking
		self.assertEqual(x0*y0, z0)
		self.assertEqual(x1*y1, z1)
		self.assertEqual(x2*y2, z2)
		self.assertEqual(x3*y3, z3)
		self.assertEqual(x4*y4, z4)
		self.assertEqual(x5*y5, z5)
		self.assertEqual(x6*y6, z6)
		self.assertEqual(x7*y7, z7)




	def test_qtunit_split(self):
		#Test Data Declaration
		x0 = QTUnit(3, "Hello"); y0 = QTUnit(3, "Hi"); z0 = QTUnit(complex(9), ("Hello","Hi"))
		x1 = QTUnit(2, 5); y1 = QTUnit(2, 2); z1 = QTUnit(complex(4), (5, 2)); 
		x2 = QTUnit(3, (4, 4)); y2 = QTUnit(3, (4, 4)); z2 = QTUnit(complex(9), ((4,4), (4,4)));
		x3 = QTUnit(2, (5, 4, 2)); y3 = QTUnit(2, (5, 4, 1)); 
		z3 = QTUnit(complex(4), ((5,4,2), (5,4,1)));
		x4 = QTUnit(complex(2), (5, 4, 2, 3)); y4 = QTUnit(complex(2, 6), (5, 4, 2, 3));
		z4 = QTData([QTUnit(complex(4, 12), (5, 4, 2, 3), (5, 4, 2, 3))]);
		x5 = QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		y5 = QTUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		z5 = QTUnit(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
		x6 = QTUnit(complex(1), 5); y6 = QTUnit((complex(3), 5)); z6 = QTUnit(complex(3), (5, 5));
		x7 = QTUnit(complex(1), 3); y7 = QTUnit((complex(3), 5)); z7 = QTUnit(complex(3), (3, 5));

		print("Checking QTUnit Split")

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




