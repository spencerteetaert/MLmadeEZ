import neural_network as n

def main():
	nn = n.NeuralNetwork([3, 4, 5, 4])
	print("Weights:", nn.get_weights())
	print("Values:", nn.get_values())
	nn.forward_propagate([.8, .2, .1, .9])
	print("Values:", nn.get_values())
main()
