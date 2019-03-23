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
				if (j < initConditions[i + 1] + 1):
					#Adding 0's to every node except bias
					l_valToAdd += [0]
				else:
					l_valToAdd += [1]

				nf_weightToAdd = []
				if (i + 1 < self.layers):
					for k in range(0, initConditions[i + 2] + 1):
						ranWeight = random.randint(-100, 100)/100
						nf_weightToAdd += [ranWeight]
					lf_weightToAdd += [nf_weightToAdd]
				else:
					for k in range(0, initConditions[i + 1] + 1):
						nf_weightToAdd += []
					lf_weightToAdd += [nf_weightToAdd]

			if (len(lf_weightToAdd) > 0):
				self.weights[0] += [lf_weightToAdd]
			self.values += [l_valToAdd]

		self.create_back_path(initConditions)

	def create_back_path(self, initConditions):
		for i in range(0, self.layers, 1):
			lb_weightToAdd = []

			for j in range(0, initConditions[i + 1] + 1):
				nb_weightToAdd = []
				if (i >= 1):
					for k in range(0, initConditions[i] + 1):
						nb_weightToAdd += [self.weights[0][i-1][k][j]]
				else:
					for k in range(0, initConditions[i + 1] + 1):
						nb_weightToAdd += []
				lb_weightToAdd += [nb_weightToAdd]

			if (len(lb_weightToAdd) > 0):
				self.weights[1] += [lb_weightToAdd]

		return True