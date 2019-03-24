def import_data(address):
	file = open(address, "r")
	values = file.read().split('\n')
	ret = []
	
	outputs = {}
	count = 0

	for j in range(0, len(values), 1):
		inputElem = []
		rowElem = values[j].split(',')
		for i in range(0, len(rowElem) - 1, 1):
			inputElem += [float(rowElem[i])]

			if (i == len(rowElem)-2):
				if not (rowElem[i+1] in outputs.values()):
					outputs[count] = rowElem[i+1]
					count = count + 1

		ret += [inputElem + [count-1]]

	return [ret] + [outputs]
	#print(values)