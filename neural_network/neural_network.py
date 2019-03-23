import random
import math
import numpy

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
		for i in range(0, self.layers, 1): 
			l_valToAdd = []
			lf_weightToAdd = []
			#For each node + 1 bias 
			for j in range(0, initConditions[i + 1] + 1):
				if (j < initConditions[i + 1]):
					#Adding 0's to every node except bias
					l_valToAdd += [0]
				else:
					l_valToAdd += [1]

				nf_weightToAdd = []
				if (i + 1 < self.layers):
					#If the next layer exists, generate weights to
					for k in range(0, initConditions[i + 2] + 1):
						ranWeight = random.randint(-100, 100)/100
						nf_weightToAdd += [ranWeight]
					lf_weightToAdd += [nf_weightToAdd]
				else:
					#If this is last layer, add empty (for indexing)
					for k in range(0, initConditions[i + 1] + 1):
						nf_weightToAdd += []
					lf_weightToAdd += [nf_weightToAdd]

			if (len(lf_weightToAdd) > 0):
				self.weights[0] += [lf_weightToAdd]
			self.values += [l_valToAdd]

		#To allow for back-prop, create the second half of the array to allow for easy reverse indexing
		self.create_back_path(initConditions)

	def create_back_path(self, initConditions):
		for i in range(0, self.layers, 1):
			lb_weightToAdd = []

			for j in range(0, initConditions[i + 1] + 1):
				nb_weightToAdd = []
				if (i >= 1):
					for k in range(0, initConditions[i] + 1):
						#Fetches
						nb_weightToAdd += [self.weights[0][i-1][k][j]]
				else:
					for k in range(0, initConditions[i + 1] + 1):
						nb_weightToAdd += []
				lb_weightToAdd += [nb_weightToAdd]

			if (len(lb_weightToAdd) > 0):
				self.weights[1] += [lb_weightToAdd]

		return True

	##################
	### Operations ###
	##################

	def sigmoid(self, value):
		return (1/(1+math.exp(-1*val)))

	def re_value(self, x):
		for i in range(0, len(x), 1):
			self.values[0][i] = u[i]

		for i in range(1, self.layers, 1):
			for j in range(0, len(self.weights[1][i]), 1):
				accum = 0
				for k in range(0, len(self.weights[1][i-1]), 1):
					accum += self.values[i-1][k] * self.weights[1][i][j][k]
				self.values[i][j] = self.sigmoid(accum)
		return True

	def get_cost(self, u):
		cost = 0
		for i in range(0, len(u), 1):
			cost += (u[i] - self.values[self.layers - 1][i])**2
		return cost

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