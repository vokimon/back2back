import unittest
import junitoutput as JU

class TestCaseTest(unittest.TestCase):

	def test_creation(self):
		JU.TestCase("name", "status", "1.0", "classname")

	def test_creation_timeIsNotANumber(self):
		self.assertRaises(ValueError, JU.TestCase, "name", "status", "time", "classname")

	def test_creation_timeIsNegative(self):
		self.assertRaises(ValueError, JU.TestCase, "name", "status", "-1.0", "classname")

	def test_attributes(self):
		testcase = JU.TestCase("name", "status", "1", "classname")
		self.assertEqual(testcase.attrib("name"), "name")
		self.assertEqual(testcase.attrib("status"), "status")
		self.assertEqual(testcase.attrib("time"), "1")
		self.assertEqual(testcase.attrib("classname"), "classname")


class TestSuiteTest(unittest.TestCase):	
	
	def test_creation(self):
		JU.TestSuite("testsuiteName")
		self.assertRaises(TypeError, JU.TestSuite)

	def test_addTestcase(self):
		JU.TestSuite("name").appendTestCase(JU.TestCase("name", "status", "1", "classname"))

	def test_time(self):
		testsuite = JU.TestSuite("name")
		testsuite.appendTestCase(JU.TestCase("name", "status", "0.3", "classname"))
		self.assertEqual(float(testsuite.attrib("time")), 0.3)
		testsuite.appendTestCase(JU.TestCase("name1", "status", "0.2", "classname"))
		self.assertEqual(float(testsuite.attrib("time")), 0.5)
		testsuite.appendTestCase(JU.TestCase("name2", "status", "9.3", "classname"))
		self.assertEqual(float(testsuite.attrib("time")), 9.8)
		testsuite.appendTestCase(JU.TestCase("name3", "status", "01.3", "classname"))
		self.assertEqual(float(testsuite.attrib("time")), 11.1)

if __name__ == '__main__':
	unittest.main()
