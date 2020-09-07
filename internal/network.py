from random import choice

class Network:
	neurons: list
	data:	 list
	N: 		 int	# neighborhood
	alpha:	 float	# learning rate
	m:		 int
	n:		 int
	def __init__(self, m, n):
		self.N = 3
		self.m = m
		self.n = n
		self.alpha = 0.1
		self.neurons = [[{
			'x': 10*i/(m-1),
			'y': 10*j/(n-1)}
			for i in range(m)] for j in range(n)]

	def Closest(self, point):
		minDist = 1e10
		closest = []
		for j, row in enumerate(self.neurons):
			for i, neuron in enumerate(row):
				dist = ((neuron['x'] - point['x'])**2 + (neuron['y'] - point['y'])**2)**0.5
				if dist < minDist:
					minDist = dist
					closest = [i, j, neuron]
		return closest

	def Update(self, t, T):
		N = 1 + int((self.N - 1)*(1 - t/T))
		alpha = self.alpha*(1 - t/T)

		point = choice(self.data)
		closest = self.Closest(point)
		i, j, _ = closest

		left   = max(i - N, 0)
		right  = min(i + N, self.m) + 1
		bottom = max(j - N, 0)
		top    = min(j + N, self.n) + 1

		for row in self.neurons[bottom:top]:
			for neuron in row[left:right]:
				neuron['x'] += alpha*(point['x'] - neuron['x'])
				neuron['y'] += alpha*(point['y'] - neuron['y'])
		
	def Train(self, T):
		for epoch in range(T):
			self.Update(epoch, T)

	def Unpack(self):
		unpacked = []
		for row in self.neurons:
			for neuron in row:
				unpacked.append(neuron)

		return unpacked

