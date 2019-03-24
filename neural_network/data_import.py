import string
from math import exp
import numpy

def import_data(address):
	file = open(address, "r")
	values = file.read().split('\n')
	ret = []
	
	outputs = {}
	count = 0

	#biases = find_max_min(values)

	for j in range(0, len(values), 1):
		inputElem = []
		rowElem = values[j].split(',')
		for i in range(0, len(rowElem) - 1, 1):
			print("pre-squish",rowElem[i])
			inputElem += [float(rowElem[i])]
			print("post squish",inputElem[-1])

			if (i == len(rowElem)-2):
				if not (rowElem[i+1] in outputs.values()):
					outputs[count] = rowElem[i+1]
					count = count + 1

		ret += [inputElem + [count-1]]

	return [ret] + [outputs]
	#print(values)

def find_max_min(value):
	values = list(value)
	minMax = [100000000,-1000000000]
	for j in range(0, len(values), 1):
		inputElem = []
		rowElem = values[j].split(',')
		for i in range(0, len(rowElem) - 1, 1):
			inputElem = convert_to_usable_number(rowElem[i])
			if (inputElem < minMax[0]):
				minMax[0] = inputElem
			if(inputElem > minMax[1]):
				minMax[1] = inputElem

	a = (-1*numpy.log(0.111111111)*numpy.log(81))/(minMax[1]*numpy.log(9) - minMax[0]*numpy.log(0.11111111))
	b = (minMax[1]*numpy.log(9)-minMax[0]*numpy.log(0.111111111))/numpy.log(81)
	print(minMax)
	print([a,b])
	return [a,b]

def convert_to_usable_number(value):
	ret = 0
	j = 0
	for i in value:
		ret += ord(i)**(j)
		j += 1
	print("usable #:",ret)
	return ret

# Transfer neuron activation
def transfer(activation, biases):
	return 10 / (1.0 + exp(-biases[0]*(activation - biases[1])))