import unittest
import junitoutput as JU

class TestCaseTest(unittest.TestCase):

	def test_creation(self):
		JU.TestCase("name", "status", "1", "classname")
		JU.TestCase("name", "status", 1, "classname")
		JU.TestCase("name", "status", 1.0, "classname")

	def test_creation_timeIsNotANumber(self):
		self.assertRaises(ValueError, JU.TestCase, "name", "status", "time", "classname")

class TestSuiteTest(unittest.TestCase):	
	
	def test_creation(self):
		JU.TestSuite("testsuiteName")
		self.assertRaises(TypeError, JU.TestSuite)

	def test_addTestcase(self):
		JU.TestSuite("name").appendTestCase(JU.TestCase("name", "status", "10", "classname"))

if __name__ == '__main__':
	unittest.main()
