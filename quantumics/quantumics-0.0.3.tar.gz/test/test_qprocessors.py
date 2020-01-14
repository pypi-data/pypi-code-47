import sys; sys.path.append("../lib");
from qprocessors import QProcessor, CPUQProcessor, DWaveQProcessor, IBMQProcessor;






class QProcessorTest(unittest.TestCase):


	def test_qprocessor_constructor(self):
		pass



	def test_qprocessor_add(self):
		pass


	def test_qprocessor_sub(self):
		pass


	def test_qprocessor_div(self):
		pass



	def test_qprocessor_mul(self):
		pass




	def test_qprocessor_equal(self):
		pass



	def test_qprocessor_train(self):
		pass




	def test_qprocessor_fit(self):
		pass



	def test_qprocessor_eval(self):
		pass







class CPUQProcessorTest(unittest.TestCase):



	def test_cpuqprocessor_constructor(self):
	 	processor = CPUQProcessor();
	 	self.assertIsInstance(processor, CPUQProcessor);




	def test_cpuqprocessor_add(self):
		processor = CPUQProcessor();
		x0 = QUnit(); y0 = QUnit(); z0 = QData();
		x0.model.set_processor(processor);
		y0.model.set_processor(processor);
		self.assertEquals(x0 + y0, z0);
		self.assertEquals((x0 + y0).model.get_processor(), x0.model.get_processor());



	def test_cpuqprocessor_sub(self):
		processor = CPUQProcessor();
		x0 = QUnit(); y0 = QUnit(); z0 = QData();
		x0.model.set_processor(processor);
		y0.model.set_processor(processor);
		self.assertEquals(x0 - y0, z0);
		self.assertEquals((x0 - y0).model.get_processor(), x0.model.get_processor());



	def test_cpuqprocessor_div(self):
		processor = CPUQProcessor();
		x0 = QUnit(); y0 = QUnit(); z0 = QData();
		x0.model.set_processor(processor);
		y0.model.set_processor(processor);
		self.assertEquals(x0 / y0, z0);
		self.assertEquals((x0 / y0).model.get_processor(), x0.model.get_processor());



	def test_cpuqprocessor_mul(self):
		processor = CPUQProcessor();
		x0 = QUnit(); y0 = QUnit(); z0 = QData();
		x0.model.set_processor(processor);
		y0.model.set_processor(processor);
		self.assertEquals(x0 * y0, z0);
		self.assertEquals((x0 * y0).model.get_processor(), x0.model.get_processor());




	def test_cpuqprocessor_equal(self):
		pass



	def test_cpuqprocessor_train(self):
		pass




	def test_cpuqprocessor_fit(self):
		pass



	def test_cpuqprocessor_eval(self):
		pass








class DWaveQProcessorTest(unittest.TestCase):



	def test_dwaveqprocessor_constructor(self):
		pass



	def test_dwaveqprocessor_add(self):
		pass



	def test_dwaveqprocessor_sub(self):
		pass


	def test_dwaveqprocessor_div(self):
		pass



	def test_dwaveqprocessor_mul(self):
		pass




	def test_dwaveqprocessor_equal(self):
		pass



	def test_dwaveqprocessor_train(self):
		pass




	def test_dwaveqprocessor_fit(self):
		pass



	def test_dwaveqprocessor_eval(self):
		pass








class IBMQProcessorTest(unittest.TestCase):



	def test_ibmqprocessor_constructor(self):
		pass



	def test_ibmqprocessor_add(self):
		pass


	def test_ibmqprocessor_sub(self):
		pass


	def test_ibmqprocessor_div(self):
		pass



	def test_ibmqprocessor_mul(self):
		pass




	def test_ibmqprocessor_equal(self):
		pass



	def test_ibmqprocessor_train(self):
		pass




	def test_ibmqprocessor_fit(self):
		pass



	def test_ibmqprocessor_eval(self):
		pass




