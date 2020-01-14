import sys;
import unittest;
sys.path.append("../pylib/");
from quantumics import QUnit, QTUnit, QData;
from processors import CPUQProcessor, DWaveQProcessor, IBMQProcessor;
from qoperator import QOperator;


class QUnitTest(unittest.TestCase):
	


	def test_qunit_constructor(self):

		#Test Data Declaration
		x0 = (3, "Hello"); y0 = QUnit(3, "Hello")
		x1 = (2, 5); y1 = QUnit(2, 5);
		x2 = (3, (4, 4)); y2 = QUnit(3, (4, 4))
		x3 = (2, (5, 4, 2)); y3 = QUnit(2, (5, 4, 2));
		x4 = (complex(2, 5), ((4, 2), 3)); y4 = QUnit(complex(2, 5), ((4, 2), 3));
		x5 = (2, ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));
		y5 = QUnit(2, ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"}));

		print("Checking Constructor");

		#Checking
		self.assertEqual(QUnit(*x0), y0, "Should be equal")
		self.assertEqual(QUnit(*x1), y1, "Should be equal")
		self.assertEqual(QUnit(*x2), y2, "Should be equal")
		self.assertEqual(QUnit(*x3), y3, "Should be equal")
		self.assertEqual(QUnit(*x4), y4, "Should be equal")
		self.assertEqual(QUnit(*x5), y5, "Should be equal")



	def test_qunit_transpose(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:

			#Test Data Declaration
			x,y = [],[]; 
			x.append(QUnit(3, "Hello")); y.append(QTUnit(3, "Hello"))
			x.append(QUnit(complex(2, 4), 5)); y.append(QTUnit(complex(2, -4), 5));
			x.append(QUnit(complex(3, 3), (4, 4))); y.append(QTUnit(complex(3, -3), (4, 4)))
			x.append(QUnit(2, (5, 4, 2))); y.append(QTUnit(2, (5, 4, 2)));
			x.append(QUnit(complex(2, 5), (5, (4, 2), 3))); y.append(QTUnit(complex(2, -5), (5, (4, 2), 3)));
			x.append(QUnit(complex(4, 7), ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"})));
			y.append(QTUnit(complex(4, -7), ((5, 4, 2, 3), {"hello": "world"}, {"machine":"learning"})))

			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);

			print("Checking Transpose")

			#Checking
			self.assertEqual(x0.t(), y0)
			self.assertEqual(x1.t(), y1)
			self.assertEqual(x2.t(), y2)
			self.assertEqual(x3.t(), y3)
			self.assertEqual(x4.t(), y4)
			self.assertEqual(x5.t(), y5)



	def test_qunit_add(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:
		
			#Test Data Declaration
			x,y,z = [],[],[];
			x.append(QUnit(complex(3))); y.append(QUnit(complex(3))); z.append(QData([QUnit(*(complex(6), None,))]));
			x.append(QUnit(complex(2), 5)); y.append(QUnit(complex(2), 2)); z.append(QData([QUnit(complex(2), 5), QUnit(complex(2), 2)])); 
			x.append(QUnit(complex(3), (4, 4))); y.append(QUnit(complex(3), (4, 4))); z.append(QData([QUnit(complex(6), (4, 4))]))
			x.append(QUnit(complex(2), (5, 4, 2))); y.append(QUnit(complex(2), (5, 4, 1))); 
			z.append(QData([QUnit(complex(2), (5, 4, 2)), QUnit(complex(2), (5, 4, 1))]));
			x.appned(QUnit(complex(2), (5, 4, 2, 3))); y.append(QUnit(complex(2, 6), (5, 4, 2, 3)));
			z.append(QData([QUnit(complex(4, 6), (5, 4, 2, 3))]));
			x.append(QUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			y.append(QUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			z.append(QData([QUnit(complex(4, 8), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}))]));
			x.append(QUnit(complex(1), 5)); y.append(QUnit(complex(3),5)); z.append(QData([QUnit(complex(4),5)]));
			x.append(QUnit(complex(1), 3)); y.append(QUnit(complex(3),5)); z.append(QData([QUnit(complex(1),3), QUnit(complex(3),5)]));

			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);
				z[i].model.set_processor(processor);


			print("Checking Addition")

			#Checking 
			self.assertEqual(x0+y0, z0)
			self.assertEqual(x1+y1, z1)
			self.assertEqual(x2+y2, z2)
			self.assertEqual(x3+y3, z3)
			self.assertEqual(x4+y4, z4)
			self.assertEqual(x5+y5, z5)
			self.assertEqual(x6+y6, z6)
			self.assertEqual(x7+y7, z7)



	def test_qunit_sub(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:

			#Test Data Declaration
			x,y,z = [],[],[];
			x[0] = QUnit(complex(3),); y[0] = QUnit(complex(3),); z[0] = QData([QUnit(0,)]);
			x[1] = QUnit(complex(2), 5); y[1] = QUnit(complex(2), 2); z[1] = QData([QUnit(complex(2), 5), QUnit(complex(-2), 2)]); 
			x[2] = QUnit(complex(3), (4, 4)); y[2] = QUnit(complex(3), (4, 4)); z[2] = QData([QUnit(0, (4, 4))])
			x[3] = QUnit(complex(2), (5, 4, 2)); y[3] = QUnit(complex(2), (5, 4, 1)); 
			z[3] = QData([QUnit(complex(2), (5, 4, 2)), QUnit(complex(-2), (5, 4, 1))]);
			x[4] = QUnit(complex(2), (5, 4, 2, 3)); y[4] = QUnit(complex(2, 6), (5, 4, 2, 3));
			z[4] = QData([QUnit(complex(0, -6), (5, 4, 2, 3))]);
			x[5] = QUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
			y[5] = QUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
			z[5] = QData([QUnit(complex(0, -2), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}))]);
			x[6] = QUnit(complex(1), 5); y[6] = QUnit(complex(3),5); z[6] = QData([QUnit(complex(-2),5)]);
			x[7] = QUnit(complex(1), 3); y[7] = QUnit(complex(3),5); z[7] = QData([QUnit(complex(1),3), QUnit(complex(-3),5)]);

			
			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);
				z[i].model.set_processor(processor);

			print("Checking Subtraction")		

			#Checking 
			self.assertEqual(x0-y0, z0)
			self.assertEqual(x1-y1, z1)
			self.assertEqual(x2-y2, z2)
			self.assertEqual(x3-y3, z3)
			self.assertEqual(x4-y4, z4)
			self.assertEqual(x5-y5, z5)
			self.assertEqual(x6-y6, z6)
			self.assertEqual(x7-y7, z7)



	def test_qunit_outer_product(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:

			#Test Data Declaration
			x,y,z = [],[],[];
			x[0] = QUnit(complex(3), "Hello"); y[0] = QTUnit(complex(3), "Hi"); z[0] = QOperator(complex(9), "Hello", "Hi")
			x[1] = QUnit(complex(2), 5); y[1] = QTUnit(complex(2), 2); z[1] = QOperator(complex(4), 5, 2)
			x[2] = QUnit(complex(3), (4, 4)); y[2] = QTUnit(3, (4, 4)); z[2] = QOperator(complex(9), (4,4), (4,4))
			x[3] = QUnit(complex(2), (5, 4, 2)); y[3] = QTUnit(complex(2), (5, 4, 1)); 
			z[3] = QOperator(complex(6), (5, 4, 2), (5, 4, 1));
			x[4] = QUnit(complex(2), (5, 4, 2, 3)); y[4] = QTUnit(complex(2, 6), (5, 4, 2, 3));
			z[4] = QOperator(complex(2, 12), (5, 4, 2, 3), (5, 4, 2, 3))
			x[5] = QUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
			y[5] = QTUnit(complex((2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			z[5] = QOperator(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), 
				(4, 2, 3, {"hello": "world"}, {"machine":"learning"}));
			x[6] = QUnit(complex(1),5); y[6] = QTUnit(complex(3),5); z[6] = QOperator(complex(3), 5, 5)
			x[7] = QUnit(complex(1),3); y[7] = QTUnit(complex(3),5); z[7] = QOperator(complex(3), 3, 5)


			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);
				z[i].model.set_processor(processor);

			
			print("Checking Outer Product")


			#Checking 
			self.assertEqual(x0*y0, z0)
			self.assertEqual(x1*y1, z1)
			self.assertEqual(x2*y2, z2)
			self.assertEqual(x3*y3, z3)
			self.assertEqual(x4*y4, z4)
			self.assertEqual(x5*y5, z5)
			self.assertEqual(x6*y6, z6)
			self.assertEqual(x7*y7, z7)



	def test_qunit_inner_product(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:

			#Test Data Declaration
			x,y,z = [],[],[];
			x.append(QTUnit(complex(3), "Hello")); y.append(QUnit(complex(3), "Hello")); z.append(complex(9))
			x.append(QTUnit(complex(2), 5)); y.append(QUnit(complex(2), 2)); z.append(0); 
			x.append(QTUnit(complex(3), (4, 4))); y.append(QUnit(complex(3), (4, 4))); z.append(9);
			x.append(QTUnit(complex(2), (5, 4, 2))); y.append(QUnit(complex(2), (5, 4, 1))); z.append(0);
			x.append(QTUnit(complex(2), (5, 4, 2, 3))); y.append(QUnit(complex(2, 6), (5, 4, 2, 3)));
			z.append(complex(4, 12))
			x.append(QTUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			y.append(QUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			z.append(complex(-11, 16))
			x.append(QTUnit(complex(1), 5)); y.append(QUnit(3,5)); z.append(complex(3))
			x.append(QTUnit(complex(1), 3)); y.append(QUnit(3,5)); z.append(complex(0))


			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);


			print("Checking Inner Product")

			#Checking
			self.assertEqual(x0*y0, z0)
			self.assertEqual(x1*y1, z1)
			self.assertEqual(x2*y2, z2)
			self.assertEqual(x3*y3, z3)
			self.assertEqual(x4*y4, z4)
			self.assertEqual(x5*y5, z5)
			self.assertEqual(x6*y6, z6)
			self.assertEqual(x7*y7, z7)



	def test_qunit_tensor_product(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:

			#Test Data Declaration
			x,y,z = [],[],[];
			x.append(QUnit(3, "Hello")); y.append(QUnit(3,"Hi")); z.append(QUnit(complex(3), ("Hello", "Hi")))
			x.append(QUnit(2, 5)); y.append(QUnit(2, 2)); z.append(QUnit(complex(4), (5, 2))); 
			x.append(QUnit(3, (4, 4))); y.append(QUnit(3, (4, 4))); z.append(QUnit(complex(9), ((4,4), (4,4))));
			x.append(QUnit(2, (5, 4, 2))); y.append(QUnit(2, (5, 4, 1))); 
			z.append(QUnit(complex(4), ((5,4,2), (5,4,1))));
			x.append(QUnit(complex(2), (5, 4, 2, 3))); y.append(QUnit(complex(2, 6), (5, 4, 2, 3)));
			z.append(QData([QUnit((complex(4, 12), (5, 4, 2, 3), (5, 4, 2, 3)))]));
			x.append(QUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			y.append(QUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			z.append(QUnit(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			x.append(QUnit(complex(1), 5)); y.append(QUnit(complex(3), 5)); z.append(QUnit(complex(3), (5, 5)));
			x.append(QUnit(complex(1), 3)); y.append(QUnit(complex(3), 5)); z.append(QUnit(complex(3), (3, 5)));

			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);
				z[i].model.set_processor(processor);


			print("Checking Tensor Product")

			#Checking
			self.assertEqual(x0*y0, z0)
			self.assertEqual(x1*y1, z1)
			self.assertEqual(x2*y2, z2)
			self.assertEqual(x3*y3, z3)
			self.assertEqual(x4*y4, z4)
			self.assertEqual(x5*y5, z5)
			self.assertEqual(x6*y6, z6)
			self.assertEqual(x7*y7, z7)




	def test_qunit_split(self):
		for processor in [CPUQProcessor(), DWaveQProcessor(), IBMQProcessor()]:

			#Test Data Declaration
			x,y,z = [],[],[];
			x.append(QUnit(3, "Hello")); y.append(QUnit(3, "Hi")); z.append(QUnit(complex(9), ("Hello","Hi")))
			x.append(QUnit(2, 5)); y.append(QUnit(2, 2)); z.append(QUnit(complex(4), (5, 2))); 
			x.append(QUnit(3, (4, 4))); y.append(QUnit(3, (4, 4))); z.append(QUnit(complex(9), ((4,4), (4,4))));
			x.append(QUnit(2, (5, 4, 2))); y.append(QUnit(2, (5, 4, 1))); 
			z.append(QUnit(complex(4), ((5,4,2), (5,4,1))));
			x.append(QUnit(complex(2), (5, 4, 2, 3))); y.append(QUnit(complex(2, 6), (5, 4, 2, 3)));
			z.append(QData([QUnit(complex(4, 12), (5, 4, 2, 3), (5, 4, 2, 3))]));
			x.append(QUnit(complex(2, 3), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			y.append(QUnit(complex(2, 5), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			z.append(QUnit(complex(-11, 16), (4, 2, 3, {"hello": "world"}, {"machine":"learning"}), (4, 2, 3, {"hello": "world"}, {"machine":"learning"})));
			x.append(QUnit(complex(1), 5)); y.append(QUnit((complex(3), 5))); z.append(QUnit(complex(3), (5, 5)));
			x.append(QUnit(complex(1), 3)); y.append(QUnit((complex(3), 5))); z.append(QUnit(complex(3), (3, 5)));


			for i in range(len(y)):
				x[i].model.set_processor(processor);
				y[i].model.set_processor(processor);
				z[i].model.set_processor(processor);


			print("Checking Split")

			#Checking
			self.assertEqual((x0, y0), z0.split((1, 1)))
			self.assertEqual((x1, y1), z1.split((1, 1)))
			self.assertEqual((x2, y2), z2.split((1, 1)))
			self.assertEqual((x3, y3), z3.split((1,  1)))
			self.assertEqual((x4, y4), z4.split((2, complex(2, 6))))
			self.assertEqual((x5, y5), z5.split((complex(2, 3), complex(2, 5))))
			self.assertEqual((x6, y6), z6.split((1, 3)))
			self.assertEqual((x7, y7), z7.split((1, 3)))

