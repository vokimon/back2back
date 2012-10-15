import unittest
import junitoutput as JU

class TestCaseTest(unittest.TestCase):

	def test_creation(self):
		JU.TestCase("name", "status", "1", "classname")

	def test_creation_timeIsNotANumber(self):
		self.assertRaises(ValueError, JU.TestCase, "name", "status", "time", "classname")

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

	def test_addTestcaseWithSameName(self):
		testsuite = JU.TestSuite("name")
		self.assertRaises(NameError, testsuite.appendTestCase, JU.TestCase("name", "status", "1", "classname"))


if __name__ == '__main__':
	unittest.main()
