import random
import math
import numpy
import scikit

class NeuralNetwork:
	######################
	### Initialization ###
	######################

	def __init__(self, initConditions):
		# initConditions = [ numLayers, numNodes, nuNodes, ... ]
		self.layers = initConditions[0]
		self.weights = [[],[]] # 0: forward weights 1: backward weights
		self.values = []

		#For each layer
		for layer in range(0, self.layers, 1): 
			l_valToAdd = []
			lf_weightToAdd = []
			#For each node + 1 bias 
			for node in range(0, initConditions[layer + 1] + 1):
				if (node < initConditions[layer + 1]):
					#Adding 0's to every node except bias
					l_valToAdd += [0]
				else:
					l_valToAdd += [1]

				nf_weightToAdd = []
				if (layer + 1 < self.layers):
					#If the next layer exists, generate weights to
					for nextNode in range(0, initConditions[layer + 2] + 1):
						ranWeight = random.randint(-100, 100)/100
						nf_weightToAdd += [ranWeight]
					lf_weightToAdd += [nf_weightToAdd]
				else:
					#If this is last layer, add empty (for indexing)
					for nextNode in range(0, initConditions[layer + 1] + 1):
						nf_weightToAdd += []
					lf_weightToAdd += [nf_weightToAdd]

			if (len(lf_weightToAdd) > 0):
				self.weights[0] += [lf_weightToAdd]
			self.values += [l_valToAdd]

		#To allow for back-prop, create the second half of the array to allow for easy reverse indexing
		self.create_back_path(initConditions)

	def create_back_path(self, initConditions):
		for layer in range(0, self.layers, 1):
			lb_weightToAdd = []

			for nextNode in range(0, initConditions[layer + 1] + 1):
				nb_weightToAdd = []
				if (layer >= 1):
					for node in range(0, initConditions[layer] + 1):
						#Fetches
						nb_weightToAdd += [self.weights[0][layer-1][node][nextNode]]
				else:
					for node in range(0, initConditions[layer + 1] + 1):
						nb_weightToAdd += []
				lb_weightToAdd += [nb_weightToAdd]

			if (len(lb_weightToAdd) > 0):
				self.weights[1] += [lb_weightToAdd]

		return True

	##################
	### Operations ###
	##################

	def sigmoid(self, x):
		return (1/(1+math.exp(-1*x)))

	def forward_propagate(self, x):
		for i in range(0, len(x), 1):
			self.values[0][i] = x[i]

		for layer in range(1, self.layers, 1):
			for node in range(0, len(self.weights[1][layer]), 1):
				accum = 0
				for pastNode in range(0, len(self.weights[1][layer-1]), 1):
					accum += self.values[layer-1][pastNode] * self.weights[1][layer][node][pastNode]
				self.values[layer][node] = self.sigmoid(accum)
		return True

	def get_cost(self, expected):
		cost = 0
		output = self.values[self.layers - 1]
		for i in range(0, len(expected), 1):
			cost += (expected[i] - output[i])*transfer_derivative(output[i])
		return cost

	def transfer_derivative(self, output):
		return output * (1 - output)

	def back_propagate_error(self, x):
		#Start w output, calc error ()
		for layer in range(len(self.weights[0]), -1, -1):
			return True

	#####################
	### Gets and Sets ###
	#####################

	def get_weights(self):
		return self.weights
	def get_values(self):
		return self.values

	##########################
	### Data export/import ###
	##########################

	def import_weights(self, address):
		file = open(address, "r")
		count = 0
		values = file.read().split(',')
		for i in range(0, 2, 1):
			for j in range(0, len(self.weights[i]), 1):
				for k in range(0, len(self.weights[i][j]), 1):
					for q in range(0, len(self.weights[i][j][k]), 1):
						self.weights[i][j][k][q] = float(values[count])
						count = count + 1
		return True

	def export_weights(self, address):
		file = open(address, "w+")

		for i in range(0, 2, 1):
			for j in range(0, len(self.weights[i]), 1):
				for k in range(0, len(self.weights[i][j]), 1):
					for q in range(0, len(self.weights[i][j][k]), 1):
						file.write(str(self.weights[i][j][k][q]) + ',')

		return True