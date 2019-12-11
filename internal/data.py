from random import seed, gauss

def GenerateData(points, sigma=0.5):
	data = []
	for point in points:
		for i in range(100):
			data.append({
				'x': gauss(point[0], sigma), 
				'y': gauss(point[1], sigma)})
	return data
							   