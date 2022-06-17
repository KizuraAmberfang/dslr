all:	train calc

calc:
		python3 main.py

train:
		python3 srcs/logreg_train.py data/dataset_train.csv

desc:
		python3 srcs/describe.py data/dataset_train.csv

hist:
		python3 srcs/histogram.py data/dataset_train.csv

scatter:
		python3 srcs/scatter_plot.py data/dataset_train.csv

pair:
		python3 srcs/pair_plot.py data/dataset_train.csv