all:	train calc

calc:
		python3 main.py

train:
		python3 maintrainer.py

desc:
		python3 srcs/describe.py data/dataset_train.csv

hist:
		python3 srcs/histogram.py data/dataset_train.csv