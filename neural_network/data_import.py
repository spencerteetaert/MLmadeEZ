import string
from math import exp
from random import randint
import numpy
from random import shuffle

def import_data(address):
	file = open(address, "r")
	values = file.read().split('\n')
	values = values[0:500]
	shuffle(values)

	ret = []  # list of all elements 
	outputs = {}  # output dict
	count = 0  # tracking output nodes

	# Returns first 50 pieces of consecutive data
	for i in range(0, min(len(values), 500), 1):
		inputElem = []
		rowElem = values[i].split(',')
		for j in range(0, len(rowElem) - 1, 1):
			if (j == len(rowElem)-2):
				if not (rowElem[j+1] in outputs.values()):
					outputs[count] = rowElem[j+1]
					count = count + 1
			try:
				inputElem += [float(rowElem[j])]
			except:
				continue

		ret += [inputElem + [list(outputs.values()).index(rowElem[len(rowElem) - 1])]]

	return [ret] + [outputs]

def import_test_data(address):
	file = open(address, "r")
	values = file.read().split('\n')
	if (len(values) > 101):
		values = values[len(values)-100:len(values)]

	shuffle(values)

	ret = []  # list of all elements 
	outputs = {}  # output dict
	count = 0  # tracking output nodes

	# Returns first 50 pieces of consecutive data
	for i in range(0, min(len(values), 500), 1):
		inputElem = []
		rowElem = values[i].split(',')
		for j in range(0, len(rowElem) - 1, 1):
			if (j == len(rowElem)-2):
				if not (rowElem[j+1] in outputs.values()):
					outputs[count] = rowElem[j+1]
					count = count + 1
			try:
				inputElem += [float(rowElem[j])]
			except:
				continue

		ret += [inputElem + [list(outputs.values()).index(rowElem[len(rowElem) - 1])]]

	print("training:",[ret] + [outputs])
	return [ret] + [outputs]