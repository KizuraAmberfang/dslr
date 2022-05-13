def isNaN(num):
    return num != num

def count(matrix, head):
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
		res.append(n)
	out = "count\t"
	headout = "\t\t"
	i = 0
	for x in res:
		if (x != 0):
			headout = headout + head[i] + "\t"
			out = out + "%0.6f" % x + "\t"
		i += 1
	print(headout)
	print(out)

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
	out = "mean\t"
	for x in res:
		out = out + "%0.6f" % x + "\t"
	print(out)

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
	out = "min\t"
	for x in res:
		out = out + "%0.6f" % x + "\t"
	print(out)

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
	out = "max\t"
	for x in res:
		out = out + "%0.6f" % x + "\t"
	print(out)