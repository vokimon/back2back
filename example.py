from b2btest import runBack2BackProgram
import sys

datapath = "data" # Point it to the directory containing your reference data

runBack2BackProgram(datapath, sys.argv, [
	('HelloWorld',
		'echo Hello World > output.txt', [
			'output.txt',
		]),
	('AlwaysChanging',
		'date > output.txt', [
			'output.txt',
		]),
])


