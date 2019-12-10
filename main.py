from internal.network import *
from internal.data import *
from internal.plot import *
from random import choice

focals = [[2, 2],
          [2, 4],
          [4, 2]]

data = GenerateData(focals)

network = Network(2, 3)
point = choice(data)

plot = Plot()
plot.Scatter(data)
plot.Scatter(network.Unpacked())
plot.Show()