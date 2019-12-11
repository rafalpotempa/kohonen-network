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

	# scat, = plt.scatter([], [])
	#
	# def Animate(self, stream): # not working yet
	# 	pass
	# 	fig = plt.figure()
	# 	def init():
	# 		self.scat.set_data([], [])
	# 		return self.scat,
	# 	def animate(self, i, stream):
	# 		x = [point['x'] for point in stream['neurons']]
	# 		y = [point['y'] for point in stream['neurons']]
	# 		self.scat.set_data(x, y)
	# 		return self.scat,
	# 	anim = FuncAnimation(fig, animate, init_func=init,frames=100, blit=True, fargs=(stream))

