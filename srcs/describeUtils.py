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

def cent(matrix, count, nquant):
	cnt = len(count)
	res = []
	for i in range(cnt):
		if count[i] != "NaN":
			lst = matrix[i]
	# conto quanti elementi sono nulli, perchè dovrò saltarli
			nullind = len(lst) - count[i]
			n = (float)(count[i] * nquant)
			nint = int(n)
			if n - nint == 0:
				try:
					float(lst[nint - 1 + nullind])
					res.append(float(lst[nint - 1 + nullind]))
				except:
					res.append("NaN")
			else:
				lower = nint - 1 + nullind
				upper = lower + 1
				diff = (float(lst[upper]) - float(lst[lower])) * (n - nint)
				res.append(float(lst[lower]) + diff)
		else:
			res.append("NaN")
	return res

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

def print_desc(str, arr):
	out = str + "\t"
	for x in arr:
		if x != "NaN":
			out = out + "{:>15}".format("%0.6f" % x) + "\t"
	print(out)

def print_head(str, arr, app):
	out = str
	i = 0
	for x in app:
		if x != "NaN":
			# out = out + "{:>15}".format(arr[i])
			out = out + "  " + arr[i]
		i += 1
	print(out)

def describe(head, count, mean, std, min, cent_25, cent_50, cent_75, max):
	spaces = []
	spaces.append(7)
	for i in range(len(head)):
		n = 0
		if count[i] != "NaN":
			if n < len(head[i]):
				n = len(head[i])
			if (n < len(str(count[i]))):
				n = len(str(count[i]))
			if (n < len(str(mean[i]))):
				n = len(str(mean[i]))
			if (n < len(str(std[i]))):
				n = len(str(std[i]))
			if (n < len(str(min[i]))):
				n = len(str(min[i]))
			if (n < len(str(cent_25[i]))):
				n = len(str(cent_25))
			if (n < len(str(cent_50[i]))):
				n = len(str(cent_50))
			if (n < len(str(cent_75[i]))):
				n = len(str(cent_75))
			if (n < len(str(max[i]))):
				n = len(str(max[i]))
			if (n != 0):
				spaces.append(n + 2)
			else:
				spaces.append("NaN")
		else:
			spaces.append("NaN")
		print(n)
	return spaces