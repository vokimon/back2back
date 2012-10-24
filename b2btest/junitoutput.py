import xml.dom.minidom as MD

class TestCase :
	def __init__(self, name) :
		if not name :
			raise ValueError

		self._element = MD.Element("testcase")
		self._element.setAttribute("name", name)
		self._element.setAttribute("status", "run")
		self._element.setAttribute("time", "0")
		self._element.setAttribute("classname", "")
		self.failed = False

	def _attrib(self, attribute) :
		return self._element.getAttribute(attribute)

	def setTime(self, time) :
		if float(time) < 0.0 :
			raise ValueError
		self._element.setAttribute("time", str(time))

	def setClassname(self, classname) :
		self._element.setAttribute("classname", classname)	

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


	def _attrib(self, attribute) :
		return self._element.getAttribute(attribute)

	def appendTestCase(self, testcase) :
		if not isinstance(testcase, TestCase) :
			raise TypeError()

		self._element.appendChild(testcase._element)
		self._element.setAttribute("tests", str(int(self._attrib("tests")) + 1)) 
		self._element.setAttribute("time", str(float(self._attrib("time")) + float(testcase._attrib("time"))))
		status = testcase._attrib("status")
		if status == "notrun" :
			self._element.setAttribute("disabled",  str(int(self._attrib("disabled")) + 1))
		if testcase.failed == True :
			self._element.setAttribute("failures", str(int(self._attrib("failures")) + 1))


class JUnitDocument() :
	def __init__(self, name) :
		self._element = MD.Element("testsuites")
		self._element.setAttribute("name", name)
		self._element.setAttribute("tests", "0")
		self._element.setAttribute("failures", "0")
		self._element.setAttribute("disabled", "0")
		self._element.setAttribute("errors", "0")
		self._element.setAttribute("time", "0")

	def _attrib(self, attribute) :
		return self._element.getAttribute(attribute)

	def appendTestSuite(self, testsuite) :
		if not isinstance(testsuite, TestSuite) :
			raise TypeError()
		self._element.appendChild(testsuite._element)
		self._element.setAttribute("tests", str(int(self._attrib("tests")) + int(testsuite._attrib("tests"))))
		self._element.setAttribute("failures", str(int(self._attrib("failures")) + int(testsuite._attrib("failures"))))
		self._element.setAttribute("disabled", str(int(self._attrib("disabled")) + int(testsuite._attrib("disabled"))))
		self._element.setAttribute("errors", str(int(self._attrib("errors")) + int(testsuite._attrib("errors"))))
		self._element.setAttribute("time", str(float(self._attrib("time")) + float(testsuite._attrib("time"))))

	def toxml(self) :
		doc = MD.Document()
		doc.appendChild(self._element)
		return doc.toprettyxml()


if __name__ == "__main__" :
	doc = JUnitDocument("MyTests")

	testsuite = TestSuite("testsuite_name")

	testcase = TestCase("testcase_name")
	testcase.setTime(1.3)
	testcase.setClassname("testcase_classname")
	testcase.appendFailure("failure message")

	testcase1 = TestCase("testcase1_name")
	testcase1.setTime(0.3)

	testsuite.appendTestCase(testcase)
	testsuite.appendTestCase(testcase1)

	doc.appendTestSuite(testsuite)

	print doc.toxml()
