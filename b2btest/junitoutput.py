
from xml.dom.minidom import Document

class TestCase :
	def __init__(self) :
		self.name = ""
		self.status = ""
		self.time = ""
		self.classname = ""

	def toElement(self) :
		element = Document().createElement("testcase")
		element.setAttribute("name", self.name)
		element.setAttribute("status", self.status)
		element.setAttribute("time", self.time)
		element.setAttribute("classname", self.classname)
		return element

class TestSuite :
	def __init__(self) :
		self.name = ""
		self.failures = 0
		self.disabled = 0
		self.errors = 0
		self.time = 0
		self.tests = 0
		self._testcases = []

	def appendTestCase(self, testcase) :
		if not isinstance(testcase, TestCase) :
			raise TypeError("Not a TestCase instance")

		self._testcases.append(testcase)
		self.tests += 1;

	def toElement(self) :
		element = Document().createElement("testsuite")
		element.setAttribute("name", self.name)
		element.setAttribute("tests", str(self.tests))
		element.setAttribute("failures", str(self.failures))
		element.setAttribute("disabled", str(self.disabled))
#		element.setAttribute("errors", self.errors)
#		element.setAttribute("time", self.time)
		for testcase in self._testcases :
			element.appendChild(testcase.toElement())
		return element;

class JUnitTestXMLOutput :
	def __init__(self) :
		self._testsuites = []

	def appendTestSuite(self, testsuite) :
		if not isinstance(testsuite, TestSuite) :
			raise TypeError("Not a TestSuite instance")
		self._testsuites.append(testsuite)

	def toXML(self) :
		doc = Document()
		element = doc.createElement("testsuites")
		element.setAttribute("tests", str(sum([testsuite.tests for testsuite in self._testsuites])))

		for testsuite in self._testsuites :
			element.appendChild(testsuite.toElement())

		doc.appendChild(element)
		return doc

if __name__ == "__main__" :
	xml = JUnitTestXMLOutput()

	testsuite = TestSuite()
	testsuite.appendTestCase(TestCase())
	testsuite.appendTestCase(TestCase())
	testsuite.appendTestCase(TestCase())
	testsuite.appendTestCase(TestCase())

	xml.appendTestSuite(testsuite)
	
	print xml.toXML().toprettyxml()
