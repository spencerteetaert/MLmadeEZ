import string
from math import exp
from random import randint
import numpy
import random

def import_data(address):
	file = open(address, "r")
	values = file.read().split('\n')
	#values.shuffle()
	#print(values)

	ret = []  # list of all elements 
	outputs = {}  # output dict
	count = 0  # tracking output nodes

	# Returns first 50 pieces of consecutive data
	for i in range(0, len(values), 1):
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
			except:
				continue

		ret += [inputElem + [list(outputs.values()).index(rowElem[len(rowElem) - 1])]]
	print("training:",[ret] + [outputs])
	return [ret] + [outputs]