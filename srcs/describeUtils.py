import math
import numpy as np

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
			res.append(np.nan)
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
			res.append(np.nan)
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
			res.append(np.nan)
	return (res)

def cent(matrix, nquant):
	columns = matrix.dtype.names
	ret = []
	for i in range(0, len(columns)):
		try:
			col = np.array(matrix[columns[i]], dtype=float)
		except:
			col = np.empty(len(matrix[columns[i]]))
			col[:] = np.nan
		col = col[~np.isnan(col)]
		if col.any():
			col.sort()
			index = (len(col) - 1) * (nquant / 100)
			lower = np.floor(index)
			upper = np.ceil(index)
			if lower == upper:
				ret.append(col[int(index)])
			else:
				first = col[int(lower)] * (upper - index)
				second = col[int(upper)] * (index - lower)
				ret.append(first + second)
		else:
			ret.append(np.nan)
	return ret

def transpose(matrix):
	ret = []
	for i in range(len(matrix[0])):
		row = []
		for x in matrix:
			row.append(x[i])
		try:
			row = [float(x) for x in row]
		except:
			pass
		row.sort()
		ret.append(row)
	return ret

def print_desc(head, arr, len_str):
	out = head
	for i in range(len(len_str)):
		if ~np.isnan(arr[i]):
			temp = "{:>" + str(len_str[i]) + "}"
			out = out + temp.format("%0.6f" % arr[i])
	print(out)

def	ft_len(f):
	str_len = 0
	if ~np.isnan(f):
		str_len = len(str(np.trunc(f))) + 5
	return str_len