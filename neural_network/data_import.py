def import_weights(self, address):
	file = open(address, "r")
	count = 0
	values = file.read().split(',')
	ret = []

	print(values)