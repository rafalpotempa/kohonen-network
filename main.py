from internal.network import *
from internal.data import *
from internal.plot import *
from random import choice, seed

seed(0)

focals = [[2, 5],
	      [2, 8],
	      [4, 5]]

data = GenerateData(focals)

network = Network(5, 5)
network.data = data

plot = Plot()
plot.Scatter(data)
plot.Scatter(network.Unpack())
plot.Show()

network.Train(1000)

plot.Scatter(data)
plot.Scatter(network.Unpack())
plot.Show()