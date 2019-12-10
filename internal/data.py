from random import seed, gauss

seed(0)

def GenerateData(points, sigma=0.2):
	data = []
	for point in points:
		for i in range(100):
			data.append({
				'x': gauss(point[0], sigma), 
				'y': gauss(point[1], sigma)})
	return data
							   