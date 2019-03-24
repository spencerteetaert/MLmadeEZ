# Code structure pulled from Jason Brownlee's neural network tutorial
# https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/ 

# Altered by MLmadeEZ, an IEEE NewHacks team
from math import exp
from random import seed
from random import random
from random import sample
from random import randint
from data_import import import_data
 
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
	for epoch in range(n_epoch):
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

	globalSettings.learningRate = 0.2
	globalSettings.nodes = 2
	epochs = 500

	network = train(globalSettings)
	# Step size
	# network size
	print("Network training success")

	dataset = import_data(globalSettings.importedFilePath, -1)

	print("dataset:",dataset)
	count = 0
	for i in range(0, len(dataset[0]), 1):		
		outputs = forward_propagate(network, dataset[0][i])
		current = [0, 0]
		for j in range(0, len(outputs), 1):
			if outputs[j] > current[0]:
				current = [outputs[j], j]
		#print(dataset[1][dataset[0][i][4]], dataset[1][current[1]])
		if (dataset[1][dataset[0][i][len(dataset[0][i])-1]] == dataset[1][current[1]]):
			count = count + 1
	print("Epochs:", epochs)
	print("Hidden nodes:", globalSettings.nodes)
	print("Learning rate:", globalSettings.learningRate)
	print(round(count/len(dataset[0])*100, 2), "% success rate")

def train(globalSettings):
	# Test training backprop algorithm
	globalSettings.learningRate = 0.2
	globalSettings.nodes = 2
	epochs = 500

	# 4 x n + n x 

	print("Network is training...")
	seed(1)

	dataset = import_data(globalSettings.importedFilePath, 0)
	n_inputs = len(dataset[0][0]) - 1
	n_outputs = len(set([row[-1] for row in dataset[0]]))
	network = initialize_network(n_inputs, globalSettings.nodes, n_outputs)

	for i in range(0, 10, 1):
		dataset = import_data(globalSettings.importedFilePath, i)
		train_network(network, dataset[0], globalSettings.learningRate, epochs, n_outputs)

	return network

	# while True:
	# 	rand = randint(0, 149)
	# 	input("...")

	# 	outputs = forward_propagate(network, dataset[0][rand])
	# 	current = [0, 0]
	# 	for i in range(0, len(outputs), 1):
	# 		if outputs[i] > current[0]:
	# 			current = [outputs[i], i]
	# 	print("At data point", current[1], "desired answer:", dataset[1][dataset[0][rand][4]])
	# 	print("Prediction:", dataset[1][current[1]], "with", round(current[0]*100, 1), "% certainty")
	# 	if (dataset[1][dataset[0][rand][4]] == dataset[1][current[1]]):
	# 		print("#Success")
	# 	else:
	# 		print("#Fail")

	# while True:
	# 	inputString = input("Enter test case:\n")
	# 	temp = inputString.split(',')
	# 	inputList = []
	# 	for i in range(0, len(temp), 1):
	# 		inputList += [float(temp[i])]

	# 	outputs = forward_propagate(network, inputList)
	# 	current = [0, 0]
	# 	for i in range(0, len(outputs), 1):
	# 		if outputs[i] > current[0]:
	# 			current = [outputs[i], i]

	# 	print("Prediction:", dataset[1][current[1]], "with", round(current[0]*100, 1), "% certainty\n")