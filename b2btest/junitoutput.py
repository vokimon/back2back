
from xml.dom.minidom import Document, Element

class TestCase(Element) :
	def __init__(self) :
		Element.__init__(self, "testcase")
		Element.setAttribute(self, "name", "")
		Element.setAttribute(self, "status", "")
		Element.setAttribute(self, "time", "")
		Element.setAttribute(self, "classname", "")

	def appendChild(self, node) :
		# TODO: raise exception
		pass

class TestSuite(Element) :
	def __init__(self) :
		Element.__init__(self, "testsuite")

	def appendChild(self, testcase) :
		if not isinstance(testcase, TestCase) :
			raise TypeError()
		Element.appendChild(self, testcase)

class TestSuites(Element) :
	def __init__(self) :
		Element.__init__(self, "testsuites")

	def appendChild(self, testsuite) :
		if not isinstance(testsuite, TestSuite) :
			raise TypeError()
		Element.appendChild(self, testsuite)

class JUnitDocument(Document) :
	def __init__(self) :
		Document.__init__(self)


if __name__ == "__main__" :
	doc = JUnitDocument()

	testsuites = TestSuites()
	testsuites.appendChild(TestSuite())

	doc.appendChild(testsuites)
	print doc.toprettyxml()
