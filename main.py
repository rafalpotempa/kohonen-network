from internal.network import *
from internal.data import *
from internal.plot import *
from random import choice

foci = [[2, 2],
        [2, 4],
        [4, 2]]

data = GenerateData(foci)

network = Network(2, 3)

point = choice(data)

print(network.Closest(choice(data)))