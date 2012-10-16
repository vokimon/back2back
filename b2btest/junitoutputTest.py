import unittest
import junitoutput as JU

class TestCaseTest(unittest.TestCase):

	def test_creation(self):
		JU.TestCase("name")

	def test_creation_timeIsNotANumber(self):
		testcase = JU.TestCase("name")
		self.assertRaises(ValueError, testcase.setTime, "time")

	def test_creation_timeIsNegative(self):
		testcase = JU.TestCase("name")
		self.assertRaises(ValueError, testcase.setTime, "-1.0")

class TestSuiteTest(unittest.TestCase):	
	
	def test_creation(self):
		JU.TestSuite("testsuiteName")
		self.assertRaises(TypeError, JU.TestSuite)

	def test_addTestcase(self):
		JU.TestSuite("name").appendTestCase(JU.TestCase("name"))

	def test_time(self):
		testsuite = JU.TestSuite("name")
		testcase = JU.TestCase("name")

		testcase.setTime(0.3)
		testsuite.appendTestCase(testcase)
		self.assertEqual(float(testsuite._attrib("time")), 0.3)

		testcase.setTime(2.3)
		testsuite.appendTestCase(testcase)
		self.assertEqual(float(testsuite._attrib("time")), 2.6)

		testcase.setTime(1.1)
		testsuite.appendTestCase(testcase)
		self.assertEqual(float(testsuite._attrib("time")), 3.7)


if __name__ == '__main__':
	unittest.main()
