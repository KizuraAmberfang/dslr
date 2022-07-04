import math
import numpy as np

def isNaN(num):
    return num != num

def mean(matrix):
	count = len(matrix[0])
	res = []
	for i in range(count):
		sum = 0
		n = 0
		for x in matrix:
			try: 
				float(x[i])
				if isNaN(float(x[i])) == 0 :
					n += 1
					sum += float(x[i])
			except:
				pass
		if n != 0:
			res.append(sum / n)
		else:
			res.append(np.nan)
	return res

def variance(matrix, mean):
	count = len(matrix[0])
	res = []
	for i in range(count):
		if mean[i] != np.nan:
			sum = 0
			n = 0
			for x in matrix:
				try:
					f = float(x[i])
					if isNaN(f) == 0:
						sum += (f - mean[i]) ** 2
						n += 1
				except:
					pass
			if n > 1:
				res.append(sum / (n - 1))
			else:
				res.append(np.nan)
		else:
			res.append(np.nan)
	return (res)

def std(matrix):
	res = []
	for x in matrix:
		if (x != np.nan):
			res.append(math.sqrt(x))
		else:
			res.append(np.nan)
	return res