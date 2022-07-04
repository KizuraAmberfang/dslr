import numpy as np

def read_csv(pathfile, sep=','):
	with open(pathfile, 'r') as file:
	# RIGA 1 labels
		row = file.readline()
		label_temp = []
		label = []
		temp = row.split(sep)
		for x in temp:
			label_temp.append((x.strip(), 'f4'))
			label.append(x.strip())
	# RIGA 2 e tutte le successive, creiamo una matrice di dati.
		matrix = []
		for row in file:
			temp = row.split(sep)
			temp2 = []
			for x in temp:
				try:
					value = float(x)
				except:
					if (str(x) != ""):
						try:
							value = np.datetime64(str(x))
						except:
							value = str(x)
					else:
						value = np.nan
				temp2.append(value)
			matrix.append(tuple(temp2))
	label_type = []
	row = matrix[0]
	i = 0
	for x in row:
		if isinstance(x, float):
			label_type.append((label[i], np.float32))
		elif isinstance(x, np.datetime64):
			label_type.append((label[i], object))
		else:
			label_type.append((label[i], 'U32'))
		i += 1
	ret = np.array(matrix, dtype=label_type)
	return ret