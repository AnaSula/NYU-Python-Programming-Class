import unittest
from c2_project import ProcessData
from c2_project import SVM


class TestProcessData(unittest.TestCase):
    def setUp(self):
        self.test_process= ProcessData()
        

    def testsplit_train(self):
        self.assertTrue(type(self.test_process.split_train()[0]) == type(self.test_process.split_train()[1])== type(self.test_process.split_train()[2]) == type(self.test_process.split_train()[3]))


    def testsplit_valid(self):
        self.assertTrue(type(self.test_process.split_valid()[0])== type(self.test_process.split_valid()[1]))


    def testvectorize_train(self):
    	self.assertTrue(type(self.test_process.vectorize_train()[0]) == type(self.test_process.vectorize_train()[1]))


class TestSVM(unittest.TestCase):
	def setUp(self):
		self.test_svm= SVM()


	def testvalid_svm(self):
		self.assertTrue(len(self.test_svm.split_valid()[1])==len(self.test_svm.valid_svm()[2]))


	def test_cfm(self):
		self.assertEqual(self.test_svm.cfm()[0].shape, (2, 2))


	def testoutput_data(self):
		self.assertEqual(self.test_svm.output_data().shape, (len(self.test_svm.valid_svm()[2]), 3))


if __name__ == '__main__':
	unittest.main()