import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

class Plot:
	def Scatter(self, data):
		_data = {
			'x': [point['x'] for point in data],
			'y': [point['y'] for point in data]}

		plt.scatter('x', 'y', data=_data)
	def Show(self):
		plt.show()
	

if __name__ == "__main__":
	plt.style.use('seaborn-pastel')

	fig= plt.figure()
	ax= plt.axes(xlim=(0, 10), ylim=(-2, 10))
	line,= ax.plot([], [], lw=3)

	def init():
		line.set_data([], [])
		return line,
	def animate(i):
		x= np.linspace(0, 4, 1000)
		y= np.sin(2 * np.pi * (x - 0.01 * i))
		line.set_data(x, y)
		return line,

	anim= FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

	plt.show()
