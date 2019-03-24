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

	if(start == -1): #Returns 100 random pieces of data
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
					continue

			ret += [inputElem + [list(outputs.values()).index(rowElem[len(rowElem) - 1])]]

		print([ret] + [outputs])
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
	print("training:",[ret] + [outputs])
	return [ret] + [outputs]
	#print(values)