def read_csv(pathfile):
	with open(pathfile, 'r') as file:
	# RIGA 1 labels
		row = file.readline()
		row = row.split(',')
		head = []
		for x in row:
			head.append(x.strip())

	# RIGA 2 e tutte le successive, creiamo una matrice di dati.
		matrix = []
		for row in file:
			temp = row.split(',')
		temp2 = []
		for x in temp:
			temp2.append(x.strip())
		matrix.append(temp2)
