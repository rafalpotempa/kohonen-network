
class Network:
	neurons = []

	def __init__(self, m, n):
		self.neurons = [[{
			'x': 10*i/(m-1),
			'y': 10*j/(n-1)}
			for i in range(m)] for j in range(n)]

	def Closest(self, point):
		minDist = 1e10
		closest = []
		for i, row in enumerate(self.neurons):
			for j, neuron in enumerate(row):
				dist = ((neuron['x'] - point['x'])**2 + (neuron['y'] - point['y'])**2)**0.5
				if dist < minDist:
					minDist = dist
					closest = [i, j, neuron]
		return closest

	def Update(self):
		pass

	def Unpacked(self):
		unpacked = []
		for row in self.neurons:
			for neuron in row:
				unpacked.append(neuron)

		return unpacked

