
import xml.dom.minidom as MD

class TestCase() :
	def __init__(self, name, status, time, classname) :
		if not time.isdigit():
			raise ValueError()
		self._element = MD.Element("testcase")
		self._element.setAttribute("name", name)
		self._element.setAttribute("status", status)
		self._element.setAttribute("time", time)
		self._element.setAttribute("classname", classname)

	def attrib(self, attribute) :
		return self._element.getAttribute(attribute)

class TestSuite() :
	def __init__(self, name) :
		self._element = MD.Element("testsuite")
		self._element.setAttribute("name", name)
		self._element.setAttribute("tests", "0")
		self._element.setAttribute("failures", "0")
		self._element.setAttribute("disabled", "0")
		self._element.setAttribute("errors", "0")
		self._element.setAttribute("time", "0")


	def attrib(self, attribute) :
		return self._element.getAttribute(attribute)

	def appendTestCase(self, testcase) :
		if not isinstance(testcase, TestCase) :
			raise TypeError()
		self._element.appendChild(testcase._element)
		self._element.setAttribute("tests", str(float(self.attrib("tests")) + 1)) 
		self._element.setAttribute("time", str(float(self.attrib("time")) + float(testcase.attrib("time"))))
		status = testcase.attrib("status")
		if status == "notrun" :
			self._element.setAttribute(self, "disabled",  str(float(self.attrib(self, "disabled")) + 1))

class JUnitDocument() :
	def __init__(self, name) :
		self._element = MD.Element("testsuites")
		self._element.setAttribute("name", name)
		self._element.setAttribute("tests", "0")
		self._element.setAttribute("failures", "0")
		self._element.setAttribute("disabled", "0")
		self._element.setAttribute("errors", "0")
		self._element.setAttribute("time", "0")

	def attrib(self, attribute) :
		return self._element.getattribute(attribute)

	def appendTestSuite(self, testsuite) :
		if not isinstance(testsuite, TestSuite) :
			raise TypeError()
		self._element.appendChild(testsuite._element)
		self._element.setAttribute("tests", str(float(self.attrib("tests")) + float(testsuite.attrib("tests"))))
		self._element.setAttribute("failures", str(float(self.attrib("failures")) + float(testsuite.attrib("failures"))))
		self._element.setAttribute("disabled", str(float(self.attrib("disabled")) + float(testsuite.attrib("disabled"))))
		self._element.setAttribute("errors", str(float(self.attrib("errors")) + float(testsuite.attrib("errors"))))
		self._element.setAttribute("time", str(float(self.attrib("time")) + float(testsuite.attrib("time"))))

	def toxml(self) :
		doc = MD.Document()
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
