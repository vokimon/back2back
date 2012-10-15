
import xml.dom.minidom as MD

class TestCase() :
	def __init__(self, name, status, time, classname) :
		if float(time) < 0.0:
			raise ValueError
		
		self._element = MD.Element("testcase")
		self._element.setAttribute("name", name)
		self._element.setAttribute("status", status)
		self._element.setAttribute("time", time)
		self._element.setAttribute("classname", classname)
		self.failed = False

	def attrib(self, attribute) :
		return self._element.getAttribute(attribute)

	def appendFailure(self, message) :
		failure = MD.Element("failure")
		failure.setAttribute("message", message)
		failure.setAttribute("type", "")
		self._element.appendChild(failure)
		self.failed = True


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
		self._element.setAttribute("tests", str(int(self.attrib("tests")) + 1)) 
		self._element.setAttribute("time", str(float(self.attrib("time")) + float(testcase.attrib("time"))))
		status = testcase.attrib("status")
		if status == "notrun" :
			self._element.setAttribute("disabled",  str(int(self.attrib("disabled")) + 1))
		if testcase.failed == True :
			self._element.setAttribute("failures", str(int(self.attrib("failures")) + 1))


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
		return self._element.getAttribute(attribute)

	def appendTestSuite(self, testsuite) :
		if not isinstance(testsuite, TestSuite) :
			raise TypeError()
		self._element.appendChild(testsuite._element)
		self._element.setAttribute("tests", str(int(self.attrib("tests")) + int(testsuite.attrib("tests"))))
		self._element.setAttribute("failures", str(int(self.attrib("failures")) + int(testsuite.attrib("failures"))))
		self._element.setAttribute("disabled", str(int(self.attrib("disabled")) + int(testsuite.attrib("disabled"))))
		self._element.setAttribute("errors", str(int(self.attrib("errors")) + int(testsuite.attrib("errors"))))
		self._element.setAttribute("time", str(float(self.attrib("time")) + float(testsuite.attrib("time"))))

	def toxml(self) :
		doc = MD.Document()
		doc.appendChild(self._element)
		return doc.toprettyxml()


if __name__ == "__main__" :
	doc = JUnitDocument("First")

	testcase = TestCase("test0", "notrun", "1", "class")
	testcase.appendFailure("failure message")

	testsuite = TestSuite("suite0")
	testsuite.appendTestCase(TestCase("test1", "run", "10", "class1"))
	testsuite.appendTestCase(TestCase("test2", "run", "10", "class1"))
	testsuite.appendTestCase(testcase)

	doc.appendTestSuite(TestSuite("suite1"))
	doc.appendTestSuite(testsuite)

	print doc.toxml()
