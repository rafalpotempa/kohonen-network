from random import seed, gauss
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

seed(0)

def GenerateData(points, sigma=0.2):
	data = []
	for point in points:
		for i in range(100):
			data.append([gauss(point[0], sigma), gauss(point[1], sigma)])
	return data

foci = [
	[2,2], 
	[2,4], 
	[4,2]
]

plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-2, 10))
plt.scatter(*zip(*GenerateData(foci)))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()							   