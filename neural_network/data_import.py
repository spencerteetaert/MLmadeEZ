import string
from math import exp
from random import randint
import numpy

def import_data(address, start):
	file = open(address, "r")
	values = file.read().split('\n')
	ret = []  # list of all elements 
	outputs = {}  # output dict
	count = 0  # tracking output nodes
	if(start == True): #Returns 100 random pieces of data
		for i in range(0, 100, 1):
			inputElem = []
			rowElem = values[randint(0, len(values)-1)].split(',')
			for j in range(0, len(rowElem) - 1, 1):
				if (j == len(rowElem)-2):  # 2nd last element, allows you to index the last element
					if not (rowElem[j+1] in outputs.values()):  # last element (output) is already found
						outputs[count] = rowElem[j+1]  # add undiscovered output
						count = count + 1  # increment output counter
				try:
					inputElem += [float(rowElem[j])]  # try to cast to float if possible
				except:
					continue
<<<<<<< HEAD
			ret += [inputElem]  
=======

			ret += [inputElem + [list(outputs.values()).index(rowElem[len(rowElem) - 1])]]

		print([ret] + [outputs])
>>>>>>> 2073a3d77d102beacc1b762804adc8e2bbde70e4
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

		ret += [inputElem + [list(outputs.values()).index(rowElem[len(rowElem) - 1])]]

	#print(ret)
	print([ret] + [outputs])
	return [ret] + [outputs]
	#print(values)