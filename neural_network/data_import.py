import string
from math import exp
from random import randint
import numpy

def import_data(address, start):
	file = open(address, "r")
	values = file.read().split('\n')
	ret = []
	
	outputs = {}
	count = 0

	if(start == True): #Returns 100 random pieces of data
		for i in range(0, 100, 1):
			inputElem = []
			rowElem = values[randint(0, len(values)-1)].split(',')
			for j in range(0, len(rowElem) - 1, 1):
				if (j == len(rowElem)-2):
					if not (rowElem[j+1] in outputs.values()):
						outputs[count] = rowElem[j+1]
						#print("new output found:",outputs[count])
						count = count + 1
				try:
					inputElem += [float(rowElem[j])]
					#print("input: #",inputElem[-1])
				except:
					#print("none float found")
					continue

			ret += [inputElem + [count-1]]
			print(ret[-1])
		return [ret] + [outputs]

	#biases = find_max_min(values)

	# Returns first 50 pieces of consecutive data
	for i in range(min(start*50, len(values) - 50), min(start*50 + 50, len(values)), 1):
		inputElem = []
		rowElem = values[i].split(',')
		for j in range(0, len(rowElem) - 1, 1):
			if (j == len(rowElem)-2):
				if not (rowElem[j+1] in outputs.values()):
					outputs[count] = rowElem[j+1]
					#print("new output found:",outputs[count])
					count = count + 1
			try:
				inputElem += [float(rowElem[j])]
				#print("input: #",inputElem[-1])
			except:
				#print("none float found")
				continue

		ret += [inputElem + [count-1]]

	#print(ret)
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