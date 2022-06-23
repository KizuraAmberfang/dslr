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
			label_type.append((label[i], "<f4"))
		else:
			label_type.append((label[i], '<U20'))
		i += 1
	ret = np.array(matrix, dtype=label_type)
	return ret

def read_csv_to_list(pathfile, sep=','):
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
		for r in file:
			temp = r.split(sep)
			temp2 = []
			for x in temp:
				try:
					value = float(x)
				except:
					if (str(x) != ""):
						value = str(x)
					else:
						value = np.nan
				temp2.append(value)
			matrix.append(temp2)
	label_type = []
	i = 0
	for x in matrix[0]:
		if isinstance(x, float):
			label_type.append("<f4")
		else:
			label_type.append('<U20')
		i += 1
	# ret = np.array(matrix, dtype={'names': label, 'formats': label_type})
	ret = np.array(matrix)
	return ret
