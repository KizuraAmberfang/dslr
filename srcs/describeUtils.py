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
				if x[i].upper() != 'NAN':
					n += 1
			except:
				pass
		res.append(n)
	out = "count\t\t"
	headout = "\t\t"
	i = 0
	for x in res:
		if (x != 0):
			headout = headout + head[i] + "\t"
			out = out + str(x) + "\t"
		i += 1
	print(headout)
	print(out)