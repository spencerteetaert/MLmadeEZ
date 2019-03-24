# Code structure pulled from Jason Brownlee's neural network tutorial
# https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/ 

# Adapted and modified by MLmadeEZ, an IEEE NewHacks team
from math import exp
from random import seed
from random import random
from random import sample
from random import randint
from data_import import *
 
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network
 
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
 
# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))
 
# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs
 
# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)
 
# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
		#print(neuron['delta'])
 
# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']
 
# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	sizeOfSubset = len(train)//n_epoch
	for epoch in range(n_epoch - n_epoch//10):
		dataset = list(train[epoch*sizeOfSubset:epoch*sizeOfSubset+sizeOfSubset])
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		#print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
 
def bridge(globalSettings):
	# Test training backprop algorithm
	# globalSettings.learningRate = 0.2
	# globalSettings.nodes = 2

	print("Network is training...")
	#print(globalSettings.nodes)
	#seed(1)

	trainingData = import_data(globalSettings.importedFilePath)
	n_inputs = len(trainingData[0][0]) - 1
	n_outputs = len(set([row[-1] for row in trainingData[0]]))
	network = initialize_network(n_inputs, globalSettings.nodes, n_outputs)
	train_network(network, trainingData[0], globalSettings.learningRate, globalSettings.epochs, n_outputs)	
	print("Network training success")
	#print(network)

	#print("dataset:",dataset)
	testDataSet = import_test_data(globalSettings.importedFilePath, trainingData[1])
	count = 0
	for i in range(0, len(testDataSet[0]), 1):		
		outputs = forward_propagate(network, testDataSet[0][i])
		current = [0, 0]
		for j in range(0, len(outputs), 1):
			if outputs[j] > current[0]:
				current = [outputs[j], j]
		print(trainingData[1][testDataSet[0][i][len(testDataSet[0][i])-1]], trainingData[1][current[1]])
		if (trainingData[1][testDataSet[0][i][len(testDataSet[0][i])-1]] == trainingData[1][current[1]]):
			count = count + 1

	print("Epochs:", globalSettings.epochs)
	print("Hidden nodes:", globalSettings.nodes)
	print("Learning rate:", globalSettings.learningRate)
	print(round(count/len(testDataSet[0])*100, 2), "% success rate")

	return network