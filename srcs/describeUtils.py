import math

def isNaN(num):
    return num != num

def count(matrix):
	count = len(matrix[0])
	res = []
	for i in range(count):
		n = 0
		for x in matrix:
			try:
				float(x[i])
				if isNaN(float(x[i])) == 0 :
					n += 1
			except:
				pass
		if n > 0:
			res.append(n)
		else:
			res.append("NaN")
	return res

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
			res.append("NaN")
	return res

def variance(matrix, mean):
	count = len(matrix[0])
	res = []
	for i in range(count):
		if mean[i] != "NaN":
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
				res.append("NaN")
		else:
			res.append("NaN")
	return (res)

def std(matrix):
	res = []
	for x in matrix:
		if (x != "NaN"):
			res.append(math.sqrt(x))
		else:
			res.append("NaN")
	return res

def min(matrix):
	count = len(matrix[0])
	res = []
	for i in range(count):
		min = float("inf")
		n = 0
		for x in matrix:
			try: 
				f = float(x[i])
				if isNaN(f) == 0 and f < min:
					n += 1
					min = f
			except:
				pass
		if n != 0:
			res.append(min)
		else:
			res.append("NaN")
	return (res)


def max(matrix):
	count = len(matrix[0])
	res = []
	for i in range(count):
		max = float("-inf")
		n = 0
		for x in matrix:
			try: 
				f = float(x[i])
				if isNaN(f) == 0 and f > max:
					n += 1
					max = f
			except:
				pass
		if n != 0:
			res.append(max)
		else:
			res.append("NaN")
	return (res)


def print_desc(str, arr):
	out = str + "\t"
	for x in arr:
		if x != "NaN":
			out = out + "%0.6f" % x + "\t"
	print(out)