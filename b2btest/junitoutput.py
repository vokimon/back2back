
from xml.dom.minidom import Document, Element

class TestCase() :
	def __init__(self, name, status, time, classname) :
		if not time.isdigit():
			raise ValueError

		self._element = Element("testcase")
		self._element.setAttribute("name", name)
		self._element.setAttribute("status", status)
		self._element.setAttribute("time", str(time))
		self._element.setAttribute("classname", classname)

	def getAttribute(self, attribute) :
		return self._element.getAttribute(attribute)

class TestSuite() :
	def __init__(self, name) :
		self._element = Element("testsuite")
		self._element.setAttribute("name", name)
		self._element.setAttribute("tests", "0")
		self._element.setAttribute("failures", "0")
		self._element.setAttribute("disabled", "0")
		self._element.setAttribute("errors", "0")
		self._element.setAttribute("time", "0")


	def getAttribute(self, attribute) :
		return self._element.getAttribute(attribute)

	def appendTestCase(self, testcase) :
		if not isinstance(testcase, TestCase) :
			raise TypeError()
		self._element.appendChild(testcase._element)
		self._element.setAttribute("tests", str(int(self._element.getAttribute("tests")) + 1)) 
		self._element.setAttribute("time", str(int(self._element.getAttribute("time")) + int(testcase.getAttribute("time"))))
		status = testcase.getAttribute("status")
		if status == "notrun" :
			self._element.setAttribute(self, "disabled",  str(int(self._element.getAttribute(self, "disabled")) + 1))

class JUnitDocument() :
	def __init__(self, name) :
		self._element = Element("testsuites")
		self._element.setAttribute("name", name)
		self._element.setAttribute("tests", "0")
		self._element.setAttribute("failures", "0")
		self._element.setAttribute("disabled", "0")
		self._element.setAttribute("errors", "0")
		self._element.setAttribute("time", "0")

	def getAttribute(self, attribute) :
		return self._element.getAttribute(attribute)

	def appendTestSuite(self, testsuite) :
		if not isinstance(testsuite, TestSuite) :
			raise TypeError()
		self._element.appendChild(testsuite._element)
		self._element.setAttribute("tests", str(int(self._element.getAttribute("tests")) + int(testsuite.getAttribute("tests"))))
		self._element.setAttribute("failures", str(int(self._element.getAttribute("failures")) + int(testsuite.getAttribute("failures"))))
		self._element.setAttribute("disabled", str(int(self._element.getAttribute("disabled")) + int(testsuite.getAttribute("disabled"))))
		self._element.setAttribute("errors", str(int(self._element.getAttribute("errors")) + int(testsuite.getAttribute("errors"))))
		self._element.setAttribute("time", str(int(self._element.getAttribute("time")) + int(testsuite.getAttribute("time"))))

	def toxml(self) :
		doc = Document()
		doc.appendChild(self._element)
		return doc.toprettyxml()


if __name__ == "__main__" :
	doc = JUnitDocument("First")

	testsuite = TestSuite("suite0")
	testsuite.appendTestCase(TestCase("test1", "run", "10", "class1"))
	testsuite.appendTestCase(TestCase("test1", "run", "10", "class1"))

	doc.appendTestSuite(TestSuite("suite1"))
	doc.appendTestSuite(testsuite)

	print doc.toxml()
